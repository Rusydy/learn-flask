from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route for the main page
@app.route('/')
def index():
    return 'Hello World!'

# route for the upload page
@app.route('/page/upload')
def upload_page():
    return render_template('upload.html')

# get uploade file from request and save it to /uploads folder
@app.route('/upload', methods=['POST'])
def upload():
    # get file from request
    file = request.files['file']
    # if file is not empty return error with message
    if file == '':
        return 'No selected file'

    # if file is not empty save it to /uploads folder
    if file:
        # get filename
        filename = file.filename
        # save file to /uploads folder
        file.save(os.path.join('uploads', filename))
        return 'File uploaded successfully'


app.run(host='localhost', port=5000)

''' 
Run the above code using the following command in the terminal to start the server
    export FLASK_APP=main.py
    export FLASK_ENV=development
    flask run
'''
