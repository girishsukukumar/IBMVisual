#from cloudant import Cloudant
from flask import Flask, flash, request, redirect, url_for
from watson_developer_cloud import VisualRecognitionV3
import atexit
import os
import json
import time
app = Flask(__name__, static_url_path='')

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 7000))

apikey='hnueCLEdY6bxW_-qM2jucYc11a46FbCw--yd5PnUCAxe'
UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def root():
    return app.send_static_file('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploadsimple_post', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'myFile' not in request.files:
            flash('No file part')
            return redirect(request.url)
        print "1"
        print request.url
        file = request.files['myFile']
        # if user does not select file, browser also
        # submit an empty part without filename
        print file.filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        print "3"
        file.save(file.filename)
        print "6"
        thresh = 0.6
        print ">>7"
        #fileName = file.filename
        fileName = "b1.jpeg" 
        visual_recognition = VisualRecognitionV3( '2018-03-19', iam_api_key=apikey)

        classes = visual_recognition.classify(images_file=fileName, threshold=thresh)
        time.sleep(10)
        print ">>8"
        score  = 0 
        bestClass = ' '
        #print classes  
        #for a in classes['images'][0]['classifiers'][0]['classes']:
        #   val  = float(a['score'])

        #   print(a['score'] , val)
        #   if score < val:
        #      score = val
        #      bestClass = a['class']

        score = round(score,2) * 100
        bestMatchStr = "Best match" + bestClass 
        ConfidenceStr = " I am " +  str(score) + "% confident"
        retString = "<HTML>"  + bestMatchStr +   ConfidenceStr + "</HTML>"
        return retString
        #print ("Best match", bestClass , "With a confidence of ", score)
 
        #return app.send_static_file('index.html')
        #return  request.url 
    return

@atexit.register
def shutdown():
    return 

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=port, debug=True)
