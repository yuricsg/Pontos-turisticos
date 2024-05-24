from models import PontoTuristicoDAO
from controllers import TouristaController

def main():
    ponto_turistico_dao = PontoTuristicoDAO('pontos_turisticos.json')
    tourista_controller = TouristaController(ponto_turistico_dao)
    tourista_controller.main()

if __name__ == "__main__":
    main()
