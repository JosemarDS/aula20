import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import requests

dados = pd.read_csv('dados.csv')
# print(dados)
# x = dados['quantidade']
# y = dados['vendas']

# plt.bar(x, y)
# plt.show()


plt.style.use('_mpl-gallery')

# make data:
x = dados['quantidade']
y = dados['vendas']

# plot
fig, ax = plt.subplots()

ax.bar(x, y) # width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()


