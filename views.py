from flask import Flask, request, render_template, flash, redirect, url_for, session, jsonify
import hashlib, uuid, os
import database
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from werkzeug.utils import secure_filename
import webbrowser
import time


app = Flask(__name__)
connection = database.create_connection()
cursor = connection.cursor()

app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_key'
)

@app.route('/')
def index():
    
    return render_template("index.html")


@app.route('/street')
def street():
	return render_template("street.html")  

if __name__ == "__main__":
    app.run(host='localhost', debug=True)   


