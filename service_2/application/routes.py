from flask import Flask, request, jsonify
from application.models import Deck
from application import app, db
import random
from os import getenv


def random_int():
    int = random.randint(1, 52)
    return int


@app.route('/service_2', methods=['POST'])
def card_points():
    number = random_int()
    query = Deck.query.filter_by(id=number).first()
    point = query.Points
    return {'points':'{}'.format(point)}

def card():
    query = Deck.query.filter_by(id=number).fisrt()
    card = query.Description
    return {'card':'{}'.format(card)}
