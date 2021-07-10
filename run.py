# Python file meant to run the website through flask. 
from flask import Flask, render_template
app = Flask(__name__, images_url_path='')

@app.route("/")
def home():
    return render_template('main.html')
    
if __name__ == '__main__':
   app.run()