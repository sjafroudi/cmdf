from flask import Flask, render_template
import cv2

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello"

    