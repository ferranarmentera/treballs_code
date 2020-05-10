# primer programa
import random
myName = input('hola quin és el teu nom?   ')
print('encantat de coneixet, ' + myName,
      "Sabies que el teu nom té", len(myName), '  lletres ?')
myAge = input('Quants anys tens?  ')
print('molt bé!! que gran que ets!!!, saps que en tindras  ' +
      str(int(myAge) + 10) + '  en deu anys?')
myCollege = input('a quin col·legi vas? ')
print(myCollege, 'es un bon col·legi , ara veurem si éts una bona estudiant....')
print('ara farem unes proves:')
counter = 0
i = 0
while i < 5:
    i = i+1
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print('Quant fan', a, '*', b, '?')
    multipl = int(input())
    if multipl == a*b:
        print('correcte!')
    else:
        print('Incorrecte!')
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print('Quant fan', a, '/', b, '?')
    divi = int(input())
    if divi == a//b:
        print('correcte!')
    else:
        print('Incorrecte!')
