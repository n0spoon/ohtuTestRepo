# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger('aloitetaan ohjelma')

x = int(input('luku1: '))
y = int(input('luku2: '))
print(f'{x} + {y} = {summa(x, y)}') # muutos masterissa
print(f'{x} - {y} = {erotus(x, y)}') # muutos masterissa

logger('lopetetaan ohjelma')
print('goodbye!')
