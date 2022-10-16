from flask import Flask, request, render_template, url_for
from markupsafe import escape

app = Flask(__name__)

# name = request.args.get("name", "World")
    # return f'Hello, {escape(name)}!'
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/profileConsumer")
def profileConsumer():
    return render_template('profileConsumer.html')


@app.route("/profileProfessional")
def profileProfessional():
    return render_template('profileProfessional.html')

@app.route('/signin')
def signin():
    return render_template('signin.html', title='Signin')

@app.route('/signupConsumer')
def signupConsumer():
    return render_template('signupConsumer.html', title='Signup Consumer')


@app.route('/signupProfessional')
def signupProfessional():
    return render_template('signupProfessional.html', title='Signup Professional')



if __name__ == '__main__':
    app.run(debug=True)