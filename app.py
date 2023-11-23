from flask import Flask, render_template, request, redirect, url_for


app = Flask("app")

@app.route("/", methods = ['GET', 'POST'])
def func():
    if request.method == 'POST':
        username = request.form['name']
        if username:
            return redirect(url_for('hello', name = username))
    else:
        return render_template('home.html')

@app.route("/hello-<name>", methods = ['GET', 'POST'])
def hello(name):
    return render_template("hello.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)