from flask import Flask
app = Flask(__name__)
# Route 1 - Home
@app.route("/" )
def home():
    return "Welcome to the Home Page!"

# Route 2 - About
@app.route("/about")
def about():
    return "This is the About Page."

# Route 3 - Contact
@app.route("/contact")
def contact():
    return "You can reach us at contact@example.com."

# Route 4 - Services
@app.route("/services")
def services():
    return "Here are our services."

# Route 5 - Help
@app.route("/help")
def help_page():
    return "This is the Help Page."

if __name__ == "__main__":
    app.run(debug=True)
