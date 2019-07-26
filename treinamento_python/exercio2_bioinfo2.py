'''w = open("Fabaceae.txt", "w")

w.write("As Fabaceae ou Leguminosae representam uma grande e economicamente importante família das Angiospermas, que inclui as vagens, ervilhas e feijões, por exemplo. Dentro das Fabaceae encontram-se tanto árvores e arbustos como plantas herbáceas perenes e/ou anuais. Essa família é normalmente reconhecida pela presença de frutos do tipo legume, [1] e pelas folhas compostas com estípulas. Leguminosae é uma das maiores famílias botânicas, de ampla distribuição geográfica, sendo a terceira maior família de plantas terrestres em número de espécies, atrás apenas de Orchidaceae e Asteraceae. incluem cerca de 751 gêneros e 19.000 espécies conhecidas [2][3][4] (7% das angiospermas[5]) sendo os 5 maiores gêneros: Astragalus (mais de 3.000 espécies), Acácia (mais de 1000 espécies), Indigofera (cerca de 700 espécies), Crotalaria (cerca de 700 espécies) e Mimosa (cerca de 500 espécies); esses gêneros abarcam cerca de um quarto de todas as espécies leguminosas.")


'''
name = input("Digite o nome do arquivo que vc deseja abrir: ")
arquivo = open(name, "r")

linhas = arquivo.read()
print(linhas.strip())

arquivo.close()


