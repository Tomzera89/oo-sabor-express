from modelos.cardapio.item_cardapio import Cardapio

class Bebida(Cardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08) # Aplicando desconto de 8%