import owi_maplin_robot_arm
from flask import Flask, Response


arm = owi_maplin_robot_arm.Arm()
app = Flask(__name__)


@app.route('/')
def flash():
    def inner():
        yield "starting</br>\n"
        arm.move(owi_maplin_robot_arm.LedOn)
        yield "completed\n"
    return Response(inner())


app.run(host="0.0.0.0")
