from modelos.cardapio.item_cardapio import Cardapio

class Sobremesa(Cardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        self._descricao = descricao

    def __str__(self):
        return self._nome # Retornando o nome do item cardápio como string
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)