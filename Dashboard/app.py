from flask import Flask,render_template
app = Flask(__name__, static_folder='static',template_folder='templates')

@app.route("/")
def hello():
    return "Hello World!"
@app.route('/html')
def html():
    return render_template('index.html')
@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)
if __name__ == "__main__":
    app.run()
