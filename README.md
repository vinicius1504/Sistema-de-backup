   <h1>Backup Script</h1>
    <p>Este script realiza o backup de arquivos de um servidor remoto usando SFTP. Ele se conecta a um servidor remoto via SSH, verifica se um arquivo de backup específico já existe localmente, e se não existir, faz o download do arquivo.</p>

   <h2>Requisitos</h2>
    <ul>
        <li>Python 3.x</li>
        <li>Biblioteca <code>paramiko</code></li>
    </ul>

   <h2>Instalação</h2>
    <p>Primeiro, instale o <code>paramiko</code>:</p>
    <pre><code>pip install paramiko</code></pre>

 <h2>Configuração</h2>
    <p>Você precisa configurar os seguintes parâmetros no script:</p>
    <ul>
        <li><code>host</code>: o endereço do servidor remoto.</li>
        <li><code>user</code>: seu nome de usuário SSH.</li>
        <li><code>password</code>: sua senha SSH.</li>
        <li><code>pastaFtp</code>: o caminho no servidor remoto onde o arquivo de backup está localizado.</li>
        <li><code>caminho_local</code>: o caminho local onde o arquivo de backup será salvo.</li>
    </ul>

 <h2>Uso</h2>
    <p>1. Configure os parâmetros mencionados acima no script.<br>
    2. Execute o script:</p>
    <pre><code>python backup.py</code></pre>

 <h2>Funcionamento</h2>
    <p>O script segue os seguintes passos:</p>
    <ol>
        <li>Calcula a data do dia anterior e formata para o nome do arquivo de backup.</li>
        <li>Conecta-se ao servidor remoto via SSH usando <code>paramiko</code>.</li>
        <li>Navega até a pasta desejada no servidor.</li>
        <li>Lista os arquivos na pasta remota.</li>
        <li>Verifica se o arquivo de backup já existe localmente.</li>
        <li>Se o arquivo existir localmente, o script encerra.</li>
        <li>Se o arquivo não existir localmente, o script verifica se o arquivo está presente no servidor remoto e, em caso afirmativo, baixa o arquivo.</li>
        <li>Se o arquivo não for encontrado no servidor remoto, o script exibe uma mensagem de erro e encerra.</li>
    </ol>

   <h2>Exceções</h2>
    <p>O script captura exceções gerais durante o processo de backup e exibe uma mensagem de erro detalhada.</p>

  <h2>Exemplo de Saída</h2>
    <pre><code>====================
Um momento listando os arquivos
====================
📝 listando arquivos 📝
====================
-> banco-25-03-2024-1.zip
-> banco-26-03-2024-1.zip
====================

✅ Arquivo Baixado com Sucesso ✅
 ->  Encerrando o sistema em alguns segundos 
=================================================================
</code></pre>
</div>
</body>
