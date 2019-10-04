arquivo = open("C:\\Users\\ADS\\PycharmProjects\\Programacao2_Faculdade\\manipulacao_arquivos\\dezNomes.txt", 'w')

for i in range(3):
    arquivo.write(input("Digite um nome: "))
    arquivo.write("\n")
arquivo.close()

arquivo = open("C:\\Users\\ADS\\PycharmProjects\\Programacao2_Faculdade\\manipulacao_arquivos\\dezNomes.txt", 'r')

for linha in arquivo:
    if 'Gisele' in linha:
        print('Achei')

arquivo.close()
