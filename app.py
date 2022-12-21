import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request, render_template

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
    return render_template("form.html")


if __name__ == '__main__':
    app.run()


df = pd.read_csv('mushrooms.csv')  # data frame object

# Key characteristics
kc = df[['class', 'gill-color', 'population',
         'spore-print-color', 'stalk-root', 'bruises']]
# Main function that takes user-selected params

# Version that stays nominal
kcn = df[['class', 'gill-color', 'population',
         'spore-print-color', 'stalk-root', 'bruises']]


def main(gc, pop, spc, bs, sr):
    keys = kc.loc[
        (kc['gill-color'] == gc) &
        (kc['population'] == pop) &
        (kc['spore-print-color'] == spc) &
        (kc['bruises'] == bs) &
        (kc['stalk-root'] == sr)
    ]
    return keys


# Transforming data from nominal (e, p) to ordinal (0, 1)
labelEncoder = LabelEncoder()
for column in kc.columns:
    kc[column] = labelEncoder.fit_transform(kc[column])


def classify(userSelection):
    try:
        # Removing class from user-selected data frame
        X = userSelection.drop(['class'], axis=1)
        Y = userSelection["class"]

        # Setting up train / test data
        X_train, X_test, Y_train, Y_test = train_test_split(
            X, Y, random_state=40, test_size=.5, train_size=.5)
        rf = RandomForestClassifier(n_estimators=50, random_state=42)
        rf.fit(X_train, Y_train)
        # Accuracy score
        accuracy = round(rf.score(X_test, Y_test)*100, 2)
        preds = list(rf.predict(X_test))
        if preds[0] == 1:
            predictedClass = 'Poisonous! '
        else:
            predictedClass = 'Edible! '
        predictions = int(len(preds))

        message = "Predicted class: {}".format(predictedClass) + "Prediction accuracy was {}%".format(
            accuracy)+" correct for {}".format(predictions)+" specimens."
        if predictions > 0:
            return message
        else:
            return 'Insufficient data'
    except ValueError:
        return 'There are no matching specimens with these selected attributes. Try a different combination of attributes.'
