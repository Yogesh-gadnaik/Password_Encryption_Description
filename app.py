from flask import Flask, render_template, request
from logic import database_entry, hide_pass

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('index.html')


@app.route('/database', methods=['POST', 'GET'])
def Entry():
    name = request.form['name']
    password = request.form['pass']
    gender = request.form['gender']
    city = request.form['city']

    Encrypted_pass = hide_pass(password)
    response = database_entry(name, Encrypted_pass, gender, city)
    if response == 1:
        return render_template('response.html', name=name, msg='Your Information Successfully recorded')
    else:
        return render_template('response.html', name=name, msg='Something went wrong please try again ')


@app.route('/new')
def new_register():
    return render_template('register.html')


@app.route('/check', methods=['POST', 'GET'])
def check_register():
    name = request.form['name']
    password = request.form['pass']
    from logic import check_password
    response = check_password(name, password)
    print(response)
    if response == 1:
        return 'Yes this is valid user'
    else:
        return 'Do not have an accout please register first'


@app.route('/reset')
def new_reset():
    return render_template('reset.html')


@app.route('/recover', methods=['POST', 'GET'])
def recover_password():
    name = request.form['name']
    city = request.form['city']
    newpass = request.form['newpass']
    from logic import recover
    response = recover(name, city, newpass)
    # print(response)
    if response:
        return 'Your Password is changed'
    else:
        return 'Please try again later'


if __name__ == '__main__':
    app.run(debug=True)
