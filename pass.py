from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

def generate_password(length):
    Upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
    Lower = "qwertyuiopasdfghjklzxcvbnm"
    Digits = "0123456789"
    Symbols = "!@#$&*"

    Password = ""

    # Ensure at least one from each category
    Password += random.choice(Upper)
    Password += random.choice(Lower)
    Password += random.choice(Digits)
    Password += random.choice(Symbols)

    all_chars = Upper + Lower + Digits + Symbols

    while len(Password) < length:
        Password += random.choice(all_chars)

    Password = list(Password)
    random.shuffle(Password)

    return "".join(Password)

@app.route("/", methods=["GET", "POST"])
def home():
    password = ""

    if request.method == "POST":
        try:
            length = int(request.form.get("length"))

            if length < 4:
                password = "Minimum length is 4"
            else:
                password = generate_password(length)

        except:
            password = "Enter a valid number"

    return render_template("index.html", password=password)

# Render deployment config
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)