escolha = int(input(" Digite 1 para ler arquivo \n Digite 2 para imprimir o conteudo \n Digite 3 para sair \n "))

if escolha == 1:
	arquivo = open("msn.txt", "r")
	
elif escolha == 2:
	arquivo = open("msn.txt", "r")
	linhas = arquivo.read()

	print(linhas.strip())

	arquivo.close()

elif escolha == 3:
	arquivo = open("msn.txt", "r")

	arquivo.close