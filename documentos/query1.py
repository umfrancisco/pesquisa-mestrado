import mysql.connector

# faz a conexão com o banco de dados sql
mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="1234",
    database="pesquisa"
)

mycursor = mydb.cursor()

# cria um contador
i = 1927

# titulo da consulta
print("# Seleção de prontuários para a etapa qualitativa:\n")

# faz uma seleção de sete prontuários segundo os critérios estabelecidos pela consulta
while (i < 1934):
    print("Detento de "+str(i)+":")
    print("[id documento, id caixa, local detencao, infracao]")
    mycursor.execute("select id_documento, id_caixa, local_detencao, infracao from manicomio where data_entrada = "+str(i)+" and local_detencao in('Penitenciária do Estado', 'Cadeia Pública da Capital') and infracao = 'Homicídio' order by local_detencao desc limit 1")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    i += 1
    print()
