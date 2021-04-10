import mysql.connector as connector


def fetch_all(self):
	query="select * from customer"
	cur=self.cur.mycursor()
	cur.execute(qery)
	for row in cur:
		print(row)