from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_coca_cola = Bebida('coca-cola', 2.50, '350ml')
prato_pizza = Prato('pizza', 30.00, 'Sabor Calabresa')



def main(): # Executa a função main() caso este script seja importado como módulo
    print(bebida_coca_cola)
    print(prato_pizza)

if __name__ == "__main__": # Executa a função main() caso este script seja executado diretamente
    main()