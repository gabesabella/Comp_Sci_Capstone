from flask import Flask, request, render_template
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_curve, auc, roc_curve
from sklearn.metrics import classification_report, precision_score
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# pd.set_option('display.max_rows', None)
df = pd.read_csv('mushrooms.csv')  # data frame object
# 3 gives decent accuracy.

kc = df[['class', 'gill-color', 'population',
         'spore-print-color', 'stalk-root', 'bruises']]

labelEncoder = LabelEncoder()
for column in kc.columns:
    kc[column] = labelEncoder.fit_transform(kc[column])

X = kc.drop(['class'], axis=1)  # Only the class
Y = kc["class"]  # Class removed


# Data split in half
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, random_state=40, test_size=.5, train_size=.5)

rf = RandomForestClassifier(n_estimators=50, random_state=42)
rf.fit(X_train, Y_train)
preds = rf.predict(X_test)


print("Random Forest Preidtion Accuracy: {}%".format(
    round(rf.score(X_test, Y_test)*100, 2)))
predictions = rf.predict(X_test)
cr = classification_report(Y_test, predictions)
print(cr)


# # Version that stays nominal
# kcn = df[['class', 'odor', 'gill-color', 'gill-size', 'ring-type']]

# # Creates a data frame using user entered variables
# # This is what we want to plot


# def main(gc, pop, spc, bs, sr):
#     keys = kc.loc[
#         (kc['gill-color'] == gc) &
#         (kc['population'] == pop) &
#         (kc['spore-print-color'] == spc) &
#         (kc['bruises'] == bs) &
#         (kc['stalk-root'] == sr)
#     ]
#     return keys


# # Transforming data from nominal (e, p) to ordinal (0, 1)
# labelEncoder = LabelEncoder()
# for column in kc.columns:
#     kc[column] = labelEncoder.fit_transform(kc[column])


# def callAlg(df):
#     try:
#         # Removing class from form data
#         X1 = df.drop(['class'], axis=1)
#         Y1 = df["class"]
#         # X2 = df.drop(['class'], axis=1)

#         X1_train, X1_test, Y1_train, Y1_test = train_test_split(
#             X1, Y1, random_state=40, test_size=.5, train_size=.5)
#         rf = RandomForestClassifier(n_estimators=50, random_state=42)
#         rf.fit(X1_train, Y1_train)
#         accuracy = rf.score(X1_test, Y1_test)*100, 2
#         preds = list(rf.predict(X1_test))
#         predictions = int(len(preds))
#         message = "Prediction accuracy is {}%".format(
#             accuracy)+" over {}".format(predictions)
#         return message, predictions
#     except (TypeError, ValueError):
#         return 'Insufficient data'


# # def saveGraph(X1):
# #     count = X1.value_counts()
# #     plt.figure(figsize=(8,7))
# #     sns.barplot(count.index, count.values, alpha=0.8, palette="prism")
# #     plt.ylabel('Count', fontsize=12)
# #     plt.xlabel('Class', fontsize=12)
# #     plt.title('Number of poisonous/edible mushrooms')
# #     plt.savefig("static/img/value_counts.png", format='png', dpi=500)


# X = kc.drop(['class'], axis=1)  # Data set without class
# Y = kc["class"]  # Data set class only
# # Data split into four groups for training and testing
# X_train, X_test, Y_train, Y_test = train_test_split(
#     X, Y, random_state=40, test_size=.5, train_size=.5)
# # Random Forest Classifier Initiated
# rf = RandomForestClassifier(n_estimators=60, random_state=42)
# rf.fit(X_train, Y_train)  # Clqassifier fit with split data
# preds = rf.predict(X_test)  # Predictions
# # Prediction message
# print("Random Forest Prediction Accuracy Based On:\nGill-Color \nPopulation \nSpore-Print-Color\nStalk-Root\nBruising:\n{}%".format(
#     round(rf.score(X_test, Y_test)*100, 2))+" accuracy")
# @app.route('/')
# def create_figure(gillColor, population, sporePrintColor, bruises, stalkRoot):
#     fig = plt.figure()
#     ax = fig.add_axes
#     plt.ylabel('Count')
#     plt.xlabel('Characteristic')
#     characteristics = ['Gill Color', 'Population',
#                        'Spore Color', 'Bruises', 'Stalk Root']

#     gc = len(kc.loc[(kc['gill-color'] == gillColor)])
#     spc = len(kc.loc[(kc['spore-print-color'] == sporePrintColor)])
#     pop = len(kc.loc[(kc['population'] == population)])
#     bs = len(kc.loc[(kc['bruises'] == bruises)])
#     sr = len(kc.loc[(kc['stalk-root'] == stalkRoot)])

#     plt.bar(characteristics, [gc, spc, pop, bs, sr])
#     plt.ylim(0, 8000)
#     plt.title('Specimens with selected characteristics')
#     return fig

# X = kc.drop(['class'], axis=1)  # Only the class
# Y = kc["class"]  # Class removed

# # Data split in half
# X_train, X_test, Y_train, Y_test = train_test_split(
#     X, Y, random_state=40, test_size=.5, train_size=.5)

# rf = RandomForestClassifier(n_estimators=60, random_state=42)
# rf.fit(X_train, Y_train)
# preds = rf.predict(X_test)
# print("Test Accuracy: {}%".format(round(rf.score(X_test, Y_test)*100, 2)))
