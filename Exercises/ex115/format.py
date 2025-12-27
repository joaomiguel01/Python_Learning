colors = {'transparent': "\033[m",
          'red': "\033[1;31m",
          'blue': "\033[1;36m",
          'yellow': "\033[1;33m",
          'green': "\033[1;32m"}

def title(text):
    print("~"*40)
    print(f"{text:^40}")
    print("~"*40)