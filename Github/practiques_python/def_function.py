

# tolerance calculator considers the material and level of precicion of the parts
# variables definition quality leve
coarsev = 0.0075
mediumv = 0.005
highv = 0.003
POR = 0.003
# uservalue = float(input("enter the dimension value  "))
# uservalue_quality = input("Enter the quality level : coarse ,medium , high ")
# if uservalue_quality == "coarse":
#     uservalueq = coarsev
# elif uservalue_quality == "medium":
#     uservalueq = mediumv
# elif uservalue_quality == "high":
#     uservalueq = highv


def tolerance_calc(value1, value2):
    if value2 == "coarse":
        print("toleance range is:", value1 * coarsev)
    elif value2 == "medium":
        print("toleance range is:", value1 * mediumv)
    elif value2 == "high":
        print("toleance range is:", value1 * highv)


print("No values entered")

tolerance_calc(float(input("enter the dimension value  ")),  input(
    "Enter the quality level : coarse ,medium , high "))


def iva():
    '''función básica para el calculo del IVA'''
    iva = 12
    costo = input('¿Cual es el monto a calcular?: ')
    calculo = costo * iva / 100
    print "El calculo de IVA es: " + str(calculo) + "\n"
