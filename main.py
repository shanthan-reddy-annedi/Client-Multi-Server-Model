import testdb

conn = testdb.Mysql("root",'83355806')
try:
    print(conn.getTeacherId('shanthan', '83355806')[0])
except TypeError:
    print("wrong User")