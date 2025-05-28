import mysql.connector
from mysql.connector import Error

class ElectricityBill:

    def connect(self):
        self.conn = mysql.connector.connect(host='localhost', database='student', user='root', password='', port=’3307’)
       self.cur = self.conn.cursor()

    def InsertRec(self):
        for i in range(1):
            self.connect()
            print("Details of Customer Electricity Bill ", i + 1)
            tariff = input("Enter Tariff  number :  (LT1, LT2) : ")
            custname = input("Enter Customer name  :   ")
            meter = int(input("Enter Meter Number  :  "))
            prv_read = int(input("Enter previous reading "))
            crn_read = int(input("Enter current reading "))

            if crn_read<=prv_read:
                print("Current reading should be more than the previous reading.. Please re-enter")
                prv_read = int(input("Enter previous reading "))
                crn_read = int(input("Enter current reading "))

            try:
                sql = 'INSERT INTO electricity values ("%s","%s", "%d", "%d", "%d" )' % (tariff, custname, meter, prv_read, crn_read)
                self.cur.execute(sql)
                self.conn.commit()
            except Error as err:
                print(err)
            finally:
                self.conn.close()

    def viewAllRec(self):
        self.connect()
        try:
            self.cur.execute("select * from Electricity")
            rows = self.cur.fetchall()
            print("\nThe available records are \n")
            for r in rows:
                print(r)
            print('Total number of records fetched are = ', self.cur.rowcount)
        except Error as err:
            print(err)
        finally:
            self.conn.close()

    def UpdateRec(self):
        self.connect()
        try:
            print("Updating customer record ")
            z = int(input("Enter Meter Number "))
            self.cur.execute("select * from Electricity where Meter_num = %d" % z)
            rows = self.cur.fetchall()
            tot_rec=self.cur.rowcount
            if tot_rec > 0 :
                for r in rows:
                    print(r)
                a3=int(input("Enter previous reading "))
                a4=int(input("Enter current reading "))
                self.cur.execute("Update Electricity set prv_read = %d, cur_read = %d where meter_num = %d" % (a3, a4,z))
                self.conn.commit()
            else:
                print("No matching records found ")
        except Error as err:
            print(err)
        finally:
            self.conn.close()

    def calcbill(self):
        self.connect()
        units = 0
        rate = 0.0
        try:
            print("Bill Calculation  ")
            y = int(input("Enter Meter number "))
            z = input("Enter Tariff Code ")
            sql="select * from Electricity where meter_num = %d and Tariff_code = '%s'" % (y, z)
            self.cur.execute(sql)
            rows = self.cur.fetchall()
            tot_rec = self.cur.rowcount
            if tot_rec > 0:
                for r in rows:
                    print(r)
                    units = r[4]-r[3]
            else:
                print("No matching records found ")

            if z == 'LT1':
                if units <= 30:
                    rate = units * 2.0
                elif units <= 100:
                    rate = 60 + ((units - 30) * 3.5)
                elif units <= 200 :
                    rate = 60 + 245 + ((units - 100) * 4.5)
                else:
                    rate = 60 + 245 + 450 + ((units - 200) * 5)

            elif z == 'LT2':
                if units <= 30:
                    rate = units * 3.5
                elif units <= 100:
                    rate = 105 + ((units - 30) * 5.0)
                elif units <= 200 :
                    rate = 105 + 350 + ((units - 100) * 6.0)
                else:
                    rate = 105 + 350 + 600 + ((units - 200) * 7.5)

            print ("\nUnits Consumed = ", units, " and Amount payable = ", rate)

        except Error as err:
            print(err)
        finally:
            self.conn.close()

obj = ElectricityBill()
ch = 0
while ch!=5:
    print("1. Add New customer\n2. View All Records\n3. Update Record\n4. Calculate Bill \n5. Exit ")
    ch = int(input('\nEnter your choice ..'))
    if ch==1 :
        obj.InsertRec()
    elif ch == 2:
        obj.viewAllRec()
    elif ch == 3:
        obj.UpdateRec()
    elif ch == 4:
        obj.calcbill()
    elif ch == 5:
        print("Quitting... ")
    else:
        print("Invalid choice..")
