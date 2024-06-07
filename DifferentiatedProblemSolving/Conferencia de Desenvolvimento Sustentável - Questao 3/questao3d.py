import sympy as sp

# Definindo a variável simbólica para o preço
p = sp.symbols('p')

# Definindo a função da receita R = p * (1000 - 4p)
R = p * (1000 - 4 * p)

# Calculando a derivada da função de receita em relação ao preço
derivada_R = sp.diff(R, p)

# Resolvendo a equação da derivada igual a zero para encontrar o preço que maximiza a receita
preco_maximo = sp.solve(derivada_R, p)

# Filtrando a solução positiva e real
preco_maximo = [sol for sol in preco_maximo if sol.is_real and sol > 0]

# Calculando a receita máxima correspondente ao preço encontrado
receita_maxima = R.subs(p, preco_maximo[0])

print(f"O preço que maximiza a receita é: R$ {preco_maximo[0]:.2f}")
print(f"A receita máxima correspondente é: R$ {receita_maxima:.2f}")
