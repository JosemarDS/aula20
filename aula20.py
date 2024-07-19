from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

numero = [[2],[4],[6],[3],[5],[1],[7],[8]]
etiquetas = [0,0,0,0,1,1,1,1]

X_train, x_test, y_train, y_test = train_test_split(numero, etiquetas, test_size=0.5)

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X_train, y_train)

result = modelo.predict(x_test)
print(result)
print(y_test)

# Machine learning
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier


# # 0 par 1 impar 
# numero = [[2],[4],[6],[3],[5],[1],[7],[8]]
# etiquetas = [0,0,0,0,1,1,1,1]

# # variáveis 
# X_train, x_test, y_train, y_test =  train_test_split(numero, etiquetas,test_size=0.5)

# # criar o modelo
# modelo = KNeighborsClassifier(n_neighbors=3)

# # Treinar o modelo
# modelo.fit(X_train, y_train)

# # resultado 
# result = modelo.predict(x_test)
# print(result)
# print(y_test)