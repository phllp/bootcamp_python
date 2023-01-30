from threading import Thread
from time import sleep

class MyThread(Thread):
  def __init__(self, tempo, texto):
    self.texto = texto
    self.tempo = tempo
    super().__init__()

  def run(self):
    sleep(self.tempo)
    print(self.texto)


mt1 = MyThread(4, 'Thread 1 completed.')
mt1.start()

mt2 = MyThread(8, 'Thread 2 completed.')
mt2.start()

mt3 = MyThread(12, 'Thread 3 completed.')
mt3.start()

for i in range(20):
  print(i)
  sleep(.5)