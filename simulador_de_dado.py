import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
          if resposta == 'sim' or resposta == 's':
              self.Gerar_valor_do_dado()
          elif resposta == 'não' or resposta == 'n':
              print('Obrigado pela participação')
          else:
              print('Favor digitar sim ou não')
        except:
          print('Ocorreu um erro ao receber sua resposta')

    def Gerar_valor_do_dado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()