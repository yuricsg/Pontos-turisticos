from models import PontoTuristico
from views import MenuView

class TouristaController:
    def __init__(self, ponto_turistico_dao):
        self.ponto_turistico_dao = ponto_turistico_dao

    def mostrar_informacoes(self, ponto):
        pontos_turisticos = self.ponto_turistico_dao.carregar_pontos_turisticos()
        for ponto_turistico in pontos_turisticos:
            if ponto_turistico.nome == ponto:
                print("=" * 40)
                print(f"Nome: {ponto_turistico.nome}")
                print(f"Local: {ponto_turistico.local}")
                print(f"Descrição: {ponto_turistico.descricao}")
                print(f"Horário de Funcionamento: {ponto_turistico.horario_funcionamento}")
                print(f"Custo de Entrada: {ponto_turistico.custo_entrada}")
                print("=" * 40)
                return
        print("Ponto turístico não encontrado.")

    def adicionar_ponto_turistico(self, nome, local, descricao, horario_funcionamento, custo_entrada):
        novo_ponto = PontoTuristico(nome, local, descricao, horario_funcionamento, custo_entrada)
        self.ponto_turistico_dao.adicionar_ponto_turistico(novo_ponto)

    def main(self):
        while True:
            MenuView.menu_principal()
            opcao = MenuView.obter_opcao()
            if opcao == "1":
                ponto = 'Recife Antigo'
                self.mostrar_informacoes(ponto)
            elif opcao == "2":
                ponto = 'Alto da Sé'
                self.mostrar_informacoes(ponto)
            elif opcao == '3':
                ponto = 'Cristo Redentor'
                self.mostrar_informacoes(ponto)
            elif opcao == '4':
                ponto = 'Torre Eiffel'
                self.mostrar_informacoes(ponto)
            elif opcao == '5':
                ponto = 'Coliseu'
                self.mostrar_informacoes(ponto)
            elif opcao == '6':
                ponto = 'Palacio de Buckingham'
                self.mostrar_informacoes(ponto)
            elif opcao == '7':

                MenuView.mostrar_menuBusca()
                opcao = MenuView.obter_opcao()
                if opcao == "1":
                    ponto = input("Digite o nome do ponto turístico: ").lower()
                    self.mostrar_informacoes(ponto)
                elif opcao == "2":
                    nome = input("Digite o nome do novo ponto turístico: ")
                    local = input("Digite o local: ")
                    descricao = input("Digite a descrição: ")
                    horario_funcionamento = input("Digite o horário de funcionamento: ")
                    custo_entrada = input("Digite o custo de entrada: ")
                    self.adicionar_ponto_turistico(nome, local, descricao, horario_funcionamento, custo_entrada)
            
                
                elif opcao == "3":
                    MenuView.mostrar_menuBusca()
                elif opcao == "4":
                    print("Obrigado por usar o Tourista! Volte sempre!")
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
            
            else:
                print("Digite o que foi solicitado.")
                continue
