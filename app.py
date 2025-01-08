from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/produk')
def produk():
    return render_template('Produk.html')

@app.route('/register')
def register():
    return render_template('Register.html')

if __name__ == '__main__':
    app.run(debug=True)
