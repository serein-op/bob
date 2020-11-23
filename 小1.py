import pandas
import csv, sqlite3
connect= sqlite3.connect("dbname.db")
cursor = connect.cursor()

df = pandas.read_csv(r'C:/Users/apple/Desktop/工作簿1.csv', encoding='gbk')
df.to_sql('tablename', connect, if_exists='append', index=False)
print('ok')
select_sql = "SELECT * FROM tablename"
cursor.execute(select_sql)
ret1 = cursor.fetchall()
print(ret1)


