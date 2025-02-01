class Prato:
    def __init__(self, nome, preco, descricao):
        self._nome = nome.title()
        self._preco = preco
        self._descricao = descricao