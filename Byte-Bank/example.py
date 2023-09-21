
def dividir(dividendo, divisor):
    
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError("dividir() deve conter apenas argumentos inteiros")
    
    try:
        aux =  dividendo/divisor
    except:
        print(f'Não foi possivel dividir {dividendo} pelo {divisor}')
        raise
    return aux


def testa_divisao(divisor):
    # try:
    resultado = dividir(10, divisor)
    print(f'O resultado da divisão de 10 por {divisor} e igual a {resultado}')
    # except ZeroDivisionError:
    #     print("Erro de divisão por erro tratado")
    # except ArithmeticError:
    #     print("Erro de atributo tratado")

# try:
#     teste = testa_divisao(2.5)
# # except Exception as E:#serve para todas as exeçoes pois trabalham com o conceito de polimorfismo
# #     print(E.__class__.__bases__) 
# except TypeError as E:
#     print(f'Tratamento para erro de tipo > {E}')
# except AttributeError as E:
#     print(f'Tratamento para erro de atributo > {E}')
# except ZeroDivisionError as E:
#     print(f'Tratamento de divisão por zero > {E}')
# except Exception as E:
#     print(f'Tratamento de erro generalista > {E}')
# finally:
#     print('Programa Encerrado')

# try:
#     print(f'O fluxo esta aqui')
#     raise ValueError
# except SyntaxError:
#     print(f'Agora ele foi pra ca')

# print(f'E fim ele continua ...')

