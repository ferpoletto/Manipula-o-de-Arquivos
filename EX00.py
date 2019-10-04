arquivo = open("C:\\Users\\ADS\\PycharmProjects\\Programacao2_Faculdade\\manipulacao_arquivos\\TestTXT2.txt", 'w')

arquivo.write("Primeira linha. \n")

arquivo.write("Segunda linha. \n")

arquivo.write("Terceira e última linha.")

arquivo.close()

arquivo = open("C:\\Users\\ADS\\PycharmProjects\\Programacao2_Faculdade\\manipulacao_arquivos\\TestTXT2.txt", 'r')

for linha in arquivo:
    print(linha)

arquivo.close()

