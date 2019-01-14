import mysql.connector
from mysql.connector import errorcode


class ConnectMySQL:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.con = mysql.connector.connect()


    def getInformation(self):
        print("Host : ", self.host)
        print("Database :", self.database)
        print("User :" ,self.user)
        print("Password :", self.password)

        MySqlInformation = {
            "Host": self.host,                
            "Database" : self.database,
            "User ": self.user,
            "Password": self.password
            }

        return MySqlInformation


    def setConfig(self):
        try:
            self.con = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database,
                auth_plugin="mysql_native_password"
            )
            print(self.con)
            if self.con.is_connected():
                print("Success Connect")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)


    def setTable(self, query):
        try:
            myCursor = self.con.cursor()
            myCursor.execute(query)
            print("Create a table")
        except mysql.connector.DatabaseError as err:
            if(err.errno == errorcode.ER_ACCESS_DENIED_ERROR):
                print("Access denied error")
            else:
                print(err)

        myCursor.close()

    def insertData(self, query, val):
        try:
            myCursor = self.con.cursor()


            #For Example
            #sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
            #val = ("John", "Highway 21")

            if type(val) == "<class 'list'>":
                myCursor.executemany()
            else:
                myCursor.execute(query,val)

            self.con.commit()
            print(myCursor.rowcount, "saved row")
            return True
        except:
            print("ERROR INSTERT_DATA")

        myCursor.close()
        return False

    def selectData(self, query):
        myCursor = self.con.cursor()

        myCursor.execute(query)

        myresult = myCursor.fetchall()
        #fetchone just one column for :)
        resultList = []
        for x in myresult:
            resultList.append(x)

        myCursor.close()
        return resultList


    def readCommend(self, query):
        try:
            myCursor = self.con.cursor()
            myCursor.execute(query)
            print("Is coming")
            print(myCursor.rowcount, "record(s) deleted or affected")
        
        except :
            print("ERROR")

        
        myCursor.close
        return True

    def CLOSE_CON(self):
        self.con.close
        del self.con

        #Countine