class MenuView:
    @staticmethod
    def mostrar_menuBusca():
        print("=" * 40)
        print("Escolha uma opção:")
        print("1. Ver informações sobre um ponto turístico")
        print("2. Adicionar um novo ponto turístico")
        print("3. Voltar ao menu principal")
        print("4. Sair")
        print("=" * 40)
    
    def menu_principal():      
        print("Bem-vindo(a) ao Tourista!")
        print("1. Recife Antigo")
        print("2. Alto da Sé")
        print("3. Cristo Redentor")
        print("4. Torre Eiffel")
        print("5. Coliseu")
        print("6. Palacio de Buckingham")
        print("7. Buscar outro ponto turístico ou adicionar")


    @staticmethod
    def obter_opcao():
        return input("Escolha uma opção: ")
