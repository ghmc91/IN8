#Para executar, basta ir pelo cmd até o local que o arquivo está salvo e digitar: python Funcao_Recursiva.py 

def recursiva(n = 1):
    if (n%2==0 and n%3==0 and n%10==0):
        return n
    else:
        return recursiva(n+1)
print('Menor Número inteiro divisível por 2, 3 e 10: ', recursiva())

