"""
Modulo colletions - Default Dict

# Recap Dicionarios

dicionario = {'curso':'programaçao em python: essencial'}

print(dicionario)

print(dicionario['curso'])
print(dicionario['outro']) # keyerror

"""

# fazendo o import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'programaçao em python essencial'

print(dicionario['outro'])

print(dicionario)










