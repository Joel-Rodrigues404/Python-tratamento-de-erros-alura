from pprint import pprint
from my_exceptions import SaldoInsuficienteError, OperacaoFinanceiraError
from leitor import LeitorDeArquivo

class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.__agencia = 0
        self.__numero = 0
        self.saques_nao_permitidos = 0
        self.transferencias_nao_permitidas = 0
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30/ContaCorrente.total_contas_criadas
    
    @property #padrao do metodo e getter ou seja vai ser executado enquanto esta lendo o atributo agencia
    def agencia(self):
        return self.__agencia  
     
    
    def __set_agencia(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo da agencia deve ser um inteiro" ,value)
        if value <= 0:
            raise ValueError("O atributo da agencia deve ser maior que zero")
        self.__agencia = value

    @property #padrao do metodo e getter ou seja vai ser executado enquanto esta lendo o atributo agencia
    def numero(self):
        return self.__numero 
     
    
    def __set_numero(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo da numero deve ser um inteiro")
        if value <= 0:
            raise ValueError("O atributo da numero deve ser maior que zero")
        self.__numero = value

    @property #padrao do metodo e getter ou seja vai ser executado enquanto esta lendo o atributo agencia
    def saldo(self):
        return self.__saldo
     
    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo da saldo deve ser um inteiro")
        self.__saldo = value
    

    def transferir(self, valor, favorecido):
        if self.saldo < 0:
            raise ValueError("O valor a ser sacado não pode ser menor que zero")
        try:
            self.sacar(valor)
        except SaldoInsuficienteError as E:
            self.transferencias_nao_permitidas += 1
            E.args = ()
            raise OperacaoFinanceiraError("Operaçao não finalizada") from E
        favorecido.depositar(valor)
    
    def sacar(self, valor):
        if self.saldo < 0:
            raise ValueError("O valor a ser sacado não pode ser menor que zero")
        if self.saldo < valor:
            self.saques_nao_permitidos += 1
            raise SaldoInsuficienteError("", saldo=self.saldo, valor=valor)
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor



def main():
    import sys

    contas = []
    while True:
        try:
            nome = input("Nome do Cliente:\n")
            agencia = input("Numero da Agencia:\n")
            breakpoint()
            numero = input("Numero da Conta Corrente:\n")
            cliente = Cliente(nome, None, None)
            conta_corrente = ContaCorrente(cliente, agencia, numero)
            contas.append(conta_corrente)
        # except ValueError as E:
        #     print(E.args)
        #     sys.exit()
        except KeyboardInterrupt:
            print(f'\n\n{len(contas)} Contas Criadas')
            sys.exit()

# if __name__ == "__main__":
#     main()

# conta_corrente = ContaCorrente(None, 0, 100)
# print(conta_corrente.agencia)


conta_corrente1 = ContaCorrente(None, 400, 1234567)
conta_corrente2 = ContaCorrente(None, 401, 1234568)

with LeitorDeArquivo("arquivo.txt") as leitor:
    leitor.ler_proxima_linha()


# try:
#     leitor = LeitorDeArquivo("arquivo.txt")
#     leitor.ler_proxima_linha()
#     leitor.ler_proxima_linha()
#     leitor.ler_proxima_linha()
#     # leitor.fechar()
# # except IOError:
# #     print("exeçao do tipo IOerror capturada e tratada")

# finally:
#     if "leitor" in locals():
#         leitor.fechar()
# try:
#     conta_corrente1.transferir(100000, conta_corrente2)
#     print(f'conta1 saldo {conta_corrente1.saldo}\n' \
#         f'conta2 saldo {conta_corrente2.saldo}')
# except OperacaoFinanceiraError as E:
#     import traceback 
#     print(E.__context__.saldo)
#     print(E.__context__.valor)
#     print('Exeçao do tipo', E.__context__.__class__.__name__)#contexto do porque ela aconteceu
#     print('Exeçao do tipo', E.__class__.__name__) #por onde ela aconteceu

#     traceback.print_exc()


# cliente = Cliente('jonh','394218', 'carteiro')
# print(cliente.cpf)
# print(cliente.nome)
# print(cliente.profissao)

# pprint(cliente.__dict__, width=40)
# cliente.idade = 20

# print(cliente.idade)