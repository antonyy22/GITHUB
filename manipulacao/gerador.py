from datetime import datetime


def gerar_logs():
    with open ('log.txt', 'w') as arquivos:
        for i in range (3):
            agora= datetime.now()
            arquivos.write(f' {agora} LOG {i+1} \n')
    print ('Log gerado com sucesso')


def main ():
    gerar_logs()

main ()