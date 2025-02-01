from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import Cardapio

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria): # Método construtor que inicializa os atributos da class
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self) # Adicionando o restaurante à lista de restaurantes

    def __str__(self): # Método que retorna uma string
        return f'{self._nome} | {self.categoria} | {self.ativo}'

    @classmethod # (DECORADOR)Define um método que é vinculado à classe.
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante':<20} | {'Categoria':<20} | {'Avaliacao':<20} | {'Ativo'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome:<20} | {restaurante.categoria:<20} | {restaurante.media_avaliacoes:<20} | {restaurante.ativo}')

    @property # (DECORADOR)Define uma propriedade, que é um atributo com métodos getter, setter e deleter.
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alterar_status(self): # Método que altera o status do restaurante (ativo/inativo)
        self._ativo = not self._ativo

    
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        total_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)  # Calcula a 'soma' das notas para cada 'avaliação' na 'lista' self._avaliacao
        quanditade_avaliacoes = len(self._avaliacao)
        media_notas = round(total_notas / quanditade_avaliacoes, 1)
        return media_notas
    

    def adc_cardapio(self, item):
        if isinstance(item, Cardapio): # Verifica se o item passado como argumento é uma instancia da class Cardapio ou derivada dela
            self._cardapio.append(item)

    @property
    def exibe_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio, start=1): # Enumera os itens do cardápio com o número e nome do item
            if hasattr(item, '_descricao'): # Verifica se o item possui a descrição
                mensagem_prato = f'{i}. {item._nome} - R$ {item._preco:<10} | Descrição: {item._descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. {item._nome} - R$ {item._preco:<10} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)