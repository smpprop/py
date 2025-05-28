import mysql.connector
from mysql.connector import Error

class Student:

    def connect(self):
        self.conn = mysql.connector.connect(host='localhost', database='student', user='root', password='', port=3306)
        self.cur = self.conn.cursor()

    def InsertRec(self):
        for i in range(1):
            self.connect()
            print("Details of Student ", i + 1)
            reg = int(input("Enter Student Registration number :  "))
            stname = input("Enter student name  :   ")
            m1 = int(input("Enter marks in First subject  :  "))
            m2 = int(input("Enter marks in Second subject :  "))
            m3 = int(input("Enter marks in Third subject  :  "))
            try:
                sql = 'INSERT INTO Std_Marks values ("%d","%s", "%d", "%d", "%d" )' % (reg, stname, m1, m2, m3)
                self.cur.execute(sql)
                self.conn.commit()
            except Error as err:
                print(err)
            finally:
                self.conn.close()

    def viewRec(self):
        self.connect()
        try:
            self.cur.execute("select * from Std_Marks")
            rows = self.cur.fetchall()
            print("\nThe available records are \n")
            for r in rows:
                print(r)
            print('Total number of records fetched are = ', self.cur.rowcount)
        except Error as err:
            print(err)
        finally:
            self.conn.close()

    def delRec(self):
        self.connect()
        try:
            z = int(input("Enter student registration number to delete"))
            sql = "delete from Std_Marks where Reg = %d " % z
            self.cur.execute(sql)
            records = self.cur.rowcount
            self.conn.commit()
            if records > 0:
                print("Record Deleted successfully.")
                self.viewRec()
            else:
                print("Registration number could not be found")
        except mysql.connector.Error as error:
            print(error)
        finally:
            self.conn.close()

obj = Student()
obj.InsertRec()
obj.viewRec()
obj.delRec()
