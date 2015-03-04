# total = 0
#
# valor1 = 10
# valor2 = 20
#
def soma(x, y):
    total = x + y
    return total

def mult(x, y):
    total = x * y
    return total

def divisao(x, y):
    total = round(float(x) / float(y), 2)
    return total

def subtracao(x, y):
    total = x - y
    return total


x = input('What is first value?')
y = input('What is the second value?')
z = input('What is the operation?')

if(z == 1):
   total = soma(x, y)
   operacao = "soma"
elif(z == 2):
   total = mult(x, y)
   operacao = "mult"
elif(z == 3):
    total = divisao(x, y)
    operacao = "divisao"
else:
    total = subtracao(x, y)
    operacao = "subtracao"

print('A {} de {} e {} = {}'.format(operacao, x, y, total))

#
# total_conta = 0
# total_soma = valor1 + valor2
#
# total_conta = soma(total_soma)
#
# total_conta = divisao(total_conta, valor1)
#
# total_conta = mult(subtracao(valor1, total_conta), -1)
#
#
# print total_conta




