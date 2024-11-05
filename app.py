# Estruturas de Dados

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