# Faça a tabuada de 1 até 10 e salve cada uma em um arquivo, depois leia e mostre na tela

for i in range(1,11):
    nome = (f'tabuada do {i}')
    arquivo = open(f"C:\\Users\\ADS\\PycharmProjects\\Programacao2_Faculdade\\manipulacao_arquivos\\tabuada\\{nome}.txt", 'w')
    arquivo.write(f'tabuada do {i}\n')
    for j in range(1, 11):
        arquivo.write(f'{i}X{j}={i*j}')
        arquivo.write('\n')
    arquivo.close()
