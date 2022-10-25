def Zadanie_Dodatkowe_1():
    Funkcja = input("Podaj Funkcje: [a/b/c]: ")
    x = int(input("Podaj x: "))

    if Funkcja == "a":
        if x > 0:
            print(f"{2 * x}")
        elif x == 0:
            print(f"{0}")
        else:
            print(f"{-3 * x}")
    elif Funkcja == "b":
        if x >= 1:
            print(f"{x ** 2}")
        else:
            print(f"{x}")
    elif Funkcja == "c":
        if x > 2:
            print(f"{2 + x}")
        elif x == 2:
            print(f"{8}")
        else:
            print(f"{x - 4}")
    else:
        print("Zła Operacja!")

def Zadanie_Dodatkowe_2():
    a = int(input("a: "))
    b = int(input("b: "))
    print(f"{a}x + {b} = 0")
    x = b / a
    print(f"x: {x}")

def Zadanie_Dodatkowe_3():
    """
        Delta > 0:
            2   8   -10
        Delta = 0:
            1   2   1
        Delta < 0:
            1   2   3
    """
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    Delta = b ** 2 - 4*a*c

    if Delta > 0:
        print(f"x1: {(-b - MATH.sqrt(Delta))/(2*a)}\nx2: {(-b + MATH.sqrt(Delta))/(2*a)}")
    elif Delta == 0:
        print(f"x: {-b/2*a}")
    else:
        print("Brak Rozwiązań")

def Zadanie_Dodatkowe_4():
    Liczba_x = int(input("Liczba x: "))
    Liczba_y = int(input("Liczba y: "))
    Liczba_z = int(input("Liczba z: "))

    if Liczba_x > Liczba_y and Liczba_x > Liczba_z: # x _ _
        if Liczba_y > Liczba_z: # x y z
            print(f"{Liczba_x} {Liczba_y} {Liczba_z}")
        else: # x z y
            print(f"{Liczba_x} {Liczba_z} {Liczba_y}")

    elif Liczba_y > Liczba_x and Liczba_y > Liczba_z: # y _ _
        if Liczba_x > Liczba_z: # y x z
            print(f"{Liczba_y} {Liczba_x} {Liczba_z}")
        else: # y z x
            print(f"{Liczba_y} {Liczba_z} {Liczba_x}")

    elif Liczba_z > Liczba_x and Liczba_z > Liczba_y: # z _ _
        if Liczba_x > Liczba_y: # z x y
            print(f"{Liczba_z} {Liczba_x} {Liczba_y}")
        else: # z y x
            print(f"{Liczba_z} {Liczba_y} {Liczba_x}")

    else:
        print(f"{Liczba_x} {Liczba_y} {Liczba_z}") # x = y = z

def Zadanie_Dodatkowe_5():
    Deszcz = input("Czy Pada Deszcz: [y/n]: ")
    Autobus = input("Czy Jest Autobus: [y/n]: ")

    if Deszcz == "y":
        Deszcz = True
    else:
        Deszcz = False

    if Autobus == "y":
        Autobus = True
    else:
        Autobus = False

    print(f"Deszcz: {Deszcz}\nAutobus: {Autobus}")

    if Deszcz and Autobus: # True True
        print("Weź Parasol, Dostaniesz Się Na Uczelnie")
    elif Deszcz and not Autobus: # True False
        print("Nie Dostaniesz Się Na Uczelnie")
    elif not Deszcz and Autobus: # False True
        print("Dostaniesz Się Na Uczelnie, Miłego Dnia i Pięknej Pogody")

def Zadanie_Dodatkowe_6(): # DOKOŃCZYĆ
    print("Jaką Operację Chcesz Wykonać: \n1) Dodawanie\n2) Odejmowanie\n3) Mnożenie\n4) Dzielenie\n5) Potęgowanie\n6) Dzielenie z Resztą")

    Operacja = int(input("Operacja: "))
    Argument_1 = int(input("Podaj Argument #1: "))
    Argument_2 = int(input("Podaj Argument #2: "))

    if Operacja == 1:
        print(f"{Argument_1} + {Argument_2} = {Argument_1 + Argument_2}")
    elif Operacja == 2:
        print(f"{Argument_1} - {Argument_2} = {Argument_1 - Argument_2}")
    elif Operacja == 3:
        print(f"{Argument_1} * {Argument_2} = {Argument_1 * Argument_2}")
    elif Operacja == 4:
        if Argument_2 != 0:
            print(f"{Argument_1} / {Argument_2} = {Argument_1 / Argument_2}")
        else:
            print("ERROR: DZIELENIE PRZEZ 0")
    elif Operacja == 5:
        print(f"{Argument_1} ** {Argument_2} = {Argument_1 ** Argument_2}")
    elif Operacja == 6:
        if Argument_2 != 0:
            print(f"{Argument_1} % {Argument_2} = {Argument_1 % Argument_2}")
        else:
            print("ERROR: DZIELENIE PRZEZ 0")
    else:
        print("Zła Operacja!")
    pass

def Zadanie_Dodatkowe_7():
    Litera = input("Podaj Literę: ")

    if Litera.isupper():
        print(Litera.lower())
    else:
        print(Litera.upper())

# Main
if __name__ == "__main__":
    Zadanie_Dodatkowe_1()
    #Zadanie_Dodatkowe_2()
    #Zadanie_Dodatkowe_3()
    #Zadanie_Dodatkowe_4()
    #Zadanie_Dodatkowe_5()
    #Zadanie_Dodatkowe_6()
    #Zadanie_Dodatkowe_7()
    pass