class OperacaoFinanceiraError(Exception):
    pass

class SaldoInsuficienteError(OperacaoFinanceiraError):
    def __init__(self, message='', saldo=None, valor=None, *args):
        self.saldo = saldo
        self.valor = valor
        msg = 'Saldo insuficiente para efetuar a transação\n' \
            f'Saldo Atual: {self.saldo} Valor a ser sacado: {self.valor}'
        self.msg = message or msg
        super(SaldoInsuficienteError, self).__init__(message or msg, self.saldo, self.valor *args)