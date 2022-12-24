
import flask
import werkzeug
import time
import os
from test_grader import *
app = flask.Flask(__name__)

@app.route('/upload', methods=['POST'])
def handle_request():
    #result=predictOutput("D:/comsats project/AI part/fyp/2.JPG")
    print("here1")
    files_ids = flask.request.files.getlist("file")
    print("\nNumber of Received Images : ", len(files_ids))
    image_num = 1
    for file_id in files_ids:
        print("\nSaving Image ", str(image_num), "/", len(files_ids))
        imagefile = flask.request.files[file_id]
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        print("Image Filename : " + imagefile.filename)
        timestr = time.strftime("%Y%m%d")
        path = "testinmges/"+timestr
        print(path)
        isFile = os.path.exists(path)
        print(isFile)
        if isFile==False:
            os.mkdir("testinmges/"+timestr)
        timestr2 = time.strftime("%Y%m%d-%H%M%S")
        imagefile.save("testinmges/"+timestr+"/"+timestr2+'_'+filename)
        image_num = image_num + 1
    result=predictOutput("testinmges/"+timestr+"/"+timestr2+'_'+filename)
    return result
@app.route('/',methods=["GET"])
def index():

        # result=predictOutput("D:/comsats project/AI part/fyp/2.JPG")

    return "result"
ports=0
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
