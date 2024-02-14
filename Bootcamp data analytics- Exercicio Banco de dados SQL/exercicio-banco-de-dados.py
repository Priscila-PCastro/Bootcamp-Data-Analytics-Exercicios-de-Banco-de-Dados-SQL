import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# 1.  Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# 2.Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Isadora",23,"Mediciana")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"Maria Eduarda",19,"Administração")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"Luiz Henrique",18,"Computação")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Paula",25,"Farmácia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Marco",30,"Nutrição")')

# 3.Consultas Básicas: Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecionar todos os registros da tabela "alunos".

#dados = cursor.execute('SELECT * FROM alunos')

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

#dados = cursor.execute('SELECT nome,idade FROM alunos GROUP BY idade HAVING idade>20')

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

#dados = cursor.execute('SELECT * FROM alunos ORDER BY curso ASC')

# d) Contar o número total de alunos na tabela

#dados = cursor.execute('SELECT count() FROM alunos')

#4. Atualização e Remoção

# a) Atualize a idade de um aluno específico na tabela.

#dados = cursor.execute('UPDATE alunos SET idade=35 WHERE nome="Marco"')

# b) Remova um aluno pelo seu ID.

#dados = cursor.execute('DELETE FROM alunos where id=5')

# 5. Criar uma Tabela e Inserir Dados Crie uma tabela chamada "clientes" com os campos: 
# id (chave primária), nome (texto), idade (inteiro) e saldo (float).
# Insira alguns registros de clientes na tabela.

#cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo DECIMAL(10,2));')

#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1,"Carla",42, 600.00)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3,"José",30, 1000.00)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4,"Paula",28, 500.00)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5,"Cristiane",40, 50.00)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(6,"Fabricia",45, 100.00)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(7,"Emiliano",50, 80.50)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(8,"Giovana",35, 65.00)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(9,"Pedro",38, 400.00)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(10,"Luiz Henrique",18, 200.00)')

# 6.6. Consultas e Funções Agregadas.Escreva consultas SQL para realizar as seguintes tarefas:

#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

#dados = cursor.execute('SELECT nome,idade FROM clientes WHERE idade> 30 GROUP BY nome,idade')

#b) Calcule o saldo médio dos clientes.
#dados = cursor.execute('SELECT Round(AVG(saldo), 2) AS saldo_medio FROM clientes')

#c) Encontre o cliente com o saldo máximo.
#dados = cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1;')

#d) Conte quantos clientes têm saldo acima de 1000. 
#dados = cursor.execute('SELECT count(*) FROM clientes WHERE saldo>1000')

#7. Atualização e Remoção com Condições

#a) Atualize o saldo de um cliente específico.
#dados = cursor.execute('UPDATE clientes SET saldo=2500.00 WHERE nome="Emiliano"')

#b) Remova um cliente pelo seu ID.
#dados = cursor.execute('DELETE FROM clientes WHERE id=9')

#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: 
#id(chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 
#cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor REAL)')


#Insira algumas compras associadas a clientes existentes na tabela "clientes".

#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1, 1, "Calça Jeans Levis", 250.00)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(2, 2, "Short Jeans Levis", 180.00)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(3, 3, "Blusa Levis", 104.00)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(4, 4, "Calça Jeans Levis", 150.00)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(5, 5, "Camisa Jeans Levis", 300.00)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(6, 6, "Camisa Jeans Levis", 250.00)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(7, 7, "Short Jeans Levis", 300.00)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(8, 8, "Short Jeans Levis", 195.00)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(9,10, "Blusa Levis", 104.00)')

#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

#dados = cursor.execute('SELECT c.nome, co.produto, co.valor FROM clientes AS c JOIN compras AS co ON c.id = co.cliente_id')


for clientes in dados:
   print(clientes)

conexao.commit()
conexao.close