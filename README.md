Backup Script
Este script realiza o backup de arquivos de um servidor remoto usando SFTP. Ele se conecta a um servidor remoto via SSH, verifica se um arquivo de backup específico já existe localmente, e se não existir, faz o download do arquivo.

Requisitos
Python 3.x
Biblioteca paramiko
Instalação
Primeiro, instale o paramiko:

bash
Copiar código
pip install paramiko
Configuração
Você precisa configurar os seguintes parâmetros no script:

host: o endereço do servidor remoto.
user: seu nome de usuário SSH.
password: sua senha SSH.
pastaFtp: o caminho no servidor remoto onde o arquivo de backup está localizado.
caminho_local: o caminho local onde o arquivo de backup será salvo.
Uso
Configure os parâmetros mencionados acima no script.
Execute o script:
bash
Copiar código
python backup.py
Funcionamento
O script segue os seguintes passos:

Calcula a data do dia anterior e formata para o nome do arquivo de backup.
Conecta-se ao servidor remoto via SSH usando paramiko.
Navega até a pasta desejada no servidor.
Lista os arquivos na pasta remota.
Verifica se o arquivo de backup já existe localmente.
Se o arquivo existir localmente, o script encerra.
Se o arquivo não existir localmente, o script verifica se o arquivo está presente no servidor remoto e, em caso afirmativo, baixa o arquivo.
Se o arquivo não for encontrado no servidor remoto, o script exibe uma mensagem de erro e encerra.
