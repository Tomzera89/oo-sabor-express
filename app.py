from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_praca.alterar_status()



def main(): # Executa a função main() caso este script seja importado como módulo
    Restaurante.listar_restaurantes()

if __name__ == "__main__": # Executa a função main() caso este script seja executado diretamente
    main()