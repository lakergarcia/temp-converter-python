print ('Convertidor de temperaturas')

# This is a function that allows the user to enter the value of the temperature.
n1 = int(input("introduce el valor de la temperatura: "))

# This is a menu that allows the user to choose the conversion they want to make.
opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    
    1) Convertir de Celcius a Fahrenheit
    2) Convertir de Fahrenheit a Celcius
    3) Convertir de Celcius a Kelvin 
    4) Convertir de Kelvin a Celcius
    5) Convertir de Fahrenheit a Kelvin
    6) Convertir de Kelvin a Fahrenheit
    7) Cambiar valor
    8) Apagar convertidor
    """)
    opcion = int(input("Elige una opción: "))     


# The above code is converting Celsius to Fahrenheit.
    if opcion == 1:
        c= n1
        fahrenheit = (c * 1.8) + 32
        resultado_f = round(fahrenheit, 2)
        print (" ")
        print ('{} °C equivalen a {} °F' .format(c, resultado_f))


# This is converting Fahrenheit to Celsius.
    elif opcion == 2:
        f= n1
        celcius = (f-32) * (5/9)
        resultado_c = round(celcius, 2)
        print(" ")
        print ('{} °F equivalen a {} °C' .format(f, resultado_c))


# This is converting Celsius to Kelvin.
    elif opcion == 3:

        c_to_k = n1
        kelvin = c_to_k + 273.15
        resultado_k = round(kelvin, 2)
        print(" ")
        print ('{} °C equivalen a {} K' .format(n1, resultado_k))


# This is converting Kelvin to Celsius.
    elif opcion == 4:
        k_to_c = n1
        celcius_k= k_to_c - 273.15
        resultado_k_to_c = round(celcius_k, 2)
        print(" ")
        print ('{} k equivalen a {} °C' .format(n1, resultado_k_to_c))


# This is converting Fahrenheit to Kelvin.
    elif opcion == 5: 
        f_to_k = n1
        f_to_kelvin = 5/9 * (f_to_k - 32) + 273.15
        resultado_f_to_k = round(f_to_kelvin, 2)
        print(" ")
        print ('{} °F equivalen a {} K' .format(n1, resultado_f_to_k))

    
# This is converting Kelvin to Fahrenheit.
    elif opcion == 6: 
        k_to_f = n1
        kelvin_to_f = (1.8) * (k_to_f - 273.15) + 32
        resultado_k_to_f = round(kelvin_to_f, 2)
        print(" ")
        print ('{} K equivalen a {} ºF' .format(k_to_f, resultado_k_to_f))


# This is a function that allows the user to change the value of the temperature.
    elif opcion == 7:
        n1 = int (input("Introduce el nuevo valor de temperatura: ") )


# This is a function that allows the user to exit the program.
    elif opcion == 8:
        print (' ')
        print ('HASTA PRONTO. Besitos :* Y no olvides tomar awita <3')
        break

# This is a function that allows the user to exit the program.
    else:
        print("Opción incorrecta")

# End of the program.