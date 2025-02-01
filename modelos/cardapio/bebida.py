class Bebida:
    def __init__(self, nome, preco, tamanho):
        self._nome = nome.title()
        self._preco = preco
        self._tamanho = tamanho.upper()