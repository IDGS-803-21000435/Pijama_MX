from io import open

archivo_texto=open('nombres.txt', 'a+')

archivo_texto.write('\n peli')

for lines in archivo_texto.readlines():
    print(lines.rstrip())


print(archivo_texto.read())

archivo_texto.seek(10)# para establecer en que lugar iniciara el puntero

print(archivo_texto.read())

archivo_texto.close()