from app import app
from flask import make_response, request

@app.route("/", methods = ["POST", "GET"])
def index():
    response = make_response("END connection ok")
    response.headers['Content-Type'] ="text/plain"
    return response


@app.route("/ussdres", methods = ["POST", "GET"])
def res():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    text = request.values.get("text", None)
    phone_number = request.values.get("phoneNumber", None)
    if text =="":
        response = "END hi welcome to your ussd application"
    # usrResponse = text.split("*")[0]

    # if text == ''
