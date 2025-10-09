import numpy as np
import plotly.express as px
from scipy.stats import linregress

titulo_do_grafico = input('Qual o nome do gráfico? \n')
eixo_x = input('Qual o nome do Eixo x? \n')
eixo_y = input('Qual o nome do Eixo y? \n')
x_dados = tuple(map(float, input('Digite os valores de x separados por espaço: ').split()))
y_dados = tuple(map(float, input('Digite os valores de y separados por espaço:').split()))
print('\n\n\n')

# Regressão linear
reg = linregress(x_dados, y_dados)

# Coeficientes
A = reg.slope        # Coeficiente angular
B = reg.intercept    # Coeficiente linear
A_erro = reg.stderr   # Incerteza no coef. angular
B_erro = reg.intercept_stderr  # Incerteza no coef. linear

legenda = f"Reta: y = ({A:.3f} ± {A_erro:.5f})x + ({B:.3f} ± {B_erro:.5f})"

#Reta ajustada
x_fit = np.linspace(min(x_dados), max(x_dados), 100)
y_fit = A * x_fit + B

# Gráfico com Plotly
fig = px.scatter(x=x_dados, y=y_dados, labels={'x':eixo_x, 'y':eixo_y}, title=titulo_do_grafico)
fig.update_traces(name="Dados experimentais", showlegend=True)
fig.add_scatter(x=x_fit, y=y_fit, mode='lines', name="Ajuste Linear (melhor reta)")
fig.add_annotation(
    x=1.0, # Posição X da anotação (em coordenadas de dados)
    y=75.0, # Posição Y da anotação (em coordenadas de dados)
    text = legenda, # Texto a ser exibido
    showarrow = False
)
fig.update_layout(
    title={
        'text': titulo_do_grafico,
        'x': 0.45,            # centraliza (0 = esq, 0.5 = centro, 1 = dir)
        'xanchor': 'center', # ancora no centro
        'y': 0.95,           # ajusta a altura do título (1 = topo)
        'yanchor': 'top'
    },
    title_font=dict(
        family="Arial Black",  # fonte
        size=24,               # tamanho da letra
        color="darkblue"       # cor
    )
)            
fig.show()
