class MenuView:
    @staticmethod
    def mostrar_menu():
        print("=" * 40)
        print("Bem-vindo(a) ao Tourista!")
        print("Escolha uma opção:")
        print("1. Ver informações sobre um ponto turístico")
        print("2. Adicionar um novo ponto turístico")
        print("3. Sair")
        print("=" * 40)

    @staticmethod
    def obter_opcao():
        return input("Escolha uma opção: ")
