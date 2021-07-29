from flask import Flask, render_template, redirect, url_for, request, make_response

app = Flask(__name__)

@app.route('/home')
def main():
    return "WHAT NOW?"

@app.route('/login', methods = ['POST', 'GET'])
def login():
    return render_template("login.html")

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    form = request.form
    user = form['username']
    print("GOT IT")
    res = make_response()
    res.set_cookie('username', user)
    return redirect(url_for('main'))

@app.route('/new')
def new():
    return render_template("new.html")


if __name__ == '__main__':
    app.run(debug = True)