import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()

db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="123",
    db="my_db"
)

c=db.cursor()
c.execute("INSERT INTO books (title, author, price, publisher, page_count) VALUES (%s, %s, 0, %s, 100);", ('Книга', 'Автор', 'Издание'))
db.commit()
c.close()
db.close()