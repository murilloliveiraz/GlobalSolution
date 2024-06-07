import matplotlib.pyplot as plt

# Definindo os dados iniciais
dados_iniciais = 10  # em TB
crescimento_mensal = 0.03  # 3% ao mês
capacidade_disco = 50  # em TB

# Calculando a quantidade de dados consumida em 1 ano
dados_ano = dados_iniciais * (1 + crescimento_mensal) ** 12

# Calculando quanto tempo a aplicação ainda poderá rodar no disco rígido atual
meses_restantes = (capacidade_disco - dados_iniciais) / (dados_iniciais * crescimento_mensal)

# Criando os dados para o gráfico e exibindo os valores no console
meses = range(55)  # 1 ano (12 meses) + 1 mês adicional para o cálculo
quantidade_dados = []
for i in meses:
    dados_mes = dados_iniciais * (1 + crescimento_mensal) ** i
    quantidade_dados.append(dados_mes)
    print(f'Mês {i}: {dados_mes:.2f} TB')

# Plotando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(meses, quantidade_dados, marker='o', linestyle='-', color='b')
plt.axhline(y=capacidade_disco, color='r', linestyle='--', label='Capacidade do Disco')
plt.title('Crescimento dos Dados de Escaneamento 3D de Oceanos')
plt.xlabel('Meses')
plt.ylabel('Quantidade de Dados (TB)')
plt.legend()
plt.grid(True)
plt.show()
