from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/python_projects")
def python_projects():
    return render_template("python_project.html")

@app.route("/web_dev")
def web_dev():
    return render_template("web_dev.html")

@app.route("/android_development")
def android_development():
    return render_template("android_development.html")

@app.route("/cyber_security")
def cyber_security():
    return render_template("cybersecurity_project.html")

@app.route("/cloud_dev")
def cloud_dev():
    return render_template("cloud_dev.html")


if __name__ == "__main__":
    app.run(debug=True)