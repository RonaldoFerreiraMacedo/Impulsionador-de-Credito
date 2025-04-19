import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# DataFrame
data = {
    'Nome': ['Alice', 'Joao', 'Charlie', 'David', 'Eva', 'Diego', 'Denize', 'Claudio'],
    'Idade': [25, 30, 35, 40, 45, 60, 22, 24],
    'Profissão': ['Engenheiro', 'Médico', 'Professor', 'Advogado', 'Médico', 'Engenheiro', 'Estudante', 'Estudante'],
    'Salário': ['4500', '8000', '5000', '10000', '12000', '15000', '1200', '1500'],
    'Limite_Credito': ['2500', '4000', '4000', '1000', '10000', '2000', '500', '250'],
    'Historico_Inadimplencia': ['0', '0', '0', '1', '0', '1', '0', '1'],
    'Estado_Civil': ['Casamento', 'Casamento', 'Solteiro', 'Solteiro', 'Casamento', 'Solteiro', 'Solteiro', 'Solteiro'],
    'Imovel_Proprio': ['0', '0', '0', '1', '1', '1', '0', '0']
}

df = pd.DataFrame(data)
print(df.to_string())

# Convertendo para números
df['Salário'] = df['Salário'].astype(int)
df['Limite_Credito'] = df['Limite_Credito'].astype(int)
df['Historico_Inadimplencia'] = df['Historico_Inadimplencia'].astype(int)
df['Imovel_Proprio'] = df['Imovel_Proprio'].astype(int)

# Ordenando pelo Limite de Credito
df = df.sort_values(by='Limite_Credito')

# Eixo X e largura das barras
x = np.arange(len(df))
largura = 0.35

# Plotando o gráfico de Barras Salário x Limite de Crédito
plt.figure(figsize=(10, 6))
plt.bar(x - largura / 2, df['Salário'], width=largura, label='Salário', color='skyblue')
plt.bar(x + largura / 2, df['Limite_Credito'], width=largura, label='Limite de Crédito', color='orange')

plt.xticks(x, df['Nome'], rotation=45)
plt.xlabel('Pessoa')
plt.ylabel('R$')
plt.title('Salário x Crédito')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Grafico de Barras Limite de Credito X Historico de inadimplencia
fig, ax1 = plt.subplots(figsize=(10, 6))

# Eixo Principal: Salario
ax1.bar(x - largura / 2, df['Limite_Credito'], width=largura, label='Credito', color='green')
ax1.set_ylabel('Limite de Crédito (R$)')
ax1.set_xticks(x)
ax1.set_xticklabels(df['Nome'], rotation=45)

# Eixo secundario: Historico de inadimplencia
ax2 = ax1.twinx()
ax2.bar(x + largura / 2, df['Historico_Inadimplencia'], width=largura, label='Inadimplência', color='purple')
ax2.set_ylabel('Inadimplência (0 ou 1)')
ax2.set_ylim(0, 1.5)

# Titulo e legendas
plt.title('Crédito vs Inadimplência')
fig.legend(loc='upper right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()

# Grafico de barras e linhas
fig, ax1 = plt.subplots(figsize=(10, 6))
df = df.sort_values(by='Limite_Credito').reset_index(drop=True)
credito_ordenado = df['Limite_Credito']

# Criando Eixo x: Idade
ax1.plot(credito_ordenado.index, df['Idade'], marker='o', color='red', label='Idade')
ax1.set_xlabel('Pessoas', fontsize=12)
ax1.set_ylabel('Idade', color='red', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(df['Nome'], rotation=45)

# Criando o segundo Eixo X: Limite de Credito
ax2 = ax1.twinx()
ax2.bar(credito_ordenado.index, df['Limite_Credito'], color='blue', alpha=0.5, label='Crédito')
ax2.set_ylabel('Limite de Credito', color='blue', fontsize=12)

plt.title('Crédito x Idade')
plt.grid(axis='y', linestyle='--', alpha=0.5)
fig.legend(loc='upper right')
plt.show()
