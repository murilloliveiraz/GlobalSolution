# Cálculo em Python
preco_inicial = 50
vendas_iniciais = 800
preco_desejado = 115

# Diferença de preço
diferenca_preco = preco_desejado - preco_inicial

# Redução nas vendas
reducoes = diferenca_preco // 5
vendas_perdidas = reducoes * 20

# Quantidade final de vendas
vendas_finais = vendas_iniciais - vendas_perdidas

# Receita final
receita_final = vendas_finais * preco_desejado

print(f"A quantidade de ingressos vendidos a um preço de R$ {preco_desejado:.2f} será: {vendas_finais}")
print(f"A receita total será: R$ {receita_final:.2f}")