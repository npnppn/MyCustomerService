import pymysql

conn = pymysql.connect(host = 'localhost', user = 'root', password = 'dgu1234!' ,db = 'lab5')
# host = DB주소(localhost 또는 ip주소), user = DB id, password = DB password, db = DB명
curs = conn.cursor()
curs.execute('call GetAvgofAge()') #프로시져  호출
rows = curs.fetchall()
for data in rows:
    print("-----Output of Procedure-----")
    print(data)
    
curs.execute('select get_id(37, "male")') #함수 호출
rows2 = curs.fetchall()
for data2 in rows2:
    print("-----Output of Function-----")
    print(data2)
