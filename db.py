import pymysql
import passwords

__author__ = 'zunin'

class MySQL:
    def __init__(self):
        db_pass = passwords.Db_pass()
        db = pymysql.connect(host=db_pass.host,
                             user=db_pass.user,
                             passwd=db_pass.password,
                             db=db_pass.db)
        self.cur = db.cursor()

    def write_no_tag(self):
        self.cur.execute("SELECT ID FROM checkin")
        id = self.cur.fetchall()
        notag = "No Tag"
        print (notag)
        if notag not in id[0]:
            self.cur.execute("TRUNCATE TABLE `checkin`")
            self.cur.execute("INSERT INTO checkin(ID) VALUES('No Tag')")
        self.cur.close()

    def read_db(self):
        self.cur.execute("SELECT go FROM ready")
        go = self.cur.fetchall()
        print(go)

    
# TODO: Implement database code into class
"""
while True:
        serialin = ser.read(12)
        serialin = serialin[1:11]
        if len(serialin)==0:
                cur = db.cursor()
                cur.execute("SELECT ID FROM checkin")
                id = cur.fetchall()
                notag = "No Tag"
                print notag
                if notag not in id[0]:
                        cur.execute("TRUNCATE TABLE `checkin`")
                        cur.execute("INSERT INTO checkin(ID) VALUES('No Tag')")
                cur.close()
                while len(serialin) == 0:
                        tempin = ser.read(12)
                        serialin = tempin[1:11]
                        print "Taking a break!"
        else:
                cur = db.cursor()
                cur.execute("TRUNCATE TABLE `checkin`")
                cur.execute("INSERT INTO checkin(ID) VALUES(%s)",(serialin))
                print "You can now check-in"
                cur.close()
                while serialin == currentid:
                        tempin = ser.read(12)
                        serialin = tempin[1:11]
                        cur = db.cursor()
                        cur.execute("SELECT go FROM ready")
                        go = cur.fetchall()
                        gotag = "go"
                        if gotag in go[0]:
                                chain1()
                                sleep(5)
                                cur.execute("TRUNCATE TABLE `ready`")
                                cur.execute("INSERT INTO ready(go) VALUES('no go')")
                        print "The same tag is still on the check-in counter"

db.close()

"""