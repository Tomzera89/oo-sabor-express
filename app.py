from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Everton', 5)
restaurante_praca.receber_avaliacao('Maria', 6)
restaurante_praca.receber_avaliacao('José', 8)

restaurante_praca.alterar_status()



def main(): # Executa a função main() caso este script seja importado como módulo
    Restaurante.listar_restaurantes()

if __name__ == "__main__": # Executa a função main() caso este script seja executado diretamente
    main()