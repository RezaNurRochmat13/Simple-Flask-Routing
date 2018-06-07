from flask import Flask

app = Flask(__name__)

# Routing to index path
@app.route("/")
def index():
    return 'Welcome in Phyton Flask'

# Routing to profile path
@app.route("/profile/<username>")
def profile(username):
    return 'Welcome in profile pages. Hello my name is %s' % username

# Routing to about path
@app.route("/about/<username>")
def about(username):
    return 'Welcome in about pages %s' % username

# Routing to contact path
@app.route("/contact/<username>")
def contact(username):
    return 'Welcome in contact pages %s' % username
