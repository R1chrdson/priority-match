from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "SecretKey"


@app.route('/')
def home():
    return render_template('tml.tml')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
