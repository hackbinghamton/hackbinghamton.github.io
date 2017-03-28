#pip install scipy sklearn
from sklearn.tree import DecisionTreeClassifier

# The first entry is the weight of the fruit in grams,
# the second entry is 0 -> smooth, 1 -> bummpy

features = [[140, 0], [130, 0], [150, 1], [170, 1]]

# 0 -> apple, 1-> orange
labels   = [0, 0, 1, 1]

# Create a classifier
classifier = DecisionTreeClassifier()

classifier.fit(features, labels)

prediction = classifier.predict([[160, 1]])

if prediction == 0:
    print("Apple")

# predicition == 1
else:
    print("Orange")

