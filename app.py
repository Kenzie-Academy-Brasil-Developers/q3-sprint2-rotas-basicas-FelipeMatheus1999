from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get():
    return {"data": "Hello Flask!"}

@app.route("/current_datetime", methods=["GET"])
def current_datetime():
    date = int(datetime.now().strftime("%H"))
    current_datetime = datetime.now().strftime("%H/%m/%Y %X %p")
    message = ""

    if date >= 6 and date < 12:
        message = "Bom dia!"
    
    elif date >= 12 and date < 18:
        message = "Boa tarde!"
    
    else:
        message = "Boa noite!"
    
    return {"current_datetime": current_datetime, "message": message}
