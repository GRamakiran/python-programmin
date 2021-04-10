import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="root",
	database="python"
	)
	
mycursor = mydb.cursor()

'''mycursor.execute("CREATE TABLE customer(name VARCHAR(225),address VARCHAR(255))")
sql = "INSERT INTO customer (name,address) VALUES (%s,%s)"
val=("Raj","Chennai")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")'''

print(sql="select * from customer")