# Módulos padrão do Python (import, from, as e *)
# Link para a documentação oficial: https://docs.python.org/3/py-modindex.html

# Importação inteira - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

import sys  # Importa todo o módulo sys

platform = 'A MINHA'  # Define uma variável local chamada platform
print(sys.platform)  # Acessa a variável platform do módulo sys
print(platform)  # Acessa a variável local platform
"""A vantagem aqui é que o namespace do módulo sys é mantido, evitando conflitos com a variável local."""

# Importação de partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

from sys import exit, platform  # Importa apenas exit e platform do módulo sys

print(platform)  # Acessa a variável platform importada do módulo sys
"""A desvantagem é que perdemos o namespace do módulo sys, o que pode causar conflitos de nome."""

# Alias para o módulo inteiro - import nome_modulo as apelido
import sys as s  # Importa todo o módulo sys com o apelido s

sys = 'alguma coisa'  # Define uma variável local chamada sys
print(s.platform)  # Acessa a variável platform do módulo sys (agora chamado s)
print(sys)  # Acessa a variável local sys
"""Usar alias permite evitar conflitos de nome e manter os nomes curtos."""

# Alias para partes do módulo - from nome_modulo import objeto as apelido
from sys import exit as ex  # Importa exit do módulo sys com o apelido ex
from sys import platform as pf  # Importa platform do módulo sys com o apelido pf

print(pf)  # Acessa a variável platform do módulo sys (agora chamado pf)
"""Usar alias para partes do módulo também ajuda a evitar conflitos de nome e a manter os nomes curtos."""

# Má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

from sys import *  # Importa tudo do módulo sys

print(platform)  # Acessa a variável platform importada do módulo sys
exit()  # Chama a função exit importada do módulo sys
"""Importar tudo de um módulo é uma má prática porque pode causar conflitos de nome e poluir o namespace global."""
