from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

friends_dict = [
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "pages": "295", "classification": "Fiction", "details": "Recommend, Read", "acquisition": "It was a gift."}
]


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Web form template", friends=friends_dict
    )


@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        title = form["title"]
        author = form["author"]
        pages = form["pages"]
        details = form.getlist("details")  # this is a PYthon list
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
            "acquisition": acquisition
            }

        print(friend_dict)
        friends_dict.append(
            friend_dict
        )  # append this dictionary entry to the larger friends dictionary
        print(friends_dict)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", pageTitle="About My Library"
    )


if __name__ == "__main__":
    app.run(debug=True)
