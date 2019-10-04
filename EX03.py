# Escreva um programa que receba do usuário 5 números inteiros e o nome do arquivo no qual eles devem ser armazenados.
# Em seguida, ler do arquivo estes valores armazenados copiando-os para um vetor de inteiros e imprimindo na tela.

nomeArquivo = input("Digite o nome do arquivo que vc quer salvar: ")

arquivo = open(f"C:\\Users\\ADS\\PycharmProjects\\Programacao2_Faculdade\\manipulacao_arquivos\\{nomeArquivo}.txt", 'w')

for i in range(5):
    arquivo.write(input("digite um número inteiro: "))
arquivo.close()

arquivo = open(f"C:\\Users\\ADS\\PycharmProjects\\Programacao2_Faculdade\\manipulacao_arquivos\\{nomeArquivo}.txt", 'r')

lista = []
for linha in arquivo:
    lista.append(linha)

print(lista)