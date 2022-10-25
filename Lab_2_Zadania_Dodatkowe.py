def Zadanie_Dodatkowe_1():
    """
    Wyznaczanie wartości liczby zapisanej w systemie pozycyjnym o podstawie p ∈ {2, … ,10}. Wartość
    liczby - liczba zapisana w systemie dziesiętnym. Na wejściu podajemy liczbę jako string, na wyjściu - liczbę
    dziesiętną typu int.
    """
    Liczba = input("Podaj Liczbę: ")
    Podstawa = int(input("Podaj Podstawę: "))
    Liczba_10 = 0

    if 2 <= Podstawa <= 10:
        for x in range(len(Liczba)):
            #print(f"{Liczba[x]} * {Podstawa}^{len(Liczba)-x-1} = {int(Liczba[x]) * (Podstawa ** (len(Liczba)-x-1))}")
            Liczba_10 += int(Liczba[x]) * (Podstawa ** (len(Liczba)-x-1))

        print(f"{Liczba} ({Podstawa}) == {Liczba_10} (10)")
    else:
        print("ERROR: Zła Podstawa")

def Zadanie_Dodatkowe_2():
    """
    Wyznaczanie wartości liczby podanej w systemie pozycyjnym o podstawie p ∈ {2, … ,10} przy użyciu
    algorytmu Horner'a. Na wejściu podajemy liczbę jako string, na wyjściu - liczbę dziesiętną typu int.
    """
    Liczba = input("Podaj Liczbę: ")
    Podstawa = int(input("Podaj Podstawę: "))
    Wynik = int(Liczba[0])

    #print(f"Wynik = {Wynik}")

    if 2 <= Podstawa <= 10:
        for x in range(len(Liczba) - 1):
            #print(f"Wynik = {Wynik} * {Podstawa} + {Liczba[x+1]}")
            Wynik = Wynik  * Podstawa + int(Liczba[x+1])
        pass

        print(f"Wynik: {Wynik}")
    else:
        print("ERROR: Zła Podstawa")

def Zadanie_Dodatkowe_3():
    """
    Wyznaczanie zapisu podanej liczby dziesiętnej w systemie pozycyjnym o podstawie p ∈ {2, … ,10, 16}.
    Na wejściu podajemy liczbę całkowitą, na wyjściu - liczbę zapisaną jako string.
    """
    Liczba = input("Podaj Liczbę: ")
    Liczba_Kopia = Liczba
    Podstawa = int(input("Docelowa Podstawa: "))
    Wynik = ""
    Mozliwe_Liczby = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"]

    if 2 <= Podstawa <= 16:
        while True:
            if Liczba == 0:
                Wynik = Wynik[::-1] # Odwrócenie Kolejności
                break
            else:
                Wynik += str(Mozliwe_Liczby[(int(Liczba) % Podstawa)]) 
                Liczba = int(Liczba) // Podstawa

        print(f"{Liczba_Kopia} (10) == {Wynik} ({Podstawa})")
    else:
        print("ERROR: Zła Docelowa Podstawa")

if __name__ == "__main__":
    Zadanie_Dodatkowe_1()
    #Zadanie_Dodatkowe_2()
    #Zadanie_Dodatkowe_3()
    pass