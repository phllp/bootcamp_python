# Utilizar o Lock impede que outras Threads sejam instanciadas para determinado processo antes que o processo de 
# uma thread anterior seja finalizada
from threading import Thread, Lock
from time import sleep

class Padaria:
  def __init__(self, estoque):
    self.estoque = estoque
    self.lock = Lock()

  def comprar(self, qtde):
    self.lock.acquire()
    if self.estoque < qtde:
      print('Nao possuimos a quantidade de paes solicitada em estoque.')
      self.lock.release()
      return 
    sleep(1)

    self.estoque -= qtde
    print(f'Voce comprou {qtde} paes. Ainda temos {self.estoque} em estoque')
    self.lock.release()

if __name__ == '__main__':
  padaria = Padaria(20)
  for i in range(20):
    t = Thread(target=padaria.comprar, args=(i,))
    t.start()