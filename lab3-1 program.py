import pymysql

conn = pymysql.connect(host = 'localhost', user = 'root', password = 'dgu1234!' ,db = 'lab5')
# host = DB주소(localhost 또는 ip주소), user = DB id, password = DB password, db = DB명
curs = conn.cursor()

sql1 = "select team_id from team where task = some(select task from support where task = %s);"
curs.execute(sql1, ('online'))
print("//////////////sql1////////////////")
print('sql1 : "select team_id from team where task = some(select task from support where task = %s);"')
result1 = curs.fetchall()
for i in result1:
    print(i)

sql2 = "select avg(budget) from team where task = some(select task from support where location = %s) group by task;"
curs.execute(sql2, ('Hong kong'))
print("//////////////sql2////////////////")
print('"select avg(budget) from team\
where task = some(select task from support\
where location = %s)\
group by task;"')
result2 = curs.fetchall()
for i in result2:
    print(i)

sql3 = "select employee_id, name from employee where team_id = some (select team_id from team as T, Support as P where T.task = P.task and P.location = %s);"
curs.execute(sql3, ('Hong kong'))
print("//////////////sql3////////////////")
print('"select employee_id, name from employee where team_id = some (select team_id from team as T, Support as P where T.task = P.task and P.location = %s);"')
result3 = curs.fetchall()
for i in result3:
    print(i)
print("//////////////sql4////////////////")
print('"select task, budget from team where budget < some(select avg(budget) from team);"')
sql4 = "select task, budget from team where budget < some(select avg(budget) from team);"
curs.execute(sql4)

result4 = curs.fetchall()
for i in result4:
    print(i)
