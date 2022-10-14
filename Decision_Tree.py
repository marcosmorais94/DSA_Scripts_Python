#-----------------------------------------------------------------------------
# CURSO MACHINE LEARNING - CAP.09 RANDOM FOREST

#EXEMPLO 1 - MODELO COM ÍNDICE GINI E ENTROPIA

#%% - Importando Pacotes

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import pydot
import graphviz

#Primeiro criamos o modelo e depois exportamos ele em graphviz (linha 10)
# Só assim podemos visualizar o gráfico da árvore

#%% - Criando o dataset

instancias = [
    {'Melhor Amigo': False, 'Especie': 'Cachorro'},
    {'Melhor Amigo': True, 'Especie': 'Cachorro'},
    {'Melhor Amigo': True, 'Especie': 'Gato'},
    {'Melhor Amigo': True, 'Especie': 'Gato'},
    {'Melhor Amigo': False, 'Especie': 'Gato'},
    {'Melhor Amigo': True, 'Especie': 'Gato'},
    {'Melhor Amigo': True, 'Especie': 'Gato'},
    {'Melhor Amigo': False, 'Especie': 'Cachorro'},
    {'Melhor Amigo': True, 'Especie': 'Gato'},
    {'Melhor Amigo': False, 'Especie': 'Cachorro'},
    {'Melhor Amigo': False, 'Especie': 'Cachorro'},
    {'Melhor Amigo': False, 'Especie': 'Gato'},
    {'Melhor Amigo': True, 'Especie': 'Gato'},
    {'Melhor Amigo': True, 'Especie': 'Cachorro'},
]


#Transformando o dataset em DataFrame
df = pd.DataFrame(instancias)
df

#%% - Modelo de Machine Learning

#Dados de treino e teste
x_train = [[1] if a else [0] for a in df['Melhor Amigo']]
y_train = [1 if d == "Cachorro" else 0 for d in df['Especie']]
labels = ['Melhor Amigo']

print(x_train)
print(y_train)

#Modelo
modelo_v1 = DecisionTreeClassifier(max_depth= None,
                                   max_features= None,
                                   criterion='entropy',
                                   min_samples_leaf= 1,
                                   min_samples_split= 2)

#Apresentando dados ao Classificador
modelo_v1.fit(x_train, y_train)

#%% - Apresentando dados do Modelo v1

arquivo = 'C:/FCD/DSA/Python/tree_modelov1.dot' #arquivo para graph

export_graphviz(modelo_v1, out_file = arquivo, feature_names = labels)
with open(arquivo) as f:
    dot_graph = f.read()
graphviz.Source(dot_graph)

#%% EXEMPLO 2 - ÍNDICE GINI

#Modelo
modelo_v2 = DecisionTreeClassifier(max_depth= None,
                                   max_features= None,
                                   min_samples_leaf= 1,
                                   min_samples_split= 2)

#Apresentando dados ao Classificador
modelo_v2.fit(x_train, y_train)

#%% - Apresentando dados do Modelo v1

arquivo = 'C:/FCD/DSA/Python/tree_modelov2.dot' #arquivo para graph

export_graphviz(modelo_v1, out_file = arquivo, feature_names = labels)
with open(arquivo) as f:
    dot_graph = f.read()
graphviz.Source(dot_graph)

