import psycopg2
import time
# dos for uno para el bloque y otro para toda la tabla

start_time = time.time() #begin clock


conn= psycopg2.connect(user ="informatica",database="base_volumen")
cur = conn.cursor()

size_block=10000000

cursor_psql='''
	BEGIN;
	declare mycur cursor for SELECT edad from personas1;
'''

fetch_psql='''
	fetch %s from mycur;
'''%size_block

commit_psql='''
	CLOSE mycur;
	COMMIT;
'''

cur.execute(cursor_psql)




arr_age=[0 for i in range(0,100)] #all age posible in the database

while True:
	try:
		cur.execute(fetch_psql)
		aux=int(cur.fetchone()[0])
		while True:
			try:
				arr_age[aux]+=1
				aux=int(cur.fetchone()[0])
			except:
				break
	except:
		break



cur.execute(commit_psql) # es necesario llamar a commit y a begin ?
conn.commit()
cur.close()
conn.close()

for i in range(0,len(arr_age)):
	print(i," -> ",arr_age[i])


print("--- %s seconds ---" % (time.time() - start_time), " Tamanio del bloque ", size_block)
