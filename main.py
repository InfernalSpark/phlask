from flask import Flask, render_template, redirect, url_for, request, make_response

app = Flask(__name__)

@app.route('/')
def main():
    print("")
    return "WHAT NOW?"

@app.route('/login', methods = ['POST', 'GET'])
def login():
    return render_template("login.html")
    form = request.form
    user = form['username']
    print("GOT IT")
    res = make_response()
    res.set_cookie('username', user)

if __name__ == '__main__':
    app.run(debug = True)