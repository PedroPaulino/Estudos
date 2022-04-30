class Conversor():


    def __init__(self, real) -> None:
        self.real = real
    
    def dolar_hoje(self):
        self.dolar = 4.94
        return self.dolar

    def converter(self):
        self.__real_dolar = round((self.real / self.dolar), 2)
        return self.__real_dolar

print(" Programa Conversor de Real para Dolar")
print("################################")
real_informado_usuario = int(input("Informe o valor em real: "))
conversao_1 = Conversor(real_informado_usuario)
print("################################")
print(f'Dolar Hoje: {conversao_1.dolar_hoje()}')
print("################################")
print(f'Valor convertido: {conversao_1.converter()}')

