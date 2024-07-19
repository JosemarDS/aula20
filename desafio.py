import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def plot_data():
    #  ler CSV file
    data = pd.read_csv('dados.csv') #separar por ' , ' as colunas

    # Extrair data
    x = data['quantidade']
    y = data['vendas']

    # Criar a figura
    fig, grafico = plt.subplots()
    grafico.plot(x, y, marker='o', linestyle='-', color='b')

    # add as labels
    grafico.set_xlabel('x')
    grafico.set_ylabel('y')
    grafico.set_title('Vendas Anuais')

    # mostrar o grafico
    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# janela tkinter
janela = tk.Tk()
janela.title('Análise de Vendas')

# button
botao = tk.Button(janela, text='Exibir Gráfico', command=plot_data)
botao.pack(pady=20)

# loop tkinter
janela.mainloop()