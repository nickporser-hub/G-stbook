from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    # Läs in alla gamla inlägg
    with open("guestbook.json", "r", encoding="utf-8") as file:
        posts = json.load(file)

    if request.method == "POST":

        name = request.form["name"]
        message = request.form["message"]

        # Lägg till det nya inlägget först
        posts.insert(0, {
            "name": name,
            "message": message
        })

        # Spara till JSON
        with open("guestbook.json", "w", encoding="utf-8") as file:
            json.dump(posts, file, ensure_ascii=False, indent=4)

    # Skicka posts till HTML
    return render_template("index.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)