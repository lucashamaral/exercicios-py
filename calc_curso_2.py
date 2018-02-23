def calc_curso_2(aluno, valor, dias, porcen):
    str_list = [aluno, valor, dias, porcen]
    float_list = [float(x) for x in str_list]

    calc = (float_list[0] * float_list[1] * float_list[2]) // 100 * float_list[3]
    return calc

a = input('Alunos: ')
v = input('Valor: ')
d = input('Dias: ')
p = input('Porcentagem:')

print('O valor a pagar é: ', calc_curso_2(a, v, d, p))

