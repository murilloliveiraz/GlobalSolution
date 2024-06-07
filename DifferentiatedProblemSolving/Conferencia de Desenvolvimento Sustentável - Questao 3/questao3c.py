import sympy as sp

# Definindo as variáveis
p = sp.symbols('p')

# Receita desejada
R_desejada = 50000

# Equação da receita
equacao_receita = p * (1000 - 4 * p) - R_desejada

# Resolver a equação para encontrar o preço
solucoes = sp.solve(equacao_receita, p)

# Filtrar as soluções reais e positivas
preco_correto = [sol for sol in solucoes if sol.is_real and sol > 0]

# Exibir o preço correto
print(f"O preço correto para obter uma receita de R$ 50.000,00 é: R$ {preco_correto[0]:.2f}")