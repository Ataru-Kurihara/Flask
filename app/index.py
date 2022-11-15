from collections import defaultdict

from flask import Flask, render_template, Response, request, abort
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = "secret"


class User(UserMixin):
    def __init__(self, id, mailaddress, password):
        self.id = id
        self.mailaddress = mailaddress
        self.password = password


users = {
    1: User(1, "aaaa@com", "password"),
    2: User(2, "bbbb@com", "password")
}

nested_dict = lambda: defaultdict(nested_dict)
user_check = nested_dict()
for i in users.values():
    user_check[i.mailaddress]["password"] = i.password
    user_check[i.mailaddress]["id"] = i.id


@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))


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
    # return Response("home: <a href='/login/'>Login</a> <a href='/protected/'>Protected</a> <a "
    #                 "href='/logout/'>Logout</a>")
    return render_template('top.html')


@app.route('/protected/')
@login_required
def protected():
    return Response('''
    protected<br />
    <a href="/logout/">logout</a>
    ''')


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # ユーザーチェック
        if request.form["mailaddress"] in user_check and request.form["password"] == user_check[request.form["mailaddress"]
        ]["password"]:
            # ユーザーが存在した場合はログイン
            login_user(users.get(user_check[request.form["mailaddress"]]["id"]))
            return Response('''
                login success!<br />
                <a href="/protected/">protected</a><br />
                <a href="/logout/">logout</a>
                ''')
        else:
            return abort(401)
    else:
        return render_template("login.html")
    # return render_template('login.html')


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return Response('''
    logout success!<br />
    <a href="/login/">login</a>
    ''')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
