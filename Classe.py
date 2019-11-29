#Para executar, basta ir pelo cmd até o local que o arquivo está salvo e digitar: python Classe.py 
class produto_de_3():
    
    def __init__(self, a=0,b=0,c=0):
        self._a = a
        self._b = b
        self._c = c
    
    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self):
        self.a = a
    
    @property
    def b(self):
        return self._b
    
    @b.setter
    def b(self):
        self.b = b
    
    @property
    def c(self):
        return self._c
    
    @c.setter
    def c(self):
        self.c = c
        
    def produto(self):
        return (self.a * self.b * self.c)

#Utilizando o construtor para passar os valores
p_3 = produto_de_3(3,3,3)
print('produto de 3,3,3 = ', p_3.produto())


p_3_5_2 = produto_de_3()

#Setando valores
p_3_5_2._a = 3
p_3_5_2._b = 5
p_3_5_2._c = 2

print('produto de 3,5,2 = ', p_3_5_2.produto())

#Métodos Get
print(p_3_5_2.a)
print(p_3_5_2.b)
print(p_3_5_2.c)

