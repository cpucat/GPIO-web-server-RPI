from flask import Flask, render_template, make_response
import RPi.GPIO as GPIO
from itertools import cycle
app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pin1 = 11
pin2 = 15
pin3 = 40
pin4 = 35
pin5 = 18
pin6 = 13

sts1 = 0
sts2 = 0
sts3 = 0
sts4 = 0
sts5 = 0
sts6 = 0

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)
GPIO.setup(pin5, GPIO.OUT)
GPIO.setup(pin6, GPIO.OUT)

GPIO.output(pin1, GPIO.LOW)
GPIO.output(pin2, GPIO.LOW)
GPIO.output(pin3, GPIO.LOW)
GPIO.output(pin4, GPIO.LOW)
GPIO.output(pin5, GPIO.LOW)
GPIO.output(pin6, GPIO.LOW)



@app.route('/')
def index():
    return render_template('index.html', IP='INSERT YOUR IP')

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'pin1':
        actuator = pin1
    if deviceName == 'pin2':
        actuator = pin2
    if deviceName == 'pin3':
        actuator = pin3
    if deviceName == 'pin4':
        actuator = pin4
    if deviceName == 'pin5':
        actuator = pin5
    if deviceName == 'pin6':
        actuator = pin6
        
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)
        
    return render_template('index.html, IP='INSERT YOUR IP'')
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')