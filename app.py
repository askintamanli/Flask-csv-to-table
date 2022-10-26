from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def upload():
   return render_template("upload_form.html")

@app.route("/succses" , methods = ["POST","GET"])
def succses():
   
   if request.method == "POST":
      file = request.files['file']
      if file:
         name = file.filename
         df = pd.read_csv(file)
         
      
         return render_template("succses.html", name = name, df = df ) 

   return render_template("succses.html", name = file.filename )


if __name__ == "__main__" : 
    app.run(debug = True)