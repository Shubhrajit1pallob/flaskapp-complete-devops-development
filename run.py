from app.routes import app

if __name__ == "__main__":
    app.run(debug=False, port=8888, host='0.0.0.0')