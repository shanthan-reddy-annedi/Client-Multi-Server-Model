import mysql.connector
from mysql.connector import errorcode

class Mysql:
    def __init__(self, user, password):
        try:
            self.password = password
            self.user = user
            self.mydb = mysql.connector.connect(host='localhost',
                                           user=self.user,
                                           passwd=self.password,
                                           database="employee")
            self.succeed = True
            self.cursor = self.mydb.cursor()

        except mysql.connector.Error as err:
            self.succeed = False
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                pass

            else:
                print(err)

    def getTeacherId(self, user, passw):
        quary = f"SELECT teacher_id from user WHERE username='{user}' AND pass='{passw}'"

        self.cursor.execute(quary)
        data = self.cursor.fetchall()
        try:
            return data[0]
        except IndexError:
            return False

    def getTeacherIncome(self, id):
        quary = f"SELECT income,name from teacher WHERE id={id}"

        self.cursor.execute(quary)
        data = self.cursor.fetchall()
        try:
            return data[0]
        except IndexError:
            return False