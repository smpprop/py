import mysql.connector
from mysql.connector import Error
class Employee:
    def connect(self):
        self.conn = mysql.connector.connect(host='localhost', database='employee', user='root', password='', port='3306')
        self.cur = self.conn.cursor()

    def InsertRec(self):
        for i in range(1):
            self.connect()
            print("Details of Employee ", i + 1)
            print()
            num = int(input("Enter Employee  number :  "))
            empname = input("Enter Employee name  :   ")
            sal = int(input("Enter Employee Salary  :  "))
            try:
                sql = 'INSERT INTO employee values ("%d","%s", "%d" )' % (num, empname, sal)
                self.cur.execute(sql)
                self.conn.commit()
            except Error as err:
                print(err)
            finally:
                self.conn.close()

    def viewAllRec(self):
        self.connect()
        try:
            self.cur.execute("select * from employee")
            rows = self.cur.fetchall()
            print("\nThe available records are \n")
            for r in rows:
                print(r)

            print('Total number of records fetched are = ', self.cur.rowcount)
        except Error as err:
            print(err)
        finally:
            self.conn.close()

    def viewSingleRec(self):
        self.connect()
        try:
            print("\nSearch record by Employee Number ")
            z = int(input("Enter Employee Number "))
            self.cur.execute("select * from employee where num = %d" % z)
            rows = self.cur.fetchall()
            tot_rec=self.cur.rowcount
            if tot_rec > 0 :
                for r in rows:
                    print(r)
            else:
                print("No matching records found ")
        except Error as err:
            print(err)
        finally:
            self.conn.close()

    def viewRecSalary(self):
        self.connect()
        try:
            print("\nSearch employee based on salary ")
            x = int(input("Enter Minimum salary  "))
            y = int(input("Enter Maximum salary  "))
            sql = "select * from  employee where sal between %d and %d " % (x,y)
            self.cur.execute(sql)
            rows = self.cur.fetchall()
            tot_rec = self.cur.rowcount

            if tot_rec > 0 :
                for r in rows:
                    print(r)
            else:
                print("No matching records found ")
        except mysql.connector.Error as error:
            print(error)
        finally:
            self.conn.close()

ch = 0
obj = Employee()
while ch!=5:
    print("1. Add Employee\n2. View All Employees\n3. View Single Employee\n4. View Employee based on salary\n5. Exit ")
    ch = int(input('\nEnter your choice ..'))
    if ch==1 :
        obj.InsertRec()
    elif ch == 2:
        obj.viewAllRec()
    elif ch == 3:
        obj.viewSingleRec()
    elif ch == 4:
        obj.viewRecSalary()
    elif ch == 5:
        print("Quitting... ")
    else:
        print("Invalid choice..")
