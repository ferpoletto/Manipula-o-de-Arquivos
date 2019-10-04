# Faça um programa que crie um arquivo contendo o nome de 5 pessoas, se o nome informado for igual ao seu nome crie outro arquivo
# somente com o seu nome.

exe02 = open("C:\\Users\\ADS\\PycharmProjects\\Programacao2_Faculdade\\manipulacao_arquivos\\exe02.txt", 'w')

MEUNOME = 'FERNANDO'

for i in range(5):
    nome = (input("Digite um nome: "))
    if nome == MEUNOME:
        meuNomeArquivo = open("C:\\Users\\ADS\\PycharmProjects\\Programacao2_Faculdade\\manipulacao_arquivos\\exe02MEUNOME.txt",'w')
        meuNomeArquivo.write(nome)
        meuNomeArquivo.close()
    else:
        exe02.write(nome)
        exe02.write("\n")

exe02.close()


