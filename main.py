from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Простая база данных пользователей (в реальном приложении используйте БД)
users = {
    'user1': 'password1',
    'user2': 'password2'
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        test = request.form.get('test', None)
        if users.get(username) == password:
            return redirect(url_for('dashboard'))
        else:
            return 'Login Failed'
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return 'Welcome to the Dashboard'


if __name__ == '__main__':
    app.run(debug=True)
