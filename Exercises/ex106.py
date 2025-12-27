from time import sleep
import builtins

colors = {"transparent": "\033[m",
          "red": "\033[1;39;41m",
          "blue": "\033[1;39;46m",
          "yellow": "\033[1;39;43m",
          "white": "\033[7m",
          "purple": "\033[1;44m"}


def title(text, color):
    print(f"{color}~{colors['transparent']}"*(len(text)+4))
    print(f"{color}  {text}  {colors['transparent']}")
    print(f"{color}~{colors['transparent']}"*(len(text)+4))


def help_command(command):
    try:
        title(f"Acessando manual do comando '{command}'", colors['blue'])
        sleep(1)
        obj = getattr(builtins, command)
        print(f"{colors['white']}\n")
        print(f"{obj.__doc__}")
        print(f"{colors['transparent']}")
    except Exception:
        title(f"{command} não é um comando interno válido!", colors['red'])


def main():
    while True:
        title("Sistema de Ajuda PyHelp", colors['yellow'])
        func = input("Função ou biblioteca: ").lower()

        if func == "fim":
            title("Até logo!", colors['purple'])
            sleep(1)
            break
        else:
            help_command(func)



if __name__ == "__main__":
    main()