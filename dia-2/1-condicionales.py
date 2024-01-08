nombre = 'Roxana'
apellido = 'Rodriguez'

if nombre == 'Roxana' and apellido == 'Rodriguez':
    print('Hola Roxana, como están tus cuyes?')
else:
    print('Hola Roxana')

nombre_completo = nombre + ' ' + apellido
print(nombre_completo)

# recibir información por el teclado desde la terminal
ingreso = input()
print(ingreso)

dia = input('Ingrese el día de la semana: ').upper()
# Si el día es SABADO indicar que es fin de semana, caso contrario indicar que ese día se trabaja

if dia == 'SABADO':
    print('Es fin de semana')
elif dia == 'DOMINGO':
    print('Es fin de semana y hay que lavar la ropa')
else:
    print('Ese día se trabaja')