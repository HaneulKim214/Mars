from flask import Flask, render_template

posts = [
    {
        'author': "Hanna Jung",
        "title": "Blog Post 1",
        "content": "First post coentet"
    },
    {
        'author': "Hanneul",
        "title": "Blog Post 2",
        "content": "Second post coentet"
    }
]


app = Flask(__name__)

# both route will run hello function.
@app.route("/home")
@app.route("/")
def hello():
    return render_template('home.html', p=posts, title="Home Page")


@app.route("/about")
def about():
    return render_template("about.html", title="About page")


if __name__ == "__main__":
    app.run()