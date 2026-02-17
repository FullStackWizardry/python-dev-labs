""" 
upload file with html form
"""
from flask import Flask, request
import os

app=Flask(__name__)
os.makedirs("uploads",exist_ok=True)

@app.route("/",methods=["GET","POST"])
def upload():
    if request.method=="POST":
        f=request.files["file"]
        f.save("uploads/"+f.filename)
        return "uploaded"
    return '''
    <form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <button>Upload</button>
    </form>
    '''

app.run()