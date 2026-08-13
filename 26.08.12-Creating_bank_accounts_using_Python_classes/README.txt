Crie uma classe Account() que represente uma conta bancária com os seguintes atributos:

bank para o nome do banco
acc_id para o id da conta
holder_id para o id do titular
balance para o saldo inicial da conta
start_date para a data e a hora em que a conta foi aberta
Certifique-se de que balance é do tipo float e tem um valor padrão de 0.0.
.
Adicione dois métodos de classe, deposit() e withdraw(); ambos aceitam números de ponto flutuante como argumentos e ajustam balance de acordo. O método deposit() aumenta o saldo balance, enquanto o método withdraw() o reduz.
Ambos os métodos esperam que a entrada amount seja do tipo float.
.
Adicione um método que busca o número de telefone de um determinado banco. Por exemplo, esse método pode pesquisar na web, encontrar o número de telefone do banco e imprimi-lo. Para simplificar as coisas, pedimos que você implemente essa funcionalidade criando um método estático bankphone. Esse método deve aceitar um nome de banco e imprimir sempre 1-000-1234567 como saída.
.
Suponha que precisemos de uma maneira rápida de adicionar uma conta usando uma string que armazena os IDs da conta e do titular. Por exemplo, temos uma string "001/2406".

Para alcançar isso, pedimos que você crie o método de classe quick(). Esse método deve esperar uma string com os IDs da conta e do titular, dividi-la em duas partes e armazenar os valores correspondentes nas variáveis acc_id e holder_id. Em seguida, o método deve retornar a classe, em que bank é sempre default_bank e balance é 0.0.

teste o programa
Hora de usar a classe. Crie uma instância chamada first (primeira) usando a forma padrão com as seguintes informações: o nome do banco é old_trusty, o ID da conta é 001, o ID do titular é 10043, a soma inicial é 500. Em seguida, deposite mais 250 unidades e retire 400. Imprima o saldo.

Em seguida, crie outra instância chamada second (segunda) usando o método quick() e passando '002/10123' como entrada. Imprima o ano em que uma conta foi criada 