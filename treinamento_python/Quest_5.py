name = input("Digite o nome do arquivo aqui: ")

arquivo = open(name)

linhas = arquivo.readlines()
multifasta = {}

for linha in linhas:
	if linha[0] == ">":
		seq_atual = linha.strip()
		multifasta[seq_atual] = ""
	else: 
		multifasta[seq_atual] = multifasta[seq_atual]+linha.strip()
print (multifasta)

