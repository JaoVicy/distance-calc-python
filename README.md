# Distance-Calc-Python 📍

Projeto para cálculo de distâncias geodésicas entre pontos geográficos usando Python. Todo o projeto está preparado para execução em um container Docker.

## Descrição 📚

Este projeto realiza cálculos da menor distância entre dois ou mais pontos na superfície da Terra (distância geodésica), utilizando a biblioteca [geopy](https://geopy.readthedocs.io/). As classes principais são:

- **GeoPoint:** Armazena latitude e longitude de um ponto.
- **DistanceCalculator:** Permite adicionar vários pontos e calcular distâncias entre eles, usando a função geodesic do geopy.

## Funcionalidades ✨

- Armazenamento de múltiplos pontos geográficos (latitude e longitude)
- Cálculo da distância em quilômetros entre pontos usando a curvatura real da Terra
- Execução facilitada via Docker

## Exemplo de Uso 🎯

```python
from defs.GeoPoint import GeoPoint
from defs.DistanceCalculator import DistanceCalculator

# Criando pontos
ponto1 = GeoPoint(-23.5505, -46.6333)  # São Paulo
ponto2 = GeoPoint(-22.9068, -43.1729)  # Rio de Janeiro

# Instanciando o calculador e adicionando pontos
calc = DistanceCalculator()
calc.add_point(ponto1)
calc.add_point(ponto2)

# Definindo um ponto de referência
referencia = GeoPoint(-15.8267, -47.9218)  # Brasília
distancias = calc.calculate_distances(referencia)
print(distancias)  # Exemplo de saída: [873.1, 934.6]
