#Para executar, basta ir pelo cmd até o local que o arquivo está salvo e digitar: python Arrays.py 

estados = ['Minas Gerais', 'Rio de Janeiro', 'São Paulo', 'Espírito Santo']
siglas = ['ES', 'MG', 'SP', 'RJ']

dic = dict(zip(sorted(siglas), sorted(estados)))
for d in dic.items():
    print(d[0] + ' -> ' + d[1])

