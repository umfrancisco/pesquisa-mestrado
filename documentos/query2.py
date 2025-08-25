import mysql.connector

# faz a conexão com sql
mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="1234",
    database="pesquisa"
)

mycursor = mydb.cursor()

# cria um contador
i = 0

# array para os títulos
title = [
    "[Local de detencao, quantidade de prontuários, porcentagem]",
    "[Ano de internacao, quantidade de prontuários]",
    "[Infracao, quantidade de prontuários, porcentagem excluindo não identificados]",
    "[Quantidade de prontuários da Penitenciária do Estado ou Cadeia Pública com infração de homicídio, porcentagem]",
    "[Quantidade de prontuários com infração não identificada agrupada por locais de detenção]",
    "[Quantidadde de prontuários com infração de homicídio agrupada por locais de detenção]",
    "[Prontuários excluindo Penitenciária do Estado, Cadeia Pública da Capital e Cadeia do interior]"
]

# array para as consultas
query = [
    "select local_detencao, count(*) as qtd, count(*)/(select count(*) from manicomio) from manicomio group by local_detencao order by qtd desc",
    "select data_entrada, count(*) from manicomio group by data_entrada",
    "select infracao, count(*), count(*)/(select count(*) from manicomio) from manicomio where not infracao = 'Não identificado' group by infracao",
    "select count(*), count(*)/(select count(*) from manicomio) from manicomio where local_detencao in('Penitenciária do Estado', 'Cadeia Pública da Capital') and infracao = 'Homicídio'",
    "select local_detencao, count(*) as qtd from manicomio where infracao = 'Não identificado' group by local_detencao order by qtd desc",
    "select local_detencao, count(*) as qtd from manicomio where infracao = 'Homicídio' group by local_detencao order by qtd desc",
    "select data_entrada, local_detencao, local_internacao, infracao from manicomio where not local_detencao in ('Penitenciária do Estado', 'Cadeia Pública da Capital', 'Cadeia do interior')"
]

# executa as consultas com os titulos
while (i < len(query)):
    print("#"+str(i+1)+" "+title[i])
    mycursor.execute(query[i])

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    i += 1
    print()
