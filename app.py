from flask import Flask ,render_template, request
import main_file as m
app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])

def hello():

    li = m.main()

    mk=li

    return render_template("index.html", data=mk)
'''@app.route('/my-link/')
def my_link():
  return hello()'''


if __name__ == "__main__":
    app.run(debug=True)