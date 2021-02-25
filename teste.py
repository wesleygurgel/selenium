from datetime import datetime
import time

# atual = datetime.now()
# atual_texto = atual.strftime('%H:%M')
# hora = atual_texto[0:2]
# minuto = atual_texto[3:]
#
# if int(hora) == 7:
#     if int(minuto) < 20:
#
#
#     print('sou maior ou igual a 7')
#
# if int(minuto) >= 20:
#     print('sou maior igual a 20')

formato = '%H:%M'
atual = datetime.now()
atual = atual.strftime('%H:%M')
horario_esperado = '07:20'

data1 = datetime.strptime(atual, formato)
data2 = datetime.strptime(horario_esperado, formato)

diff = data1 - data2
diff_minutes = (diff.days * 24 * 60) + (diff.seconds/60)
print(f'{diff_minutes * 60} seconds')
print(diff_minutes)

