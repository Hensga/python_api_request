from flask import Flask, redirect, url_for
import requests

app = Flask(__name__)

response = requests.get('https://randomfox.ca/floof')
response.status_code

# print(response.json())

responseImg = response.json()

fox = responseImg['image']


@app.route("/")
def home():
    return "<h1 style='text-align: center;'>My Fox of the Day</h1>" + f"<img src='{fox}'>"


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()
