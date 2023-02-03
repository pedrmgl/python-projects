
while True:
    primeiro_numero = input('Digite o primeiro número: ')
    segundo_numero = input('Digite o segundo número: ')
    operador = input('Digite o operador (+ , - , / , *): ')

    numero_valido = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(primeiro_numero)
        num_2_float = float(segundo_numero)
        numero_valido = True
    except:
        print('Não é possível realizar o cálculo.')
        numero_valido = None
        continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando cálculo. Confira o resultado abaixo.')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {num_1_float+num_2_float}')
    if operador == '-':
        print(f'{num_1_float} - {num_2_float} = {num_1_float-num_2_float}')
    if operador == '/':
        print(f'{num_1_float} / {num_2_float} = {num_1_float/num_2_float}')
    if operador == '*':
        print(f'{num_1_float} * {num_2_float} = {num_1_float*num_2_float}')
    

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break





