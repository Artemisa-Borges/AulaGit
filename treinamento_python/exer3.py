seq = input("Digite sua sequencia aqui: ")

arquivo = open("seq.fasta", "w")

arquivo.write(">seq")
arquivo.write(seq)

arquivo.close()