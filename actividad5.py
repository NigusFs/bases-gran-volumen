import psycopg2

conn= psycopg2.connect(user ="informatica",database="base_volumen")
cur = connection.cursor()

table=input("Ingrese el nombre de la tabla \n")
size_block=input()
sql='''
	SELECT edad from %s;
'''%table

cur.execute(sql)

size_element=50000000 # rows of the tables
size_block = 100000 if size_block ==" "  else size_block # check this comparation

= #rows whom be stored in ram 
arr_age=[0 for i in range(0,99)] #all age posible in the database

#while cur.fetchmany(size_block) !=[]: #stop when then is no more data
#	cur.fetchmany(size_block)


for i in range(0, size_element/size_element)
	i_age=cur.fetchmany(size_block)
	if cur.fetchmany(size_block) != []:
		arr_age[i_age]+=1
	else 
		break 


conn.commit()
cur.close()
conn.close()

for i in range(0,len(arr_age)-1)
	print(i," -> ",arr_age[i])