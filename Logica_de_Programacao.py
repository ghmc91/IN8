#Para executar, basta ir pelo cmd até o local que o arquivo está salvo e digitar: python Logica_de_Programacao.py 

def tres_cinco():

    lista = []
    for i in range(1000):    
        if (i%3==0 and i%5==0):
            lista.append(i)
    return sum(lista)

print('soma dos números divisíveis por 3 e 5 menores que 1000: ', tres_cinco())

