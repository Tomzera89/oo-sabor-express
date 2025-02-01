from abc import ABC, abstractmethod # Definindo a classe Cardapio como abstrata

class Cardapio(ABC): # Classe abstrata
    def __init__(self, nome, preco):
        self._nome = nome.title()
        self._preco = preco


    @abstractmethod
    def aplicar_desconto(self, desconto):
        pass