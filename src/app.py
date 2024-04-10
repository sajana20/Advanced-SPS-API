from flask import Flask, request
from src.repositories.parking_area_repository import ParkingAreaRepository
from src.repositories.user_repo import UserRepository
from src.repositories.user_token_repo import UserTokenRepository
from src.repositories.user_reservation_repo import UserReservationRepository
from src.push_notification import Notification
from src.repositories.footage_repo import FootageRepository
import json

app = Flask(__name__)

@app.route("/login", methods=['post'])
def login():
    email = request.form["email"]
    password = request.form['password']
    return UserRepository().get_user_details(email, password)


@app.route("/signup", methods=['post'])
def signup():
    user_name = request.form["user_name"]
    email = request.form['email']
    password = request.form['password']
    return UserRepository().set_user_details(user_name, email, password)


@app.route("/logout/<user_id>", methods=['post'])
def logout(user_id):
    return UserTokenRepository().delete_user_token(user_id)


@app.route("/availability")
def get_availability():
    response = ParkingAreaRepository().get_parking_availability()
    return response


@app.route("/availability", methods=['post'])
def set_availability():
    user_id = request.form["user_id"]
    slot_id = request.form["slot_id"]
    availability = request.form['availability']
    active = 1 if availability == '0' else 0

    ParkingAreaRepository().update_parking_availability(user_id, slot_id, availability)
    if (user_id == '0'):
        UserReservationRepository().update_active_status(active, slot_id)
    else:
        UserReservationRepository().update_user_reservation(user_id, slot_id, active)
    return json.dumps({"status": "Success"})


@app.route("/checkAvailability/<slot_id>")
def checkAvailabilityBySlotId(slot_id):
    response = ParkingAreaRepository().checkAvailability(slot_id)
    return response


@app.route("/footage", methods=['post'])
def set_footage():
    slot_id = request.form["slot_id"]
    file_name = request.form['file_name']
    FootageRepository().set_footage(slot_id, file_name)
    return json.dumps({"status": "Success"})


@app.route("/pushNotification", methods=['post'])
def send_pushNotification():
    slot_id = request.form["slot_id"]
    title = request.form["title"]
    message = request.form["message"]
    token = UserTokenRepository().get_user_token(slot_id)
    response = Notification().send_push_notification(token, title, message)
    return response


@app.route("/fcmToken", methods=['post'])
def save_token():
    user_id = request.form["user_id"]
    token = request.form["token"]
    response = UserTokenRepository().set_user_token(user_id, token)
    return response


@app.route("/reservations/<user_id>")
def getReservationsByUserId(user_id):
    response = UserReservationRepository().get_user_reservation(user_id)
    return response


@app.route("/footageFileName/<reservation_id>")
def getfootagefileName(reservation_id):
    response = FootageRepository().get_footage_file_name(reservation_id)
    return response


app.run()
