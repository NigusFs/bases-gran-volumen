import psycopg2
import time

start_time = time.time() #begin clock


conn= psycopg2.connect(user ="informatica",database="base_volumen")
cur = conn.cursor()


sql='''
	SELECT edad from personas1;
'''
cur.execute(sql)

arr_age=[0 for i in range(0,100)] #all age posible in the database


while True:
	try:
		arr_age[int(cur.fetchone()[0])]+=1
	except:
		break


conn.commit()
cur.close()
conn.close()

for i in range(0,len(arr_age)):
	print(i," -> ",arr_age[i])


print("--- %s seconds ---" % (time.time() - start_time))
