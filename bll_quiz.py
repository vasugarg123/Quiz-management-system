import pymysql
import re
con=pymysql.connect(host="localhost",user="vasu@123",password="admin123",database="test")
try:
    mycursor=con.cursor()
    # qry="use erp"
    # mycursor.execute(qry)
    con.commit()
except Exception as err:
        con.rollback()
        print("error found:",err)


#<------------------------------------ADMIN VIEW STARTS HERE-------------------------->

class admin:
    try:
        def __init__(self):
            self.uname=""
            self.pwd=""

        def check_adminUname(self):
            qry = "select admin_uname from admin_details"
            mycursor.execute(qry)
            con.commit()
            mydata = mycursor.fetchall()
            for e in mydata:
                if (e[0] == self.uname):
                    return False
            return True


        def add_admin(self):
                if(len(self.uname)>=5 and len(self.uname)<=10 and len(self.pwd)>=5 and len(self.pwd)<=10):
                    pattern=re.compile("[\w@#]+")
                    match1=re.match(pattern,self.uname)
                    match2 = re.match(pattern, self.pwd)
                    if match1 and match2:

                        qry="insert into admin_details values('%s','%s')"%(self.uname,self.pwd)
                        mycursor.execute(qry)
                        con.commit()
                        return True
                    else:
                        return False
                else:
                    return False


        def delete_admin(self):
            qry="delete from admin_details where admin_uname=('%s') and admin_pwd=('%s')"%(self.uname,self.pwd)
            line = mycursor.execute(qry)
            con.commit()
            if (line != 0):
                return True
            else:
                return False

        @staticmethod
        def display():
            qry = "select * from admin_details"
            mycursor.execute(qry)
            con.commit()
            mydata = mycursor.fetchall()
            if (len(mydata) == 0):
                return False
            else:
                return mydata


    except Exception as err:
        con.rollback()
        print("error found:", err)

class user:
    try:
        def __init__(self):
            self.uname=""
            self.mob_no=""
            self.email=""


        def search_user(self,mode):
             qry=""
             if(mode==1):
                 qry="select * from user_details where user_uname=('%s')"%(self.uname)

             elif(mode==2):
                 qry = "select * from user_details where user_email=('%s')" % (self.email)

             elif (mode==3):
                 qry = "select * from user_details where user_mob_no=('%s')" % (self.mob_no)


             mycursor.execute(qry)
             mydata = mycursor.fetchall()
             con.commit()
             if (len(mydata) != 0):
                 return mydata
             else:
                 return False


        @staticmethod
        def display():
            qry="select * from user_details"
            mycursor.execute(qry)
            con.commit()
            mydata=mycursor.fetchall()
            if(len(mydata)==0):
                return False
            else:
                return mydata

    except Exception as err:
            print("error found:", err)


class quiz_details:
    try:
        def __init__(self):
            self.ques_id=""
            self.ques=""
            self.option1=""
            self.option2= ""
            self.option3 = ""
            self.option4 = ""
            self.ans=""
            self.posMarks=""
            self.negMarks=""
            self.level=""
            self.module=""


        def check_inputs(self):
            # ques id
            if(len(self.ques_id)==4):
                pattern = re.compile("\w{4}", re.IGNORECASE)
                match = re.match(pattern, self.ques_id)
                if match:
                    qry = "select ques_id from quiz_details"
                    mycursor.execute(qry)
                    mydata = mycursor.fetchall()
                    for e in mydata:
                        if (e[0] == self.ques_id):
                            return "exists"
                else:
                    return "invalid ques id"
            else:
                return "invalid ques id"

            # ques
            pattern = re.compile("[\w\s]+")
            match = re.match(pattern, self.ques)
            if match:
                pass
            else:
                return "invalid ques"

            # option1
            pattern = re.compile("[\w\s]+")
            match = re.match(pattern, self.option1)
            if match:
                pass
            else:
                return "invalid option1"

            # option2
            pattern = re.compile("[\w\s]+")
            match = re.match(pattern, self.option2)
            if match:
                pass
            else:
                return "invalid option2"

            # option3
            pattern = re.compile("[\w\s]+")
            match = re.match(pattern, self.option3)
            if match:
                pass
            else:
                return "invalid option3"

            # option4
            pattern = re.compile("[\w\s]+")
            match = re.match(pattern, self.option4)
            if match:
                pass
            else:
                return "invalid option4"

            # answer
            pattern = re.compile("[\w\s]+")
            match = re.match(pattern, self.ans)
            if match:
                pass
            else:
                return "invalid answer"

            # positive Marks
            pattern = re.compile("\d+")
            match = re.match(pattern, self.posMarks)
            if match:
                pass
            else:
                return "invalid posMarks"

            # negative Marks
            pattern = re.compile("\d+")
            match = re.match(pattern, self.negMarks)
            if match:
                pass
            else:
                return "invalid negMarks"

            return True

        def add_ques(self):

            qry = "insert into quiz_details values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                self.ques_id, self.ques, self.option1, self.option2 ,self.option3, self.option4, self.ans,self.posMarks,self.negMarks,self.level,self.module)

            mycursor.execute(qry)
            con.commit()

        def search_ques(self):
                qry = "select * from quiz_details where ques_id=('%s')" % (self.ques_id)
                mycursor.execute(qry)
                mydata = mycursor.fetchall()
                if (len(mydata) == 0):
                    return False
                else:
                    return mydata[0]


        def delete_ques(self):
            qry="delete from quiz_details where ques_id=('%s')"%(self.ques_id)
            line=mycursor.execute(qry)
            con.commit()
            if(line!=0):
                return True
            else:
                return False

        # def modify_ques(self):
        #
        #     qry = "update quiz_details set where ques_id=('%s')" % (
        #         self.ques, self.option1, self.option2, self.option3, self.option4, self.ans,
        #         self.posMarks, self.negMarks, self.level,self.ques_id)
        #
        #     mycursor.execute(qry)
        #     con.commit()
        #     return True

        #display all
        @staticmethod
        def display():
            qry = "select * from quiz_details"
            mycursor.execute(qry)
            con.commit()
            mydata = mycursor.fetchall()
            if (len(mydata) == 0):
                return False
            else:
                return mydata

    except Exception as err:
        print("error found:", err)

# <----------------------ADMIN VIEW ENDS HERE------------------------------------------------>


#<------------------------USER VIEW STARTS HERE--------------------------------------------->

class login:

    def __init__(self):
        self.uname=""
        self.pwd=""

    def find_admin(self):
        qry = "select admin_uname,admin_pwd from admin_details"
        mycursor.execute(qry)
        con.commit()
        mydata = mycursor.fetchall()
        for e in mydata:
            if (e[0] == self.uname and e[1] == self.pwd):
                return True
        return False

    def find_user(self):
        qry = "select user_uname,user_pwd from user_details"
        mycursor.execute(qry)
        con.commit()
        mydata = mycursor.fetchall()
        for e in mydata:
            if (e[0] == self.uname and e[1] == self.pwd):
                return True
        return False

class signUp:

    def __init__(self):
        self.uname=""
        self.pwd=""
        self.email=""

    def check_inputs(self):

        # email
        pattern = re.compile("[\w.]+@[a-z]+\.[a-z]{3}")
        match = re.match(pattern, self.email)
        if match:
            pass
        else:
            return "invalid email"

        #user uname
        if(len(self.uname)>=5 and len(self.uname)<=10):
            pattern=re.compile("[\w@#]+")
            match=re.match(pattern,self.uname)
            if match:
                pass
            else:
                return "invalid uname"
        else:
            return "invalid uname"

        #password
        if (len(self.pwd) >= 5 and len(self.pwd) <= 10):
            pattern = re.compile("[\w@#]+")
            match = re.match(pattern, self.pwd)
            if match:
                pass
            else:
                return "invalid pwd"
        else:
            return "invalid pwd"

        return True

    def check_email(self):
        qry = "select user_email from user_details"
        mycursor.execute(qry)
        con.commit()
        mydata = mycursor.fetchall()
        for e in mydata:
            if (e[0] == self.email):
                return "exists"
        return True

    def check_uname(self):
        qry = "select user_uname from user_details"
        mycursor.execute(qry)
        con.commit()
        mydata = mycursor.fetchall()
        for e in mydata:
            if (e[0] == self.uname):
                return "exists"
        return True

    def add_user(self,obj):

        qry="insert into user_details values('%s','%s','%s','%s','%s','%s','%s','%s')"%(obj.uname,obj.pwd,self.fname,self.lname,self.age,self.gender,obj.email,self.mob_no)
        mycursor.execute(qry)
        con.commit()
        return True


class profilePage(signUp):

    def __init__(self):
        self.fname=""
        self.lname=""
        self.age=""
        self.gender=""
        self.mob_no=""
        super().__init__()

    def check_input(self):
        pattern=re.compile("[a-zA-Z]+")
        match1=re.match(pattern,self.fname)
        match2=re.match(pattern,self.lname)
        if match1 and match2:
            pass
        else:
            return "invalid name"

        if(len(self.age)==2):
            pattern=re.compile("\d{2}")
            match1=re.match(pattern,self.age)
            if match1:
                pass
            else:
                return "invalid age"
        else:
            return "invalid age"

        if (self.gender == 1):
            self.gender = "Male"
        elif (self.gender == 2):
            self.gender = "Female"
        else:
            return "invalid gender"

        if(len(self.mob_no)==10):
            pattern = re.compile("\d{10}")
            match2=re.match(pattern,self.mob_no)
            if match2:
                pass
            else:
                return "invalid mob_no"
        else:
            return "invalid mob_no"

        return True

    def editProfile(self):
        pass

class quiz_userview:

    @staticmethod
    def get_ques(mod):
        qry="select ques,option1,option2,option3,option4,positiveMarks,negativeMarks,ques_id,answer from quiz_details where module=('%s')"%(mod)
        mycursor.execute(qry)
        mydata=mycursor.fetchall()
        return mydata

    @staticmethod
    def get_mod():
        qry = "select distinct module from quiz_details"
        mycursor.execute(qry)
        mydata = mycursor.fetchall()
        return mydata

    # @staticmethod
    # def get_subMod(mod):
    #     qry = "select distinct subModule from quiz_details where module=('%s')"%(mod)
    #     mycursor.execute(qry)
    #     mydata = mycursor.fetchall()
    #     print(mydata)
    #     return mydata
    #


def addAns(q_no,ans):
    qry="insert into userAns values('%s','%s')"%(q_no,ans)
    mycursor.execute(qry)
    con.commit()

def checkAns(q_no):
    qry="select * from userAns where ques_id=('%s')"%(q_no)
    mycursor.execute(qry)
    mydata=mycursor.fetchall()
    if(len(mydata)==0):
        return False
    else:
        return mydata[0][1]
