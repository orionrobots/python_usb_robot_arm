import usb_arm
from flask import Flask, Response, request, render_template


arm = usb_arm.Arm()
app = Flask(__name__)

movemap = {
    "GripsClose": usb_arm.GripsClose,
    "CloseGrips": usb_arm.CloseGrips,
    "GripsOpen": usb_arm.GripsOpen,
    "OpenGrips": usb_arm.OpenGrips,
    "Stop": usb_arm.Stop,
    "WristUp": usb_arm.WristUp,
    "WristDown": usb_arm.WristDown,
    "ElbowUp": usb_arm.ElbowUp,
    "ElbowDown": usb_arm.ElbowDown,
    "ShoulderUp": usb_arm.ShoulderUp,
    "ShoulderDown": usb_arm.ShoulderDown,
    "BaseClockWise": usb_arm.BaseClockWise,
    "BaseCtrClockWise": usb_arm.BaseCtrClockWise,
    "LedOn": usb_arm.LedOn
}


@app.route('/')
def index():
    return render_template('index.html', patterns=movemap)


@app.route('/move', methods=['POST'])
def move():
    pattern = movemap[request.form['pattern']]

    def inner():
        yield "starting<br>\n"
        arm.move(pattern)
        yield "completed\n"
    return Response(inner())


app.run(host="0.0.0.0")
