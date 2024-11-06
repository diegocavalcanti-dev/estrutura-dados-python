# Estruturas de Dados ------------------------------

# Listas

dia_11_saldo_inicial = 1000

dia_11_transacao_1 = 243
dia_11_transacao_2 = -798.58
dia_11_transacao_3 = 427.12
dia_11_transacao_4 = -10.91

dia_11_saldo_final = dia_11_saldo_inicial + dia_11_transacao_1 + dia_11_transacao_2 + dia_11_transacao_3 + dia_11_transacao_4

print(dia_11_saldo_final)



# Conjuntos

hashtags_seg = ['#tiago', '#joao', '#bbb']
hashtags_ter = ['#sarah', '#bbb', '#fiuk']
hashtags_qua = ['#gil', '#thelma', '#lourdes']
hashtags_qui = ['#rafa', '#fora', '#danilo']
hashtags_sex = ['#juliete', '#arthur', '#bbb']

hashtags_semana = hashtags_seg + hashtags_ter + hashtags_qua + hashtags_qui + hashtags_sex
print(hashtags_semana)

print(hashtags_semana)
print(len(hashtags_semana))

hashtags_semana = list(set(hashtags_seg + hashtags_ter + hashtags_qua + hashtags_qui + hashtags_sex))

print(hashtags_semana)
print(len(hashtags_semana))


# Dicionários

wifi_disponiveis = ['rede1', 'cnx_cnx', 'uai-fi', 'r3d3']
print(wifi_disponiveis)

wifi_disponiveis = []

rede = {'nome': 'rede1', 'senha': 'cnx_cnx'}
wifi_disponiveis.append(rede)

rede = {'nome': 'uai-fi', 'senha': 'r3d3'}
wifi_disponiveis.append(rede)

print(wifi_disponiveis)


# Fluxo condicional e Repetição ------------------------------

# Estrutura condicional if / else / elif

# if <booleano / comparação lógica> == True:
#   <execute este código>
# else:
#   <senão execute este código>


# if False:
# print("Verdadeiro")
#     else:
# print("Falso")


codigo_de_seguranca = '291'
codigo_de_seguranca_cadastro = '010'

pode_efetuar_pagamento = codigo_de_seguranca == codigo_de_seguranca_cadastro
print(pode_efetuar_pagamento)

if pode_efetuar_pagamento:
  print("Pagamento efetuado")
else:
  print("Erro: Código de segurança inválido")
  
if codigo_de_seguranca == codigo_de_seguranca_cadastro:
  print("Pagamento efetuado")
else:
  print("Erro: Código de segurança inválido")
  
  
# 1.2. if / elif / else
# Podemos também avaliar múltipla condições.

# if <1º booleano / 1ª comparação lógica> == True:
#   <execute este código se a primeira condição for verdade>
# elif <2º booleano / 2ª comparação lógica> == True:
#   <execute este código se a segunda condição for verdade>
# else:
#   <senão execute este código>


codigo_de_seguranca = '802'
codigo_de_seguranca_cadastro = '852'

senha = '7703'
senha_cadastro = '7783'


if (codigo_de_seguranca == codigo_de_seguranca_cadastro) & (senha == senha_cadastro):
  print("Pagamento efetuado")

elif (codigo_de_seguranca != codigo_de_seguranca_cadastro) & (senha == senha_cadastro):
  print("Erro: Código de segurança inválido")

elif (codigo_de_seguranca == codigo_de_seguranca_cadastro) & (senha != senha_cadastro):
  print("Erro: Senha inválida inválida")

else:
  print("Erro: Código de segurança e senha inválidos")
  
  
  
  
# Estrutura condicional try /except / finally
# 2.1. Exceção
# Exceções são erros que podem acontecer durante a execução do nosso código.

# Exemplo: Erro de operações numéricas impossíveis
preco = 132.85
pessoas = 0

valor_por_pessoa = preco / pessoas


# Exemplo: Erro por combinações de tipos diferentes
nome = 'Andre Perez'
idade = True

apresentacao = 'Fala pessoal, meu nome é ' + nome + ' e eu tenho ' + idade + ' anos'

# Exemplo: Erro de indexação de estrutura de dados
anos = [2019, 2020, 2021]
ano_atual = anos[3]

cursos = {
    'python': {
        'nome': 'Python para Análise de Dados', 'duracao': 2.5
    }, 
    'sql': {
        'nome': 'SQL para Análise de Dados', 'duracao': 2
    }
}
curso_atual = cursos['analista']

# 2.2. try / except
# Estrutura para tratar exceções:

preco = 132.85
pessoas = 2

try:
  valor_por_pessoa = preco / pessoas
  print(valor_por_pessoa)
except ZeroDivisionError:
  print('Número de pessoas inválido. Espera-se um valor maior que 0 e obteve-se um valor igual a ' + str(pessoas))
  
#################  
anos = [2019, 2020, 2021]

try:
  ano_atual = anos[3]
  print(ano_atual)
except Exception:
  print('Lista de anos é menor que o valor escolhido. Espera-se um valor entre 0 e ' + str(len(anos) - 1))
  
anos = [2019, 2020, 2021]

try:
  ano_atual = anos[3]
  print(ano_atual)
except Exception as exc:
  print('Descrição da exceção: ' + str(exc))
  print('Tipo da exceção: ' + str(type(exc)))
  print('Lista de anos é menor que o valor escolhido. Espera-se um valor entre 0 e ' + str(len(anos) - 1))
  
# 2.3. try / except / finally
nome = 'Andre Perez'
idade = 19

try:
  apresentacao = 'Fala pessoal, meu nome é ' + nome + ' e eu tenho ' + idade + ' anos'
  print(apresentacao)
except TypeError:
  idade = str(idade)
finally:
  print('Segunda chance')
  apresentacao = 'Fala pessoal, meu nome é ' + nome + ' e eu tenho ' + idade + ' anos'
  print(apresentacao)
  


# Estrutura repetição for / in
# 3.1. for / in
# for variavel_temporaria in coleção:
#   <execute este código>

# 3.2. for / in / range
# Estrutura que permite a execução repetida de um bloco de código n vezes.

for valor in range(6):
  print(valor)
  
soma = 0

for valor in range(0, 100000):
  soma = soma + valor
  # print(soma)

print(soma)