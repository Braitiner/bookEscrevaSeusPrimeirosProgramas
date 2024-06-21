#versao 1
# salario = int(input("Salario: "))
# imposto = input("imposto em %: ")
# if imposto == "":
#     imposto = 27.5
# else:
#     imposto = float(imposto)
# print("Valor real {0}".format(salario - (salario * (imposto * 0.01))))

# versao 2
# salario = int(input("Salario: "))
# imposto = input("imposto em %: ")
# if not imposto:
#     imposto = 27.5
# else:
#     imposto = float(imposto)
# if imposto < 10:
#     print("baixo")
# elif imposto >= 10. and imposto < 27.5:
#     print('medio')
# elif imposto >= 27.5 and imposto <= 100:
#     print('alto')
# else:
#     print('valor invalido')
# print("Valor real {0}".format(salario - (salario * (imposto * 0.01))))

# versao 3
# salario = int(input("Salario"))
# imposto = 27.5
# while imposto > 0:
#     imposto = input("imposto ou [s] para sair: ")
#     if not imposto:
#         imposto = 27.5
#     elif imposto == "s":
#         break
#     else:
#         imposto = float(imposto)
#     print("Valor real: {}".format(salario - (salario * (imposto * 0.01))))


def sum(a, b):
    return a + b

c = sum(1, 3)
print(c)


# versao 4
def salario_descontado_imposto(salario, imposto=27.):
    return salario - (salario * (imposto * 0.01))

print(salario_descontado_imposto(5000))



# funções com packing:
from datetime import date
d = (2013, 3, 15)
date(d[0], d[1], d[2])

from datetime import date
d = (2013, 3, 15)
date(*d)

def new_user(active=False, admin=False):
    print(active)
    print(admin)

config = {"active": False, "admin": True}

new_user(config.get('active'), config.get('admin'))

new_user(**config)




# funcçoes com unpacking:

def unpacking_experiment(*args):
    arg1 = args[0]
    arg2 = args[1]
    others = args[2:]
    print(arg1)
    print(arg2)
    print(others)

unpacking_experiment(1, 2, 3, 4, 5, 666)

def unpacking_experiment(**kwargs):
    print(kwargs)

unpacking_experiment(named="test", other="ither")

import math
# math = 10
print(math.sqrt(9))

import math as funcoes_matematicas
print(funcoes_matematicas.sqrt(9))

from unittest import TestCase
from unittest import mock

from math import sqrt as pontencia
print(pontencia(9))