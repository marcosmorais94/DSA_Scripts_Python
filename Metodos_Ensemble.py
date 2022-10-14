#%% - MÉTODOS ENSEMBLE - CURSO MACHINE LEARNING

#Método Bagging

#%% - Importando Pacotes

from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn.model_selection import cross_val_score
import warnings 
warnings.simplefilter(action = 'ignore', category=FutureWarning)

#%% - Carga dos dados

digits = load_digits()

#%% - Plot dados
plt.gray()
plt.matshow(digits.images[5])
plt.show()

#%% - Pré-Processamento

data = scale(digits.data) #Coloca os dados na mesma escala

x = data #variável preditora
y = digits.target #variável target

#%% - Classificador

bagging = BaggingClassifier(KNeighborsClassifier(), max_samples= 0.5, max_features=0.5)

bagging

#%% - Score Modelo
scores = cross_val_score(bagging, x, y)

mean = scores.mean()

print(scores)
print(mean)


#%% - Método Extremely Random Forest

# É um conjunto de árvores aleatórias cricadas pelo algoritmo

#%% - Carregando Pacotes

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_digits
from sklearn.preprocessing import scale
from sklearn.model_selection import cross_val_score

#%% Carga e Pré-Processamento dos Dados

digits = load_digits()
data = scale(digits.data)

x = data
y = digits.target

#%% - Classificador com Árvore de Decisão

clf = DecisionTreeClassifier(max_depth = None, min_samples_split = 2, random_state = 0)
scores = cross_val_score(clf, x, y)
mean = scores.mean()
print(scores)
print(mean)

#%% - Classficiador com Random Forest

clf = RandomForestClassifier(n_estimators = 10, max_depth = None, min_samples_split = 2, random_state = 0)
scores = cross_val_score(clf, x, y)
mean = scores.mean()
print(scores)
print(mean)

#%% - Classificador com Extra Tree
clf = ExtraTreesClassifier(n_estimators = 10, max_depth = None, min_samples_split = 2, random_state = 0)
scores = cross_val_score(clf, x, y)
mean = scores.mean()
print(scores)
print(mean)


#%% - USO DO ADABOOST

#Pacotes

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import fetch_openml
from sklearn.model_selection import cross_val_score

#%% Carga dos dados

heart = fetch_openml('heart')

x = heart.data
y = np.copy(heart.target)
y[y == -1] = 0

#%% - Dados de Treino e Teste

x_test, y_test = x[189:], y[189:]
x_train, y_train = x[:189], y[:189]

#%% - Estimador Base

estim_base = DecisionTreeClassifier(max_depth=1, min_samples_leaf=1)

#%% - V1 do Modelo AdaBoost

ada_clf_v1 = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=1, min_samples_leaf=1),
                                learning_rate= 0.1,
                                n_estimators=400,
                                algorithm='SAMME')
#%% - Treino Modelo

ada_clf_v1.fit(x_train, y_train)

#%% - Score do Modelo

scores = cross_val_score(ada_clf_v1, x_test, y_test)
print(scores)

means = scores.mean()
print(means)

