import mysql.connector
from mysql.connector import Error

def testar_conexao():
    print("Iniciando tentativa de conexão com a nuvem...")
    
    try:
        conexao = mysql.connector.connect(
            host="mysql-146c2569-mysql-raiteis.d.aivencloud.com",
            port=19137, 
            user="avnadmin",
            password="AVNS_ND3_i1H_zo4j-t4GV9J",
            database="raiteis",
            
            client_flags=[mysql.connector.ClientFlag.SSL],
            ssl_ca="ca.pem" 
        )

        if conexao.is_connected():
            print("✅ SUCESSO: Sistema RAITEis conectado ao banco de dados MySQL!")
            return conexao

    except Error as erro_banco:
        print(f"❌ ERRO: Não foi possível conectar. Detalhes: {erro_banco}")
        return None

conexao_ativa = testar_conexao()

if conexao_ativa:
    conexao_ativa.close()
    print("Conexão encerrada com segurança após o teste.")
