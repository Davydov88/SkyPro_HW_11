from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/',)
def my_wife():

    return render_template("my_wife.html",)


app.run(debug=True)