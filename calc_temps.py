ini = input('Digite um número para escolher uma das opções \nºF = 1 \nºC = 2 \nºK = 3 \n\n')
ini_conv = float(ini)

if ini_conv == 1:
    temp = input('Digite a temperatura em ºF:\n')
    temp = float(temp)    
    calc_f = (temp - 32) // 1.8
    print(calc_f)
    
elif ini_conv == 2:
    temp = input('Digite a temperatura em ºC:\n')
    
elif ini_conv == 3:
    temp = input('Digite a temperatura em ºK:\n')

