from flask import Flask, render_template
import glob
from datetime import datetime
import os

app = Flask(__name__, template_folder='templates') 

@app.route("/category/<c>")
def category(c):
  fs = glob.glob("articles/" + c + "/*.txt")
  fill = []
  for f in fs:
      fp = f.split("/")[-1].replace(".txt", "")
      utc = datetime.utcfromtimestamp(os.path.getmtime(f))
      t = (fp, str(utc))
      fill.append(t)
  return render_template("category.html", cat=fill, title=c)

@app.route("/")
def home():
  return "hello"

if __name__ == '__main__':
  app.run(debug=True)
