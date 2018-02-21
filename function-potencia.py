def potencia(base, expoente):
    b = float(base)
    exp = float(expoente)
    
    resposta = b**exp
    return resposta

str_b = input('Digite a base: ')
str_exp = input ('Digite o expoente: ')

res = potencia(str_b, str_exp)

print('o resultado da potência é: ', res)
