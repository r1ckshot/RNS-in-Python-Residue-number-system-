import numpy as np

def znajdz_reszte(liczba, modulo):   # Funkcja przyjmuje liczbe, oraz liste modulo
    reszta1 = []    # Stworzenie listy dla wyniku
    for a in modulo:  # Dla kazdej liczby w liscie modulo (zaczynajac od 1 liczby)
        reszta = liczba % a   # Zmienna szuka reszte dla liczby przez 1 el.(liczbe) listy modulo
        reszta1.append(reszta)   # Zapisuje ta liczbe do wynikowej listy
    return reszta1  # Zwraca wynikowa liste

def reszta_dla_reszty(reszta, modulo):  # Funkcja przyjmuje dwie listy (1 - wynik dzialania na resztach, 2 - modulo)
    reszta1 = []    # Stworzenie listy dla wyniku
    for i in range(len(reszta)):   # Dla kazdej liczby w obu listach
        wynik = reszta[i] % modulo[i]  # Zmienna jeszcze raz szuka reszte przez modulo dla kazdej liczby w obu listach
        reszta1.append(wynik)    # Zapisuje ta liczbe do wynikowej listy
    return reszta1    # Zwraca wynikowa liste

def RNS(reszta, modulo):  # Funkcja przyjmuje dwie listy (1 - Poprawiony wynik dzialania na resztach, 2 - modulo)
    for x in range(0, 1000):   # Tu Pan wybiera zakres Wyniku
        k = 0
        for i in range(len(reszta)):  # Dla kazdej liczby w obu listach
            if(x % modulo[i]) == reszta[i]:  # Jezeli "liczba" modulo "liczba podana przez Pana" == reszcie z Wynikowej
                # listy, to:
                k += 1  # Zwieksza k
            else:
                k = 0   # W przeciwnym przypadku k jest rowny 0

            if k == len(reszta):  # Jezeli k jest rowny dlugosci listy z resztami, oznacza to, ze X podchodzi
                # dla wszystkich reszt
                return x  # Zwraca Wynik
    if k == 0:
        return None




liczba1 = int(input("Podaj 1 liczbe: "))
liczba2 = int(input("Podaj 2 liczbe: "))

iloscM = int(input("Podaj ilosc modulo: "))

j = 0
modulo = []

if iloscM <= 0:
    print("Podana nie poprawna liczba modulo")
    exit()
else:
    while iloscM != j:
        modulo1 = int(input("Podaj modulo: "))
        modulo.append(modulo1)
        j += 1


reszta1 = znajdz_reszte(liczba1, modulo)
reszta2 = znajdz_reszte(liczba2, modulo)

print("Reszta dla liczby:", liczba1, "modulo", modulo, "wynosi: ", reszta1)
print("Reszta dla liczby:", liczba2, "modulo", modulo, "wynosi: ", reszta2)



print("Podaj operacje na resztach ktora chcesz zrobic: ")

print("1) Dodawanie")
print("2) Odejmowanie")
print("3) Mnozenie")
print("4) Dzielenie")
wybor = int(input("Podaj wybor: "))

if wybor == 1:
    operacja = np.add(reszta1, reszta2)
    Dodawanie = list(operacja)
    Reszta_Dla_Dodawania = reszta_dla_reszty(Dodawanie, modulo)

    print("Poczatkowy wynik:", Dodawanie)
    print("Wynik dodawania: ", Reszta_Dla_Dodawania, " przez moduly: ", modulo)

    x = RNS(Reszta_Dla_Dodawania, modulo)
    print("X wynosi: ", x)

    for i in range(len(Dodawanie)):
        print(x, " modulo ", modulo[i], " = ", Reszta_Dla_Dodawania[i])


elif wybor == 2:
    operacja = np.subtract(reszta1, reszta2)
    Odejmowanie = list(operacja)
    Reszta_Dla_Odejmowania = reszta_dla_reszty(Odejmowanie, modulo)

    print("Poczatkowy wynik: ", Odejmowanie)
    print("Wynik odejmowania: ", Odejmowanie, " przez moduly: ", modulo)

    x = RNS(Reszta_Dla_Odejmowania, modulo)
    print("X wynosi: ", x)

    for i in range(len(Odejmowanie)):
        print(x, " modulo ", modulo[i], " = ", Odejmowanie[i])


elif wybor == 3:
    operacja = np.multiply(reszta1, reszta2)
    Mnozenie = list(operacja)
    Reszta_Dla_Mnozenia = reszta_dla_reszty(Mnozenie, modulo)

    print("Poczatkowy wynik: ", Mnozenie)
    print("Wynik mnozenia: ", Reszta_Dla_Mnozenia, " przez moduly: ", modulo)

    x = RNS(Reszta_Dla_Mnozenia, modulo)
    print("X wynosi: ", x)

    for i in range(len(Mnozenie)):
        print(x, " modulo ", modulo[i], " = ", Reszta_Dla_Mnozenia[i])


elif wybor == 4:
    if wybor == 4:
        if reszta2.count(0) > 0:
            print("Dzielienie przez 0 ")
            exit()
        else:
            operacja = np.divide(reszta1, reszta2)
            Dzielenie = list(operacja)
            Reszta_Dla_Dzielenia = reszta_dla_reszty(Dzielenie, modulo)

            print("Poczatkowy wynik: ", Dzielenie)
            print("Wynik dzielenia: ", Reszta_Dla_Dzielenia, " przez moduly: ", modulo)

            x = RNS(Reszta_Dla_Dzielenia, modulo)
            print("X wynosi: ", x)

            for i in range(len(Dzielenie)):
                print(x, " modulo ", modulo[i], " = ", Reszta_Dla_Dzielenia[i])


# Funkcjonalnosc programu:

# 1) Pan podaje 2 liczby
# 2) Pan wybiera ilosc modulo i wpisuje modulo
# 3) Do podanych zmiennych "reszta1" i "reszta2" sa wykonywana funkcja "znajdz_reszte" ktora szuka reszty dla 2 liczb
# przez podane modulo i zapisuje je w postaci listy; Oraz wyswietlona informacja

# 4) Dalej Pan wybiera aryfmetyczna opercje, ktore chce zrobic na resztach
# 5) Zmienna "operacja" ---> wykonuje operacje na resztach (czyli np. dodaje listy z resztami)
# 6) Zmienna "Dodawanie" przeksztalca list_numpy w zwykly list (dlatego zeby podalsza funkcja mogla dzialac na tym
# liscie)

# 7) Zmienna "Reszta_Dla_Dodawania" ---> jeszcze raz szuka innej reszty dla listy ze zmiennej "Dodawanie"
# przez podanych Panem modulo

# 8) Informacja o wyniku dzilania
# 9) Dla zmiennez "x" jest wykonywana funkcja "RNS", ktora szuka X, zeby spelnial warunek (czyli liczba ktora daje
# reszte z operacji np. Dodawanie, przez podanych Panem modulo)

# 10) Wynik :)


# Niuanse:

# 1) Robilem to sam, wiec program jest bardzo dziwny, ale dziala
# 2) Jezeli nie ma X, czyli wyniku, Pan musi zwiekszyc obszar wyszukiwan w funkcji "RNS"
# 3) Problem z Dzileniem, np. moze wyniknac dzielenie przez Zero lub nie Calkowita liczba,
# wiec dziala tylko dla podzielnych liczb
