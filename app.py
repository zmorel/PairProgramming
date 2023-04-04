from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)

app.config["SECRET_KEY"] = "b'_5#y2L\"F4Q8z\\n\\xec]/'"

friends_dict = [
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "pages": "295",
        "classification": "Fiction",
        "details": "Recommend, Read",
        "acquisition": "It was a gift.",
    }
]


# Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", pageTitle="Web form template", friends=friends_dict)


@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        title = form["title"]
        author = form["author"]
        pages = form["pages"]
        details = form.getlist("details")  # this is a Python list
        classification = form["classification"]
        acquisition = form["acquisition"]

        print(title)
        print(author)
        print(pages)
        print(details)
        print(classification)
        print(acquisition)

        details_string = ", ".join(details)  # make the Python list into a string

        friend_dict = {
            "title": title,
            "author": author,
            "pages": pages,
            "details": details_string,
            "classification": classification,
            "acquisition": acquisition,
        }

        print(friend_dict)
        friends_dict.append(friend_dict)  # append this dictionary entry to the larger friends dictionary
        flash("Record successfully added.", "success")
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", pageTitle="About My Library")


if __name__ == "__main__":
    app.run(debug=True)
