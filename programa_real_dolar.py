class Conversor():

    def __init__(self, real) -> None:
        self.real = real
    
    def dolar_hoje(self):
        self.dolar = 4.94
        return self.dolar

    def converter(self):
        self.__real_dolar = round((self.real / self.dolar), 2)
        return self.__real_dolar

class interfaceSistema():

    def __init__(self, ligar=False) -> None:
        self.ligar = ligar
        if ligar == True:
            print("Seja Bem-Vindo ao Programa Real-Dolar !")
            real_user = int(input("Informe o Valor em Real (BRL):"))
            conversor_1 = Conversor(real_user)
            print("################################")
            print(f'Dolar Hoje: {conversor_1.dolar_hoje()}')
            print(f'Valor convertido: {conversor_1.converter()}')
        else:
            print("Sistema Offline")

interfaceSistema(True)


