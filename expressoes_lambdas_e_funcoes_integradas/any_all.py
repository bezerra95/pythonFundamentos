"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o interável está vazio.
"""

# Exemplo all()
"""
print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False

print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros? True

print(all([]))  # Todos os números são verdadeiros? True

print(all((0, 1, 2, 3, 4)))  # Todos os números são verdadeiros? True

print(all({0, 1, 2, 3, 4}))  # Todos os números são verdadeiros? True

print(all('Geek'))

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))
"""
# OBS: Um iterável vazio convertido em boolean é False, mas o all() entende como True
"""
print(all([letra for letra in 'eiof' if letra in 'aeiou']))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

any -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""

print(any([0, 1, 2, 3, 4]))  # True

print(any([0, False, {}, (), []]))  # False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristiana', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))  # True

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))  # True

