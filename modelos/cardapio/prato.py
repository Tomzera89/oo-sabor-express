from modelos.cardapio.item_cardapio import Cardapio

class Prato(Cardapio): # Herança da classe Cardapio
    def __init__(self, nome, preco, descricao):  # nome e preco são herdados da superclasse
        super().__init__(nome, preco) # Chamando o método construtor da superclasse
        self._descricao = descricao

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05) # Aplicando desconto de 5%