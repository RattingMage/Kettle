from flask import Flask, request, render_template, redirect, url_for

from kettle import ElectricKettle

app = Flask(__name__)
kettle = ElectricKettle()


@app.route("/")
def index():
    context = {
        "water_level": kettle.water_level,
        "status": kettle.status,
        "temperature": kettle.temperature
    }
    return render_template("index.html", context=context)


@app.route('/set_water_level', methods=["POST"])
def set_water_level():
    water_level = request.get_json().get("water_level", 0)
    kettle.fill(float(water_level.replace(",", ".")))
    return redirect(url_for("index"))


@app.route("/switch_on")
def switch_on():
    kettle.switch_on()
    return redirect(url_for("index"))


@app.route("/switch_off")
def switch_off():
    kettle.switch_off()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
