#Idoia Muñoz Otero
#Crear un programa que lea los precios_munoz de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:

#Las cantidades totales de cada articulo.
#La cantidad de artículos en la sucursal 2.
#La cantidad del articulo 3 en la sucursal 1.
#La recaudación total de cada sucursal.
#La recaudación total de la empresa.
#La sucursal de mayor recaudación.

precios_munoz = []
cantidades_munoz = []
numarticulos_munoz = 3
numsucursales_munoz = 2

for indice_art in range(0, numarticulos_munoz):
   precios_munoz.append(float(input('Ingrese Precio Articulo %d:' % (indice_art+1))))




for indice_sucursal in range(0, numsucursales_munoz):
    cant_art = []
    for indice_art in range(0, numarticulos_munoz):
        cant_art.append(int(input('Ingrese Cant. de Articulo %d, en sucursal %d:' % (indice_art+1,indice_sucursal+1))))
    cantidades_munoz.append(cant_art)
   

print('cantidades_munoz por artículos:')
for indice_art in range(0, numarticulos_munoz):
    suma = 0
    for cant_sucursal in cantidades_munoz:
        suma = suma + cant_sucursal[indice_art]
    print('Total articulo %d: %d' % (indice_art + 1,suma))



print('Total Sucursal 2: %d' % sum(cantidades_munoz[1]))


print('Sucursal 1, Articulo 3: %d' % cantidades_munoz[0][2])


total_por_sucursal = []
for cant_sucursal in cantidades_munoz:
    total=0
    for precio,cantidad in zip(precios_munoz,cant_sucursal):
        total=total+precio*cantidad
    total_por_sucursal.append(total)

mayorrec = max(total_por_sucursal)   
indice_sucursal = 1
for indice_sucursal in range(0, numsucursales_munoz):
    print('Recaudaciones Sucursal %d: %f' % (indice_sucursal,total_por_sucursal[indice_sucursal]))
    indice_sucursal += 1


indice_sucursal = 1
for cant_sucursal in total_por_sucursal:
    if cant_sucursal == mayorrec: break
    indice_sucursal += 1

print('Recaudación total de la empresa: %f' % sum(total_por_sucursal))
print('Sucursal de Mayor Recaudación: %d' % indice_sucursal)
