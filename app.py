
from flask import Flask, request, render_template

from classify import main, classify


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        gc = request.form.get("gc")
        pop = request.form.get("pop")
        spc = request.form.get("spc")
        bs = request.form.get("bs")
        sr = request.form.get("sr")
        gillColor = int(gc)
        population = int(pop)
        sporePrintColor = int(spc)
        bruises = int(bs)
        stalkRoot = int(sr)
        userSelection = main(gillColor, population,
                             sporePrintColor, bruises, stalkRoot)
        message = classify(userSelection)
        return message
    return render_template("gfg.html")


if __name__ == '__main__':
    app.run()
