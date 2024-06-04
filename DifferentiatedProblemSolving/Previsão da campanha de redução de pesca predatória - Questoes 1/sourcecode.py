import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Dados fornecidos
anos = np.array([0, 1, 2, 3])
populacao = np.array([1190, 1155, 1030, 1015])

# Definindo o modelo de função quadrática
def modelo(t, a, b, c):
    return a*t**2 + b*t + c

# Ajustando a curva
parametros, _ = curve_fit(modelo, anos, populacao)

# Extraindo os coeficientes a, b e c
a, b, c = parametros
print(f"Coeficientes ajustados: a = {a:.4f}, b = {b:.4f}, c = {c:.4f}")

# Função ajustada
def N(t):
    return a*t**2 + b*t + c

# Calculando a população em 5 anos
populacao_em_5_anos = N(5)
print(f"População estimada em 5 anos: {populacao_em_5_anos:.2f}")

# Verificando se há algum ano em que a população será zero
# Resolvendo a equação a*t^2 + b*t + c = 0
discriminante = b**2 - 4*a*c

if discriminante < 0:
    print("A função não estima que a população terá 0 indivíduos em nenhum ano.")
else:
    t1 = (-b + np.sqrt(discriminante)) / (2*a)
    t2 = (-b - np.sqrt(discriminante)) / (2*a)
    t_zero = [t for t in [t1, t2] if t >= 0]
    
    if t_zero:
        print(f"A função estima que a população terá 0 indivíduos no ano: {t_zero[0]:.2f}")
    else:
        print("A função não estima que a população terá 0 indivíduos em nenhum ano.")

# Gerando pontos para previsão futura (até 6 anos no futuro)
anos_futuros = np.arange(0, 30, 1)
populacao_futura = N(anos_futuros)

# Mostrando a população observada e prevista
print("\nPopulação observada e prevista:")
for ano, pop_real, pop_prev in zip(np.concatenate((anos, anos_futuros[4:])), np.concatenate((populacao, [None]*len(anos_futuros[4:]))), populacao_futura):
    print(f"Ano {ano}: População observada = {pop_real if pop_real is not None else 'N/A'}, População prevista = {pop_prev:.2f}")

# Plotando a curva ajustada, os pontos de dados observados e os pontos previstos
t_values = np.linspace(0, 29, 100)
N_values = N(t_values)

plt.scatter(anos, populacao, color='red', label='Dados observados')
plt.plot(t_values, N_values, label='Curva ajustada')
plt.scatter(anos_futuros, populacao_futura, color='blue', marker='x', label='Previsões futuras')
plt.xlabel('Anos')
plt.ylabel('População')
plt.title('Ajuste de Curva Quadrática para População')
plt.legend()
plt.grid(True)
plt.show()
