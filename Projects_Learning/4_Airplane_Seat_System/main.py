# Python Airplane Seat System

from gui_utils import menu, read_option, title
from time import sleep

def main():
    while True:
        try:
            print()
            menu("SISTEMA DE RESERVA DE ASSENTOS AIR CANADA", ['Reservar uma Poltrona',
                                                               "Ver Poltronas",
                                                               "Desocupar uma Poltrona",
                                                               "Consultar uma Poltrona",
                                                               "Dados do Voo",
                                                               "Reiniciar os Assentos",
                                                               "Sair do Sistema"])
            
            choice = read_option("Digite uma opção: ", 7)
            sleep(1)
            print()

            match choice:
                case 1:
                    # Reserve a Seat
                    pass
                case 2:
                    # List Seats
                    pass
                case 3:
                    # Vacate Seat
                    pass
                case 4:
                    # Consulte Seat
                    pass
                case 5:
                    # Flight Data
                    pass
                case 6:
                    # Restart Seats
                    pass
                case 7:
                    title("SAINDO DO SISTEMA...")
                    sleep(1)
                    title("ATÉ LOGO!")
                    break
        except Exception as e:
            title("HOUVE UM ERRO AO REALIZAR O PROCEDIMENTO!")
            print(e)


if __name__ == "__main__":
    main()
