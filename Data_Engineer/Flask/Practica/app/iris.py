# MOdelo de ML KNN con los datos de Iris sin gridsearch

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle

iris = load_iris()

print(iris.keys())

print(iris)

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=23)

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train,y_train)

prediction = knn.predict(X_test)
print(prediction)

knn.score(X_train, y_train)

with open('Data_Engineer\Flask\Practica\modelo.pkl', 'wb') as archivo:
    pickle.dump(knn, archivo)