from flask import Flask


app = Flask(__name__)
app.secret_key = '5up3r 53cr3t'

# controller
from application.controllers.index import * 
from application.controllers.handler import * 