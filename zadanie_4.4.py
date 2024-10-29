#Zadanie 4.4

import logging
logging.basicConfig(level=logging.DEBUG)

#Definicje funkcji kalkulatora z parametrami

def dodawanie(a, b):
    return a + b
def odejmowanie(a, b):
    return a - b
def mnożenie(a, b):
    return a * b
def dzielenie(a, b):
    if b == 0:
        logging.warning("Próba dzielenia przez zero!")
        return "Błąd: nie można dzielić przez zero"
    return a / b

if __name__ == "__main__":
    print("To jest prosty kalkulator")
    print("Proszę wybierz liczbę odpowiadającą działaniu jakie chcesz wykonać: 1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie")
    operacja = int(input("Podaj numer operacji którą chcesz wykonać: "))

    if operacja not in {1, 2, 3, 4}:
        print("Nieprawidłowy wybór, spróbuj ponownie.")
    else:
        a = float(input("Podaj pierwszą liczbę (a): "))
        b = float(input("Podaj drugą liczbę (b): "))

#Wykonanie odpwiedniego działania

    if operacja == 1:
        logging.debug(f"Dodaję {a} i {b}")
        print(f"Wynik to: {dodawanie(a, b)}")
    elif operacja == 2:
        logging.debug(f"Odejmuję {a} od {b}")
        print(f"Wynik to: {odejmowanie(a, b)}")
    elif operacja == 3:
        logging.debug(f"Mnożę {a} i {b}")
        print(f"Wynik to: {mnożenie(a, b)}")
    elif operacja == 4:
        logging.debug(f"Dzielę {a} przez {b}")
        print(f"Wynik to: {dzielenie(a, b)}")