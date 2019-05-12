from sklearn import tree
features = [[140], [130], [150], [170]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
prediction = clf.predict([[150]])
print(prediction)