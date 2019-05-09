#! /usr/bin/env python
import MySQLdb

host = "localhost"
passwd = ""
user = "root"
dbname = "photogallery"

db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=dbname)
cursor = db.cursor()

cursor.execute("ALTER DATABASE `%s` CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_bin'" % dbname)

sql = "SELECT DISTINCT(table_name) FROM information_schema.columns WHERE table_schema = '%s'" % dbname
cursor.execute(sql)

results = cursor.fetchall()

for row in results:
  if 'archived' in row[0]:
    continue
  sql = "ALTER TABLE `%s` convert to character set DEFAULT COLLATE DEFAULT" % (row[0])
  cursor.execute(sql)
db.close()
