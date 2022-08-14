
from sklearn import metrics, preprocessing, model_selection, datasets
import pandas as pd
from sklearn import neighbors
import matplotlib.pyplot as plt
import sklearn
from sklearn.neighbors import KNeighborsRegressor


X, y = sklearn.datasets.load_iris(
    return_X_y=True)

x_normilize = preprocessing.StandardScaler()
x_norm = x_normilize.fit_transform(X)

x_train, x_test, y_train, y_test = model_selection.train_test_split(
    x_norm, y, test_size=0.1, random_state=42, stratify=y)


# initialize the knn model with 3 n_neighbors
n = neighbors.KNeighborsClassifier(n_neighbors=3)
n.fit(x_train, y_train)

pred = n.predict(x_test)
print(metrics.accuracy_score(y_test, pred))


model = KNeighborsRegressor()
model.fit(X, y)
pred = model.predict(X)
plt.scatter(pred,y)
plt.show()
