import psycopg2

#conexion a la base de datos que esta en elephntsql
con = psycopg2.connect(
    host = 'queenie.db.elephantsql.com',
    database = 'ifgilvux',
    user = 'ifgilvux',
    password = 'MRUyQ-aHX7MHs_nHxahu98Yy0yaXEiGr',
)

def agregarCancion():
    cur = con.cursor()
    cur.execute('insert into cancion values (id, name, artist, genre, time, album, date, link)')
    #for
    cur.close


def albumesRecientes():
    cur = con.cursor()
    #ejecutar el query
    cur.execute('select username, pw, email from usuario')
    #imprimir los resultados de queries
    row = cur.fetchall()
    for r in row:
        print(f"{r[0]}, pw {r[1]}, email {r[2]}")


    #cerrar el query
    cur.close()
    #cerrar la conexion
    con.close()

