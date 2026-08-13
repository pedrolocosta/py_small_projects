from datetime import datetime

class Account:                                                         # creating the class Account
    def __init__(self, bank, acc_id, holder_id, balance:float=0.0):  
        self.bank = bank                                               # setting parameters
        self.acc_id = acc_id                  # para o id da conta
        self.holder_id = holder_id            # para o id do titular
        self.balance = balance                # para o saldo incial
        self.start_date = datetime.now()      # para o momento da abertura da conta

    def deposit(self, amount:float):          # creating deposit method to increase the balance
        self.balance += amount
        
    def withdraw(self, amount:float):         # creating withdraw method to reduce the balance
        self.balance -= amount

    @staticmethod                             # usando um decorador para criar um staticmethod
    def bankphone(bank):                      # creating a bank call method to get the bank contact number
        banknumber = '1-000-1234567'
        print(banknumber)

    @ classmethod   # usando o decorador para criar um método de classe
    def quick(cls, string): # criando um método de inclusão rápida de cliente
        '''
        create an account from a string using only account and holder ids
        separated by slash
        '''
        bank = 'default_bank'
        acc_id, holder_id = string.split('/')  # dividindo a string e associando aos parâmetros do cliente 
        balance = 0.0
        return cls(bank, acc_id, holder_id, balance)

# Testando a classe e os parâmetros
first = Account('old_trusty', '001', '10043', 500) # criando a primeira conta
# print(old_trusty.__dict__)
first.deposit(250) # testando o método deposit
first.withdraw(400) # testando o método withdraw
print(first.balance )# confirmando o valor do saldo

second = Account.quick('002/10123') # criando a segunda conta com o método quick
print(second.start_date.year) # imprima o ano