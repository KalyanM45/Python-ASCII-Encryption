from flask import Flask, render_template, request

app = Flask(__name__)

def encrypt(text, key=0):
    if not isinstance(text, str):
        raise TypeError("{} should be a type string".format(text))
    if not isinstance(key, int):
        raise TypeError("{} should be of type int".format(key))
    return "".join([chr(ord(something) + key) for something in text])

def decrypt(text, key=0):
    if not isinstance(text, str):
        raise TypeError("{} should be a type string".format(text))
    if not isinstance(key, int):
        raise TypeError("{} should be of type int".format(key))
    return "".join([chr(ord(something) - key) for something in text])

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    operation = None

    if request.method == "POST":
        text = request.form.get("text")
        key = int(request.form.get("key"))
        choice = request.form.get("choice")

        if choice == "encrypt":
            result = encrypt(text, key)
            operation = "Encrypted"
        elif choice == "decrypt":
            result = decrypt(text, key)
            operation = "Decrypted"

    return render_template("home.html", result=result, operation=operation)

if __name__ == "__main__":
    app.run(debug=True)
