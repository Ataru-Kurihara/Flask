from flask import Flask, render_template

app = Flask(__name__)


# Top Page
@app.route("/hello")
def index():
    values = {"name": "Taro"}
    return render_template('index.html', data=values)


# Second Page
@app.route("/test")
def test():
    values = {"message": "Hello! This is test page."}
    return render_template('test.html', data=values)


@app.route("/")
def top():
    return render_template('top.html')

@app.route("/login")
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
