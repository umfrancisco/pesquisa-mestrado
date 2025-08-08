import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="1234",
    database="pesquisa"
)

mycursor = mydb.cursor()
i = 1927

print("Seleção de detentos da Penitenciária do Estado ou Cadeia Pública da Capital processados por Homicídio:")
while (i < 1934):
    print("Detento de "+str(i)+":")
    mycursor.execute("select id_documento, id_caixa, local_detencao, infracao from manicomio where data_entrada = "+str(i)+" and local_detencao in('Penitenciária do Estado', 'Cadeia Pública da Capital') and infracao = 'Homicídio' order by local_detencao desc limit 1")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    i += 1
    print("")

j = 1927

while (j < 1934):
    print("Detenção em "+str(j)+":")
    mycursor.execute("select local_detencao, count(*) from manicomio where data_entrada = "+str(j)+" group by local_detencao")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    j += 1
    print("")
    
k = 1927

while (k < 1934):
    print("Internação em "+str(k)+":")
    mycursor.execute("select local_internacao, count(*) from manicomio where data_entrada = "+str(k)+" group by local_internacao")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    k += 1
    print("")
 
l = 1927
   
while (l < 1934):
    print("Infrações em "+str(l)+":")
    mycursor.execute("select infracao, count(*) from manicomio where data_entrada = "+str(l)+" group by infracao")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    l += 1
    print("")    
       
m = 1927

while (m < 1934):
    print("Detenção por homicídio em "+str(m)+":")
    mycursor.execute("select local_detencao, count(*) from manicomio where data_entrada = "+str(m)+" and infracao = 'Homicídio' group by local_detencao")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    m += 1
    print("")