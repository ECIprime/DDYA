def main():

    print("Se le pedirá un número del cual se le darán ciertos datos de sí mismo\ny a continuación, se le pedirá un segundo número donde se hará un nuevo proceso junto con el anterior.")

    num1 = None

    while type(num1) != int:

        try:

            num1 = int(input("\nIngrese el primer número:"))

        except Exception:

            print("\nError, ingrese un número entero válido.")

                

    if num1 < 0:

        print("El número ingresado es negativo.")

    elif num1 > 0:

        print("El número ingresado es positivo.")

    else:

        print("El número ingresado es 0.")

    if num1%2 != 0:

        print("El número ingresado es impar.")

    else:

        print("El número ingresado es par.")

    sucesion = 2

    fibonacci = [0,1]

    haceparte = False

    lastfibo = None

    if num1 != 0 or num1 != 1:

        while lastfibo == None or lastfibo <= num1:

            fibonacci.append(fibonacci[sucesion-2] + fibonacci[sucesion-1])

            lastfibo = fibonacci[sucesion]

            if lastfibo == num1:

                haceparte = True

                print("El número ingresado hace parte de la serie de Fibonacci.")

                break

            sucesion += 1

    else:

        print("El número ingresado hace parte de la serie de Fibonacci.")
                

        

    if haceparte == False:

        print("El número ingresado no hace parte de la serie de Fibonacci.")

main()
