import logging
from tkinter import *
logging.basicConfig(level=logging.DEBUG)
class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('Gestor de clientes')
        self.build()
    def build(self):
        button = Button(self.root, text="Hola", command=self.hola)
        button.pack()
    def hola(self):
        logging.debug("¡Hola mundo!")
if __name__ == "__main__":
    logging.debug('Iniciando aplicación')
    app = MainWindow()
    app.mainloop()
    logging.debug('Fin de la aplicación')
    
