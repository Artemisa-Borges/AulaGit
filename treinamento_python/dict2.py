dic = {"nome": "Artemisa", "idade":"29", "sexo":"feminino"}

'''print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())'''

'''for k,v in dic.items():
	print (k)'''

Estados = []


estado1 = {"uf": "Piaui", "sigla": "PI"}
estado2 = {"uf": "Maranhao", "sigla": "MA"}

Estados.append(estado1)
Estados.append(estado2)
print(Estados)

print(Estados[1]["uf"])