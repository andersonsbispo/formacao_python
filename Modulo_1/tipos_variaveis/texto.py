#Declaração
nome_completo = 'Anderson Bispo'

nome_completo_aspas = '''Anderson
Bispo'''

nome_completo_quebra = 'Anderson \
Bispo'

nome = 'Anderson'
sobrenome = 'Bispo'

#Formatação
print('Nome completo (1ª forma):', nome_completo)
print('Nome completo (2ª forma):' + nome_completo)
print('Nome completo (3ª forma):' + 'Anderson' + 'Bispo')
print('Nome completo (4ª forma):' + 'Anderson', 'Bispo')
print('Nome completo (5ª forma):', nome_completo_aspas)
print('Nome completo (6ª forma):', nome_completo_quebra)
print('Nome completo (7ª forma): %s' %nome_completo)
print('Nome completo (8ª forma): %s %s' %(nome, sobrenome))
print(f'Nome completo (9ª forma): {nome} {sobrenome}')
print('Nome completo (10ª forma): {} {}'.format(nome, sobrenome))