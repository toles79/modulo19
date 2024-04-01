
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
dados_gasolina = pd.read_csv('gasolina.csv')

# Gerar gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(data=dados_gasolina, x='dia', y='venda')
plt.title('Preço Médio da Gasolina em São Paulo - Julho 2021')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.savefig('gasolina.png')
plt.show()
