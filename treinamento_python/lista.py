minha_lista = ["abacaxi", "melancias", "abacate"]
minha_lista2 = [1, 2, 3, 4, 5]
minha_lista3 = ["abacaxi", 2, 9, 89, True]

print (minha_lista)

print (minha_lista[0:2])

for i in minha_lista:
	print (i)

tamanho =  len(minha_lista)
print (tamanho)

minha_lista.append("acerola")
print ( minha_lista)

if 7 in minha_lista2:
	print("Sete esta na minha lista")
else:
	print("Sete nao esta na minha lista")