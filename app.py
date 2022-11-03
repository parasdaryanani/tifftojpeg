from converter_api import convert_tiff_to_jpg, clean_up, zip_files
from flask import Flask
from flask import request, redirect, url_for, send_from_directory, abort
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'input')
OUTPUT_FOLDER = os.path.join(os.getcwd(), 'output')
ALLOWED_EXTENSIONS = {'tif','tiff'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.secret_key = 'super secret key'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return redirect(url_for('static', filename='index.html'))

@app.route('/upload', methods=['POST'])
def upload_file():
   clean_up()
   if request.method == 'POST':
      file = request.files['file']
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      convert_tiff_to_jpg(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      try:
        return send_from_directory(directory= app.config['OUTPUT_FOLDER'], path= filename.replace('.tiff', '.jpg').replace('.tif', '.jpg'), as_attachment=True)
      except FileNotFoundError:
        abort(500)

@app.route('/upload-multi', methods=['POST'])
def upload_files():
   clean_up()
   if request.method == 'POST':
      uploaded_files = request.files.getlist("files")
      for file in uploaded_files:
        filename = secure_filename(file.filename)      
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        convert_tiff_to_jpg(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      zip_files()
      try:
        return send_from_directory(directory= app.config['OUTPUT_FOLDER'], path= "converted.zip", as_attachment=True)
      except FileNotFoundError:
        abort(500)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=5000)