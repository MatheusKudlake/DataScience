import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0,1

dados = np.random.normal(mu, sigma, 1000)
print(dados)

plt.figure(figsize = (8,6))
plt.hist(dados, bins = 30, density = True, alpha = 0.6, color = 'blue')
plt.title('Histograma de dados')
plt.xlabel('valor')
plt.ylabel('probabilidade')
plt.grid(True)
plt.show()

plt.figure(figsize=(8,6))
plt.hist(dados, bins = 30, density = True, alpha = 0.6, color = 'green')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
n = ((1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu)*2) / (2 * sigma*2)))
plt.plot(x,n,'k', linewidth = 2)
plt.show()

title = "Histograma de uma Distribuição"
plt.title(title)
plt.xlabel("Valores")
plt.ylabel("Densidade de probabilidade")