import owi_maplin_robot_arm
from flask import Flask, Response, request, render_template


arm = owi_maplin_robot_arm.Arm()
app = Flask(__name__)

movemap = {
    "GripsClose": owi_maplin_robot_arm.GripsClose,
    "CloseGrips": owi_maplin_robot_arm.CloseGrips,
    "GripsOpen": owi_maplin_robot_arm.GripsOpen,
    "OpenGrips": owi_maplin_robot_arm.OpenGrips,
    "Stop": owi_maplin_robot_arm.Stop,
    "WristUp": owi_maplin_robot_arm.WristUp,
    "WristDown": owi_maplin_robot_arm.WristDown,
    "ElbowUp": owi_maplin_robot_arm.ElbowUp,
    "ElbowDown": owi_maplin_robot_arm.ElbowDown,
    "ShoulderUp": owi_maplin_robot_arm.ShoulderUp,
    "ShoulderDown": owi_maplin_robot_arm.ShoulderDown,
    "BaseClockWise": owi_maplin_robot_arm.BaseClockWise,
    "BaseCtrClockWise": owi_maplin_robot_arm.BaseCtrClockWise,
    "LedOn": owi_maplin_robot_arm.LedOn
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
