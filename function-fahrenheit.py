#Início da função de calculo de conversão ºF para ºC
def fahr(temp):
    temp_conv = float(temp)    
    calc_temp = (temp_conv - 32) // 1.8
    return calc_temp

#Armazenamento do valor digitado dentro da variável "temp_fahr"
temp_fahr = input('Digite a temperatura em ºF: ')

#Chamada da função
res_temp = fahr(temp_fahr)

#Mostrar na tela os resultado
print('ºF = ', temp_fahr , 'ºC = ', res_temp)