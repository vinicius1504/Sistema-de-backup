import paramiko
from datetime import datetime, timedelta
import os
import time
import sys


host = 'your_host'
user = 'your_username'
password = 'your_password'
pastaFtp = "/path/to/backup"

def backup():
    try:
        # Calculo da data
        data_prevista = datetime.now() - timedelta(days=1)
        data_formatada = data_prevista.strftime("%d-%m-%Y")

        # Gera a predefinição do nome
        arquivo_desejado = f'banco-{data_formatada}-1.zip'

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=user, password=password)

        # Entra na pasta desejada
        sftp = client.open_sftp()
        sftp.chdir(pastaFtp)

        print('====================')
        print('Um momento listando os arquivos')

        # Lista os arquivos da pasta
        arquivos = sftp.listdir()
        print('====================')
        print('📝 listando arquivos 📝')

        time.sleep(5)

        for arquivo in arquivos:
            print(f'-> {arquivo}')
        print('====================')

        # Caminho local do arquivo
        caminho_local = f"C:\\path\\to\\local\\backup{arquivo_desejado}"

        # Verifica se o arquivo já existe localmente
        if os.path.exists(caminho_local):
            print(f"""        
Arquivo Já consta na pasta destinada
                      
 -> 👍 Encerrando o sistema em alguns segundos 👍
=================================================================""")
            time.sleep(5)
            sys.exit()
        else:
            # Baixa o arquivo apenas se não existir localmente
            if arquivo_desejado in arquivos:
                caminho_remoto = f"{pastaFtp}/{arquivo_desejado}"
                sftp.get(caminho_remoto, caminho_local)
                print(f"""
✅ Arquivo Baixado com Sucesso ✅
                      
 ->  Encerrando o sistema em alguns segundos 
=================================================================""")
                time.sleep(5)
                sys.exit()
            else:
                print(f"""
 
❌ Não consta nenhum arquivo de backup ❌

                      
 -> Encerrando o sistema em alguns segundos 
=================================================================""")
                time.sleep(5)
                sys.exit()

    except Exception as e:
        # Handle any other errors
        mensagem_error = f"Erro durante o backup: {str(e)}"
        print(mensagem_error)

backup()
