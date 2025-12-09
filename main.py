from calculator import add
from greetings import say_hello

def run():
    print(say_hello("GitHub"))
    print("2 + 5 =", add(2, 5))

if __name__ == "__main__":
    run()
