#Ejercicio 1  Sistema mesón CineDUOC

total = 0

#bienvenida y nombre
print ('Bienvenido al Mesón de venta de boletos y agregados de CineDUOC.')
nombre = input('¿Cuál es tu nombre? ')

#Saludo y corroborar afiliación a DUOC
print ('\nHola, '+nombre+'. \n ¿Perteneces a DUOC como estudiante o funcionario? ')
print ('1. Pertenece \n2. No Pertenece')
duoc = int(input ('Escribe un número: '))

# Tipo de Entrada y cantidad
print ('\n¿Qué tipo de entrada quieres comprar '+nombre+'?')
print ('1. Estreno \n2. Normal')
entrada = int(input ('Escribe un número: '))
cantidad = int(input('¿Cuántas entradas quieres comprar '+nombre+'? '))

if entrada == 1:
  total = total + (4800*cantidad) #precio estreno 4800
else:
  total = total + (2900*cantidad) #precio normal 2900


#descuento DUOC 30% automático a entradas sólamente, round() para eliminar decimales
if duoc == 1:
  total = round(total*0.7)



# Palomitas
print ('\n¿Te gustaría comprar palomitas '+nombre+'?')
print ('1. Si \n2. No')
palomitas = int(input ('Escribe un número: '))

if palomitas == 1:
  print ('\n¿Qué tamaño de palomitas quieres?')
  print ('1. Pequeñas \n2. Medianas \n3. Grandes')
  t_palomitas = int(input('Escribe un número: '))
  print ('\n¿Cuántas palomitas quieres?')
  n_palomitas = int(input('Escribe el número: '))

  if t_palomitas ==1:
      total = total + (2500*n_palomitas) # precio palomitas pequeñas 2500
  elif t_palomitas ==2:
      total = total + (4500*n_palomitas) # precio palomitas medianas 4500
  else:
      total = total + (7800*n_palomitas) # precio palomitas grandes 7800
else:
  total = total + 0


# Bebida
print ('\n¿Te gustaría agregar bebidas '+nombre+'?')
print ('1. Si \n2. No')
bebidas = int(input ('Escribe un número: '))

if bebidas == 1:
  print ('\n¿Qué tamaño de bebida quieres?')
  print ('1. Pequeñas \n2. Medianas \n3. Grandes')
  t_bebida = int(input('Escribe un número: '))
  print ('\n¿Cuántas bebidas quieres?')
  n_bebidas = int(input('Escribe el número: '))

  if t_bebida ==1:
      total = total + (1000*n_bebidas) # precio bebida pequeña 1000
  elif t_bebida ==2:
      total = total + (1250*n_bebidas) # precio bebida mediana 1250
  else:
      total = total + (2000*n_bebidas) # precio bebida grande 2000
else:
  total = total + 0


#Mostrar Total, solicitar efectivo y mostrar vuelto

print(nombre+', el total a pagar es de: ', total,' pesos.')
efectivo = int(input('Ingresa el total de efectivo: '))
vuelto = efectivo - total
if vuelto > 0:
  print ('Tu vuelto es de: ', vuelto, ' pesos.')
elif vuelto == 0:
  print ('No corresponde vuelto.')
else:
  print('Faltan ', vuelto , ' pesos para pagar el total.')
