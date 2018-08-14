# import py_compile
# py_compile.compile("bll_quiz.py")

import tkinter
from tkinter import *
from PIL import Image,ImageTk
import tkinter.ttk
from tkinter.ttk import *
from tkinter import messagebox
import bll_quiz
from bll_quiz import *

root = Tk()
# first page
def first_page():
    global flag

    # login form

    unameLogin = StringVar()
    pwdLogin = StringVar()


    def btnLogin_click():
        global flag
        flag = 0
        loginObj.uname = unameLogin.get()
        loginObj.pwd = pwdLogin.get()

        if (comboBoxLogin.get() == "User"):
            res = loginObj.find_user()
            if (res == True):
                tkinter.messagebox.showinfo("Sucess", "Successfully logged in")
                btnStart_click()
            else:
                tkinter.messagebox.showerror("Error", "User not found")

        elif (comboBoxLogin.get() == "Admin"):
            res = loginObj.find_admin()
            if (res == True):
                tkinter.messagebox.showinfo("Sucess", "Successfully logged in")
                adminWin()
            else:
                tkinter.messagebox.showerror("Error", "Admin not found")

    loginObj = login()
    loginFrame = tkinter.Frame(root, height=400, width=350, bg="#cccccc")
    loginFrame.place(relx=0.1, rely=0.25)

    lblColor = tkinter.Label(loginFrame, height=7, width=350, bg="#009900")
    lblColor.place(x=0, y=0)

    lblLogin = tkinter.Label(loginFrame, text="Login", font=("Times", 25, "bold"), fg="white", bg="#009900")
    lblLogin.place(x=10, y=20)

    lblCaption = tkinter.Label(loginFrame, text="Login in to get started", font=("Times", 18), fg="white", bg="#009900")
    lblCaption.place(x=10, y=70)

    lblas = tkinter.Label(loginFrame, text="Login as", font=("courier", 15, "bold"), bg="#cccccc")
    lblas.place(x=10, y=130)

    comboBoxLogin = Combobox(loginFrame, width=31, font=("times", 15))
    comboLoginList = ["User", "Admin"]
    comboBoxLogin.set("User")
    comboBoxLogin["values"] = comboLoginList
    comboBoxLogin.place(x=10, y=160)

    lblLoginUname = tkinter.Label(loginFrame, text="Username", font=("courier", 15, "bold"), bg="#cccccc")
    lblLoginUname.place(x=10, y=200)

    unameLoginTxt = Entry(loginFrame, textvariable=unameLogin, width=36,font=15)
    unameLoginTxt.place(x=10, y=230)

    lblLoginPwd = tkinter.Label(loginFrame, text="Password", font=("courier", 15, "bold"), bg="#cccccc")
    lblLoginPwd.place(x=10, y=260)

    pwdLoginTxt = Entry(loginFrame, textvariable=pwdLogin, show="*", width=36,font=15)
    pwdLoginTxt.place(x=10, y=290)

    btnSubmitLogin = tkinter.Button(loginFrame, text="Login", bg="#00e600", fg="white",
                                    font=("times", 12, "bold"), width=35,command=btnLogin_click)
    btnSubmitLogin.place(x=10, y=330)

    # sign up form

    unameSignup = StringVar()
    pwdSignup = StringVar()
    emailSignup = StringVar()
    cpwdSignup = StringVar()


    def btnSignup_click():
        global flag
        flag=1
        signUpObj.uname = unameSignup.get()
        signUpObj.pwd = pwdSignup.get()
        signUpObj.email = emailSignup.get()

        res = signUpObj.check_inputs()
        if (res == "invalid email"):
            tkinter.messagebox.showerror("Error", "Invalid Email Id")
        elif (res == "invalid uname"):
            tkinter.messagebox.showerror("Error", "Invalid Username\nlength must be of 5 to 10 characters")
        elif (res == "invalid pwd"):
            tkinter.messagebox.showerror("Error", "Invalid password\nlength must be of 5 to 10 characters")
        else:
            res=signUpObj.check_email()
            if(res=="exists"):
                tkinter.messagebox.showerror("Error","Already registered email Id")
            else:

                resp = signUpObj.check_uname()
                if (resp == "exists"):
                    tkinter.messagebox.showerror("Error", "Username already exists")
                elif (resp == True):
                        if (pwdSignup.get() == cpwdSignup.get()):
                            tkinter.messagebox.showinfo("Success", "Sucessfully registered")
                            # print(signUpObj.uname,signUpObj.pwd,signUpObj.email,sep="\t")
                            btnStart_click()
                        else:
                            tkinter.messagebox.showerror("Error", "password did not matched")

    global signUpObj
    signUpObj = signUp()

    SignupFrame = tkinter.Frame(root, height=440, width=350, bg="#cccccc")
    SignupFrame.place(relx=0.6, rely=0.25)

    lblColor = tkinter.Label(SignupFrame, height=7, width=350, bg="#ff4d4d")
    lblColor.place(x=0, y=0)

    lblLogin = tkinter.Label(SignupFrame, text="Sign Up", font=("Times", 25, "bold"), fg="white", bg="#ff4d4d")
    lblLogin.place(x=10, y=20)

    lblCaption = tkinter.Label(SignupFrame, text="Sign up to be a part of the quiz", font=("Times", 18), fg="white",
                               bg="#ff4d4d")
    lblCaption.place(x=10, y=70)

    lblSignupEmail = tkinter.Label(SignupFrame, text="Email Id", font=("courier", 15, "bold"), bg="#cccccc")
    lblSignupEmail.place(x=10, y=130)

    emailSignupTxt = Entry(SignupFrame, textvariable=emailSignup, width=36,font=15)
    emailSignupTxt.place(x=10, y=160)

    lblSignUpUname = tkinter.Label(SignupFrame, text="Username", font=("courier", 15, "bold"), bg="#cccccc")
    lblSignUpUname.place(x=10, y=190)

    unameSignupTxt = Entry(SignupFrame, textvariable=unameSignup, width=36,font=15)
    unameSignupTxt.place(x=10, y=220)

    lblSignupPwd = tkinter.Label(SignupFrame, text="Password", font=("courier", 15, "bold"), bg="#cccccc")
    lblSignupPwd.place(x=10, y=250)

    pwdSignupTxt = Entry(SignupFrame, textvariable=pwdSignup, show="*", width=36,font=15)
    pwdSignupTxt.place(x=10, y=280)

    lblSignupCPwd = tkinter.Label(SignupFrame, text="Confirm Password", font=("courier", 15, "bold"), bg="#cccccc")
    lblSignupCPwd.place(x=10, y=310)

    pwdSignupCTxt = Entry(SignupFrame, textvariable=cpwdSignup, show="*", width=36,font=15)
    pwdSignupCTxt.place(x=10, y=340)

    btnSignUp = tkinter.Button(SignupFrame, text="Sign Up", command=btnSignup_click, bg="#ff4d4d", fg="white",
                                    font=("times", 12, "bold"), width=35)
    btnSignUp.place(x=10, y=390)



#<--------------------------ADMIN VIEW---------------------------------------->
def adminWin():

    def startPageAdmin():
        global frameView
        lblColor = tkinter.Label(adminView, bg="#ffccdd", height=12)
        lblColor.pack(fill=X)
        lblHead = tkinter.Label(adminView, text="ADMIN PANEL", fg="orange", bg="#ffccdd", font=("comic", 50, "italic"))
        lblHead.place(relx=0.32, rely=0.09)
        frameView = tkinter.Frame(adminView, bg="white", height=450, width=950)
        frameView.pack()
        frameView.pack_propagate(0)
        lblColor2=tkinter.Label(frameView,bg="#eafbcc",height=6)
        lblColor2.pack(fill=X)
        btnHome = tkinter.Button(adminView, text="Home", bg="#22ccee", font=("times", 16), width=7)
        btnHome.place(relx=0.9, rely=0.3)
        btnLogOut = tkinter.Button(adminView, text="Log Out", bg="#22ccee", font=("times", 16), width=7)
        btnLogOut.place(relx=0.9, rely=0.4)

        btnUser = tkinter.Button(adminView, text="Manage Users", bg="#bbaacc", font=("times", 20), command=user_click)
        btnUser.place(relx=0.01, rely=0.3)
        btnAdmin = tkinter.Button(adminView, text="Manage Admin", bg="#bbaacc", font=("times", 20), command=admin_click)
        btnAdmin.place(relx=0.01, rely=0.45)
        btnQuiz = tkinter.Button(adminView, text="Manage Quiz", bg="#bbaacc", font=("times", 20), command=quiz_click)
        btnQuiz.place(relx=0.01, rely=0.6)

    def admin_click():
        global frameView
        frameView.destroy()
        frameView = tkinter.Frame(adminView, bg="white", height=450, width=950)
        frameView.pack()
        frameView.pack_propagate(0)
        lblColor2 = tkinter.Label(frameView, bg="#eafbcc", height=6)
        lblColor2.pack(fill=X)
        global frameInner
        frameInner = tkinter.Frame(frameView, bg="white")
        frameInner.pack(fill="both", expand=True)
        frameInner.pack_propagate(0)

        def addAdmin():
            global frameInner
            frameInner.destroy()
            frameInner = tkinter.Frame(frameView, bg="white")
            frameInner.pack(fill="both", expand=True)
            frameInner.pack_propagate(0)
            def btnAdd_click():
                adminObj.uname = adminUname.get()
                adminObj.pwd = adminPwd.get()
                if(adminCPwd.get()==adminPwd.get()):
                    res = adminObj.check_adminUname()
                    if (res == False):
                        tkinter.messagebox.showerror("Error", "Admin already exists")
                    else:
                        res = adminObj.add_admin()
                        if (res == True):
                            tkinter.messagebox.showinfo("Success", "Admin added successfully")
                        else:
                            tkinter.messagebox.showerror("Error", "Invalid Username or Password")
                else:
                    tkinter.messagebox.showerror("Error","Password did not match")

            def btnCancel_click():
                pass

            adminUname=StringVar()
            adminPwd=StringVar()
            adminCPwd = StringVar()

            lblAdminUname=tkinter.Label(frameInner,text="Username",font=("arial",15),bg="white")
            lblAdminUname.place(relx=0.2,rely=0.2)
            adminUnameTxt=Entry(frameInner,textvariable=adminUname,font=15)
            adminUnameTxt.place(relx=0.4,rely=0.2)
            lblAdminPwd = tkinter.Label(frameInner, text="Password", font=("arial", 15), bg="white")
            lblAdminPwd.place(relx=0.2, rely=0.4)
            adminPwdTxt = Entry(frameInner, textvariable=adminPwd, font=15,show="*")
            adminPwdTxt.place(relx=0.4, rely=0.4)
            lblAdminCPwd = tkinter.Label(frameInner, text="Confirm Password", font=("arial", 15), bg="white")
            lblAdminCPwd.place(relx=0.2, rely=0.6)
            adminCPwdTxt = Entry(frameInner, textvariable=adminCPwd, font=15,show="*")
            adminCPwdTxt.place(relx=0.4, rely=0.6)

            btnAdd=tkinter.Button(frameInner,text="Add",bg="#aaffcc",font=20,width=15,command=btnAdd_click)
            btnAdd.place(relx=0.45,rely=0.8)
            btnCancel = tkinter.Button(frameInner, text="Cancel", bg="#aaffcc", font=20, width=15,command=btnCancel_click)
            btnCancel.place(relx=0.65, rely=0.8)

        def deleteAdmin():
            global frameInner
            frameInner.destroy()
            frameInner = tkinter.Frame(frameView, bg="white")
            frameInner.pack(fill="both", expand=True)
            frameInner.pack_propagate(0)

            def btnDelete_click():
                adminObj.uname = adminUname.get()
                adminObj.pwd=adminPwd.get()
                res = adminObj.delete_admin()
                if (res == True):
                    tkinter.messagebox.showinfo("Success", "Admin deleted successfully")
                else:
                    tkinter.messagebox.showerror("Error", "Admin not found")

            def btnCancel_click():
                pass

            adminUname=StringVar()
            adminPwd=StringVar()

            lblAdminUname=tkinter.Label(frameInner,text="Username",font=("arial",15),bg="white")
            lblAdminUname.place(relx=0.2,rely=0.3)
            adminUnameTxt=Entry(frameInner,textvariable=adminUname,font=15)
            adminUnameTxt.place(relx=0.4,rely=0.3)
            lblAdminPwd = tkinter.Label(frameInner, text="Password", font=("arial", 15), bg="white")
            lblAdminPwd.place(relx=0.2, rely=0.5)
            adminPwdTxt = Entry(frameInner,font=15,show="*",textvariable=adminPwd)
            adminPwdTxt.place(relx=0.4, rely=0.5)
            btnAdd=tkinter.Button(frameInner,text="Delete",bg="#aaffcc",font=20,width=15,command=btnDelete_click)
            btnAdd.place(relx=0.45,rely=0.7)
            btnCancel = tkinter.Button(frameInner, text="Cancel", bg="#aaffcc", font=20, width=15,command=btnCancel_click)
            btnCancel.place(relx=0.65, rely=0.7)

        def displayAll():
            global frameInner
            frameInner.destroy()
            frameInner = tkinter.Frame(frameView, bg="white",padx=50,pady=10)
            frameInner.pack(fill="both", expand=True)
            frameInner.pack_propagate(0)

            res = admin.display()
            if (res == False):
                lblEmpty=Label(frameInner,text="No admin to show",font=("times",20))
                lblEmpty.place(relx=0.3,rely=0.2)
            else:
                lblH1=tkinter.Label(frameInner,text="Number",font=("arial",15,"bold"), bg="#cccccc",width=10,pady=5)
                lblH1.grid(row=0,column=0,padx=5,pady=5)
                lblH2 = tkinter.Label(frameInner, text="Username", font=("arial", 15, "bold"), bg="#cccccc",width=20,pady=5)
                lblH2.grid(row=0, column=1,padx=5,pady=5)
                lblH3 = tkinter.Label(frameInner, text="Password", font=("arial", 15, "bold"), bg="#cccccc",width=20,pady=5)
                lblH3.grid(row=0, column=2,padx=5,pady=5)
                for i in range(len(res)):
                    lblD1 = tkinter.Label(frameInner ,text=i+1,font=("arial", 12), bg="#f2f2f2",width=13)
                    lblD1.grid(row=i+1, column=0, pady=5,padx=5)
                    lblD2 = tkinter.Label(frameInner, text=res[i][0], font=("arial", 12), bg="#f2f2f2", width=27)
                    lblD2.grid(row=i + 1, column=1, pady=5, padx=5)
                    lblD3 = tkinter.Label(frameInner, text=res[i][1], font=("arial", 12), bg="#f2f2f2", width=27)
                    lblD3.grid(row=i + 1, column=2, pady=5, padx=5)

        adminObj=admin()

        btnAdd = tkinter.Button(frameView, text="Add an Admin", bg="#aaffdd", font=("times", 16),command=addAdmin)
        btnAdd.place(relx=0.1, rely=0.05)
        btnDelete = tkinter.Button(frameView, text="Delete an Admin", bg="#aaffdd", font=("times", 16),command=deleteAdmin)
        btnDelete.place(relx=0.4, rely=0.05)
        btnDisplay = tkinter.Button(frameView, text="Display all the Admin", bg="#aaffdd", font=("times", 16),command=displayAll)
        btnDisplay.place(relx=0.7, rely=0.05)

    def user_click():
        global frameView
        frameView.destroy()
        frameView = tkinter.Frame(adminView, bg="white", height=450, width=950)
        frameView.pack()
        frameView.pack_propagate(0)
        lblColor2 = tkinter.Label(frameView, bg="#eafbcc", height=6)
        lblColor2.pack(fill=X)

        global frameInner
        frameInner = tkinter.Frame(frameView, bg="white")
        frameInner.pack(fill="both", expand=True)
        frameInner.pack_propagate(0)

        def btnSearch_click():
            global frameInner
            frameInner.destroy()
            frameInner = tkinter.Frame(frameView, bg="white")
            frameInner.pack(fill="both", expand=True)
            frameInner.pack_propagate(0)

            def placeTxt(lblTxt):
                var = StringVar()

                def search_click():
                    mode=0
                    if(lblTxt=="Username"):
                        userObj.uname=var.get()
                        mode=1

                    elif(lblTxt=="Email Id"):
                        userObj.email=var.get()
                        mode=2

                    elif (lblTxt == "Mobile number"):
                        userObj.mob_no = var.get()
                        mode=3

                    res=userObj.search_user(mode)
                    if(res==False):
                        tkinter.messagebox.showerror("Error","User not found")
                    else:
                        btnDisplay_click(res)

                def btnCancel_click():
                    pass

                userLbl = tkinter.Label(frameInner, text=lblTxt, font=("arial", 15), bg="white",width=16)
                userLbl.place(relx=0.1, rely=0.3)
                userTxt = Entry(frameInner,textvariable=var, font=15)
                userTxt.place(relx=0.3, rely=0.3)
                btnSearch = tkinter.Button(frameInner, text="Search", bg="#aaffcc", font=20, width=15,command=search_click)

                btnSearch.place(relx=0.6, rely=0.28)
                btnCancel = tkinter.Button(frameInner, text="Cancel", bg="#aaffcc", font=20, width=15,
                                           command=btnCancel_click)
                btnCancel.place(relx=0.8, rely=0.28)


            btnUname=tkinter.Button(frameInner,text="Search by Username",font=("times",15),bg="#ffccee",command=lambda :placeTxt("Username"))
            btnUname.place(relx=0.1,rely=0.08)
            btnEmail = tkinter.Button(frameInner, text="Search by Email Id", font=("times", 15), bg="#ffccee",command=lambda :placeTxt("Email Id"))
            btnEmail.place(relx=0.4, rely=0.08)
            btnMob_no = tkinter.Button(frameInner, text="Search by Mobile number", font=("times", 15), bg="#ffccee",command=lambda :placeTxt("Mobile number"))
            btnMob_no.place(relx=0.7, rely=0.08)

        def btnDisplay_click(temp):
            global frameInner
            frameInner.destroy()
            frameInner = tkinter.Frame(frameView, bg="white",padx=3)
            frameInner.pack(fill="both", expand=True)
            frameInner.pack_propagate(0)
            if(temp!=0):
                res=temp
            else:
                res = user.display()
            if (res == False):
                lblEmpty = Label(frameInner, text="No user to show", font=("times", 20))
                lblEmpty.place(relx=0.3, rely=0.2)
            else:
                lblH1 = tkinter.Label(frameInner, text="S.no", font=("arial", 11, "bold"), bg="#cccccc", width=4,
                                      pady=5)
                lblH1.grid(row=0, column=0, padx=2, pady=5)
                lblH2 = tkinter.Label(frameInner, text="Username", font=("arial", 11, "bold"), bg="#cccccc", width=12,
                                      pady=5)
                lblH2.grid(row=0, column=1, padx=2, pady=5)
                lblH3 = tkinter.Label(frameInner, text="Password", font=("arial", 11, "bold"), bg="#cccccc", width=12,
                                      pady=5)
                lblH3.grid(row=0, column=2, padx=2, pady=5)
                lblH4 = tkinter.Label(frameInner, text="First name", font=("arial", 11, "bold"), bg="#cccccc", width=12,
                                      pady=5)
                lblH4.grid(row=0, column=3, padx=2, pady=5)
                lblH5 = tkinter.Label(frameInner, text="Last name", font=("arial", 11, "bold"), bg="#cccccc", width=12,
                                      pady=5)
                lblH5.grid(row=0, column=4, padx=2, pady=5)
                lblH6 = tkinter.Label(frameInner, text="Age", font=("arial", 11, "bold"), bg="#cccccc", width=4,
                                      pady=5)
                lblH6.grid(row=0, column=5, padx=2, pady=5)
                lblH7 = tkinter.Label(frameInner, text="Gender", font=("arial", 11, "bold"), bg="#cccccc", width=10,
                                      pady=5)
                lblH7.grid(row=0, column=6, padx=2, pady=5)
                lblH8 = tkinter.Label(frameInner, text="Email Id", font=("arial", 11, "bold"), bg="#cccccc", width=15,
                                      pady=5)
                lblH8.grid(row=0, column=7, padx=2, pady=5)
                lblH9 = tkinter.Label(frameInner, text="Mobile No.", font=("arial", 11, "bold"), bg="#cccccc", width=12,
                                      pady=5)
                lblH9.grid(row=0, column=8, padx=2, pady=5)

                for i in range(len(res)):
                    lblD1 = tkinter.Label(frameInner, text=i + 1, font=("arial", 10), bg="#f2f2f2", width=5)
                    lblD1.grid(row=i + 1, column=0, pady=5, padx=2)
                    lblD2 = tkinter.Label(frameInner, text=res[i][0], font=("arial", 10), bg="#f2f2f2", width=14)
                    lblD2.grid(row=i + 1, column=1, pady=5, padx=2)
                    lblD3 = tkinter.Label(frameInner, text=res[i][1], font=("arial", 10), bg="#f2f2f2", width=14)
                    lblD3.grid(row=i + 1, column=2, pady=5, padx=2)
                    lblD4 = tkinter.Label(frameInner, text=res[i][2], font=("arial", 10), bg="#f2f2f2", width=14)
                    lblD4.grid(row=i + 1, column=3, pady=5, padx=2)
                    lblD5 = tkinter.Label(frameInner, text=res[i][3], font=("arial", 10), bg="#f2f2f2", width=14)
                    lblD5.grid(row=i + 1, column=4, pady=5, padx=2)
                    lblD6 = tkinter.Label(frameInner, text=res[i][4], font=("arial", 10), bg="#f2f2f2", width=4)
                    lblD6.grid(row=i + 1, column=5, pady=5, padx=2)
                    lblD7 = tkinter.Label(frameInner, text=res[i][5], font=("arial", 10), bg="#f2f2f2", width=8)
                    lblD7.grid(row=i + 1, column=6, pady=5, padx=2)
                    lblD8 = tkinter.Label(frameInner, text=res[i][6], font=("arial", 10), bg="#f2f2f2", width=18)
                    lblD8.grid(row=i + 1, column=7, pady=5, padx=2)
                    lblD9 = tkinter.Label(frameInner, text=res[i][7], font=("arial", 10), bg="#f2f2f2", width=14)
                    lblD9.grid(row=i + 1, column=8, pady=5, padx=2)

        userObj=user()
        btnSearch = tkinter.Button(frameView, text="Search user", bg="#aaffdd", font=("times", 16),command=btnSearch_click)
        btnSearch.place(relx=0.25, rely=0.05)
        btnDisplay = tkinter.Button(frameView, text="Display all the Users", bg="#aaffdd", font=("times", 16),command=lambda :btnDisplay_click(0))
        btnDisplay.place(relx=0.5, rely=0.05)

    def quiz_click():
        global frameView
        frameView.destroy()
        frameView = tkinter.Frame(adminView, bg="white", height=450, width=950)
        frameView.pack()
        frameView.pack_propagate(0)
        lblColor2 = tkinter.Label(frameView, bg="#eafbcc", height=6)
        lblColor2.pack(fill=X)

        global frameInner
        frameInner = tkinter.Frame(frameView, bg="white")
        frameInner.pack(fill="both", expand=True)
        frameInner.pack_propagate(0)

        def btn_addClick():
            global frameInner
            frameInner.destroy()
            frameInner = tkinter.Frame(frameView, bg="white", padx=3)
            frameInner.pack(fill="both", expand=True)
            frameInner.pack_propagate(0)

            q_id=StringVar()
            ques=StringVar()
            opt1=StringVar()
            opt2=StringVar()
            opt3=StringVar()
            opt4=StringVar()
            ans=StringVar()
            pos=StringVar()
            neg=StringVar()

            def btnAdd_click():
                quizObj.ques_id = q_id.get()
                quizObj.ques = ques.get()
                quizObj.option1 = opt1.get()
                quizObj.option2 = opt2.get()
                quizObj.option3 = opt3.get()
                quizObj.option4 = opt4.get()
                quizObj.ans = ans.get()
                quizObj.posMarks = pos.get()
                quizObj.negMarks = neg.get()
                quizObj.level = comboBoxLevel.get()
                quizObj.module = comboBoxLevel2.get()

                res = quizObj.check_inputs()
                if (res == "exists"):
                    tkinter.messagebox.showerror("Error", "Ques Id already exists")
                elif(res=="invalid ques id"):
                    tkinter.messagebox.showerror("Error","Invalid ques id")
                elif (res == "invalid ques"):
                    tkinter.messagebox.showerror("Error", "Invalid question")
                elif (res == "invalid option1"):
                    tkinter.messagebox.showerror("Error", "Invalid Option1")
                elif (res == "invalid option2"):
                    tkinter.messagebox.showerror("Error", "Invalid Option2")
                elif (res == "invalid option3"):
                    tkinter.messagebox.showerror("Error", "Invalid Option3")
                elif (res == "invalid option4"):
                    tkinter.messagebox.showerror("Error", "Invalid Option4")
                elif (res == "invalid answer"):
                    tkinter.messagebox.showerror("Error", "Invalid answer")
                elif (res == "invalid posMarks"):
                    tkinter.messagebox.showerror("Error", "Invalid Positive marks")
                elif (res == "invalid negMarks"):
                    tkinter.messagebox.showerror("Error", "Invalid Negative marks")
                else:
                    quizObj.add_ques()
                    tkinter.messagebox.showinfo("Success","Question added successfully")

            def btnCancel_click():
                pass


            lblQues_id=tkinter.Label(frameInner,text="Ques Id",font=("arial", 15,"bold"), bg="white",width=16)
            lblQues_id.place(relx=0.1,rely=0)
            ques_idTxt=Entry(frameInner,textvariable=q_id,font=15,justify="right")
            ques_idTxt.place(relx=0.3,rely=0.01)
            lblQues = tkinter.Label(frameInner, text="Question", font=("arial", 15, "bold"), bg="white", width=16)
            lblQues.place(relx=0.1, rely=0.1)
            quesTxt = Entry(frameInner, textvariable=ques, font=15,width=60,justify="left")
            quesTxt.place(relx=0.3, rely=0.1)
            lblOpt1 = tkinter.Label(frameInner, text="Option 1", font=("arial", 15, "bold"), bg="white", width=16)
            lblOpt1.place(relx=0.1, rely=0.2)
            opt1Txt = Entry(frameInner, textvariable=opt1, font=15,justify="right")
            opt1Txt.place(relx=0.3, rely=0.2)
            lblOpt2 = tkinter.Label(frameInner, text="Option 2", font=("arial", 15, "bold"), bg="white", width=16)
            lblOpt2.place(relx=0.1, rely=0.3)
            opt2Txt = Entry(frameInner, textvariable=opt2, font=15,justify="right")
            opt2Txt.place(relx=0.3, rely=0.3)
            lblOpt3 = tkinter.Label(frameInner, text="Option 3", font=("arial", 15, "bold"), bg="white", width=16)
            lblOpt3.place(relx=0.1, rely=0.4)
            opt3Txt = Entry(frameInner, textvariable=opt3, font=15,justify="right")
            opt3Txt.place(relx=0.3, rely=0.4)
            lblOpt4 = tkinter.Label(frameInner, text="Option 4", font=("arial", 15, "bold"), bg="white", width=16)
            lblOpt4.place(relx=0.1, rely=0.5)
            opt4Txt = Entry(frameInner, textvariable=opt4, font=15,justify="right")
            opt4Txt.place(relx=0.3, rely=0.5)
            lblAns = tkinter.Label(frameInner, text="Correct answer", font=("arial", 15, "bold"), bg="white", width=16)
            lblAns.place(relx=0.1, rely=0.6)
            ansTxt = Entry(frameInner, textvariable=ans, font=15,justify="right")
            ansTxt.place(relx=0.3, rely=0.6)
            lblPos = tkinter.Label(frameInner, text="Positive Marks", font=("arial", 15, "bold"), bg="white",
                                       width=16)
            lblPos.place(relx=0.1, rely=0.7)
            posTxt = Entry(frameInner, textvariable=pos, font=15,justify="right")
            posTxt.place(relx=0.3, rely=0.7)
            lblNeg = tkinter.Label(frameInner, text="Negative Marks", font=("arial", 15, "bold"), bg="white",
                                   width=16)
            lblNeg.place(relx=0.1, rely=0.8)
            negTxt = Entry(frameInner, textvariable=neg, font=15,justify="right")
            negTxt.place(relx=0.3, rely=0.8)
            lblLevel = tkinter.Label(frameInner, text="Level", font=("arial", 15, "bold"), bg="white",
                                   width=16)
            lblLevel.place(relx=0.1, rely=0.9)
            comboBoxLevel=Combobox(frameInner,font=("arial",13),width=15,values=["Easy","Medium","Hard"],justify="right")
            comboBoxLevel.set("Easy")
            comboBoxLevel.place(relx=0.3,rely=0.9)

            lblModule = tkinter.Label(frameInner, text="Module", font=("arial", 15, "bold"), bg="white",
                                     width=16)
            lblModule.place(relx=0.5, rely=0.4)
            comboBoxLevel2 = Combobox(frameInner, font=("arial", 13), width=15, values=["Programming","Verbal ability","Aptitude","Logical reasoning"],
                                     justify="right")
            comboBoxLevel2.set("Programming")
            comboBoxLevel2.place(relx=0.7, rely=0.4)
            btnAdd = tkinter.Button(frameInner, text="Add", bg="#aaffcc", font=20, width=15, command=btnAdd_click)
            btnAdd.place(relx=0.55, rely=0.8)
            btnCancel = tkinter.Button(frameInner, text="Cancel", bg="#aaffcc", font=20, width=15,
                                       command=btnCancel_click)
            btnCancel.place(relx=0.75, rely=0.8)

        def btn_searchClick():

            global frameInner
            frameInner.destroy()
            frameInner = tkinter.Frame(frameView, bg="white")
            frameInner.pack(fill="both", expand=True)
            frameInner.pack_propagate(0)
            q_id=StringVar()

            def btnSearch_click():
                quizObj.ques_id = q_id.get()
                res=quizObj.search_ques()
                if(res==False):
                    tkinter.messagebox.showerror("Error","Question not found")
                else:
                    btn_displayClick(res)

            def btnCancel_click():
                pass


            q_id=StringVar()
            lblQues_id = tkinter.Label(frameInner, text="Ques Id", font=("arial", 15, "bold"), bg="white", width=16)
            lblQues_id.place(relx=0.1, rely=0)
            ques_idTxt = Entry(frameInner, textvariable=q_id, font=15, justify="right")
            ques_idTxt.place(relx=0.3, rely=0.01)
            btnAdd = tkinter.Button(frameInner, text="Search", bg="#aaffcc", font=20, width=15, command=btnSearch_click)
            btnAdd.place(relx=0.55, rely=0.8)
            btnCancel = tkinter.Button(frameInner, text="Cancel", bg="#aaffcc", font=20, width=15,
                                       command=btnCancel_click)
            btnCancel.place(relx=0.75, rely=0.8)

        def btn_displayClick(tem):
                global frameInner
                frameInner.destroy()
                frameInner = tkinter.Frame(frameView, bg="white", padx=3)
                frameInner.pack(fill="both", expand=True)
                frameInner.pack_propagate(0)
                if (tem != 0):
                    res = tem
                else:
                    res = quiz_details.display()

                if (res == False):
                    lblEmpty = tkinter.Label(frameInner, text="No Questions to show", font=("times", 20),bg="white")
                    lblEmpty.place(relx=0.3, rely=0.2)
                else:
                    lblH1 = tkinter.Label(frameInner, text="Ques_id", font=("arial", 11, "bold"), bg="#cccccc", width=4,
                                          pady=5)
                    lblH1.grid(row=0, column=0, padx=2, pady=5)
                    lblH2 = tkinter.Label(frameInner, text="Question", font=("arial", 11, "bold"), bg="#cccccc",
                                          width=12,
                                          pady=5)
                    lblH2.grid(row=0, column=1, padx=2, pady=5)
                    lblH3 = tkinter.Label(frameInner, text="Option1", font=("arial", 11, "bold"), bg="#cccccc",
                                          width=12,
                                          pady=5)
                    lblH3.grid(row=0, column=2, padx=2, pady=5)
                    lblH4 = tkinter.Label(frameInner, text="Option2", font=("arial", 11, "bold"), bg="#cccccc",
                                          width=12,
                                          pady=5)
                    lblH4.grid(row=0, column=3, padx=2, pady=5)
                    lblH5 = tkinter.Label(frameInner, text="Option3", font=("arial", 11, "bold"), bg="#cccccc",
                                          width=12,
                                          pady=5)
                    lblH5.grid(row=0, column=4, padx=2, pady=5)
                    lblH6 = tkinter.Label(frameInner, text="Option4", font=("arial", 11, "bold"), bg="#cccccc", width=4,
                                          pady=5)
                    lblH6.grid(row=0, column=5, padx=2, pady=5)
                    lblH7 = tkinter.Label(frameInner, text="Answer", font=("arial", 11, "bold"), bg="#cccccc", width=10,
                                          pady=5)
                    lblH7.grid(row=0, column=6, padx=2, pady=5)
                    lblH8 = tkinter.Label(frameInner, text="Positive marks", font=("arial", 11, "bold"), bg="#cccccc",
                                          width=15,
                                          pady=5)
                    lblH8.grid(row=0, column=7, padx=2, pady=5)
                    lblH9 = tkinter.Label(frameInner, text="Negative marks", font=("arial", 11, "bold"), bg="#cccccc",
                                          width=12,
                                          pady=5)
                    lblH9.grid(row=0, column=8, padx=2, pady=5)

                    for i in range(len(res)):
                        for j in range(10):
                            lblD1 = tkinter.Label(frameInner, text=res[i][j], font=("arial", 10), bg="#f2f2f2")
                            lblD1.grid(row=i + 1, column=j, pady=5, padx=2)

        quizObj=quiz_details()
        btnAdd = tkinter.Button(frameView, text="Add a question", bg="#aaffdd", font=("times", 16),command=btn_addClick)
        btnAdd.place(relx=0.1, rely=0.05)
        # btnDelete = tkinter.Button(frameView, text="Delete a question", bg="#aaffdd", font=("times", 16))
        # btnDelete.place(relx=0.3, rely=0.05)
        btnSearch = tkinter.Button(frameView, text="Search for a question", bg="#aaffdd", font=("times", 16),command=btn_searchClick)
        btnSearch.place(relx=0.35, rely=0.05)
        # btnModify = tkinter.Button(frameView, text="Modify a question", bg="#aaffdd", font=("times", 16))
        # btnModify.place(relx=0.75, rely=0.05)
        btnDisplay = tkinter.Button(frameView, text="Display all the questions", bg="#aaffdd", font=("times", 16),command=lambda :btn_displayClick(0))
        btnDisplay.place(relx=0.7, rely=0.05)

    adminView = Toplevel(root)
    adminView.config(bg="#ffffcc")
    adminView.state("z")
    startPageAdmin()
    adminView.mainloop()
#<-----------------------------------USER VIEW ---------------------------------------->
#Start section
def btnStart_click():

    # def btnLogOut_click():
    #     # homePage.destroy()
    #     # userViewMod.destroy()
    #     # userViewSub.destroy()
    #     pass
    global startPage
    startPage=Toplevel(root,bg="#e6e600")
    startPage.state("z")

    imageFrame=tkinter.Frame(startPage,height=600,width=550,bg="#e6e600")
    imageFrame.place(relx=0.05,rely=0.07)
    photo = PhotoImage(file="qphoto.gif")
    lblImg = Label(imageFrame, image=photo)
    lblImg.pack(fill="both", expand=True)

    textFrame = tkinter.Frame(startPage, height=600, width=550,bg="#e6e600")
    textFrame.place(relx=0.5, rely=0.07)

    # btnProfile=tkinter.Button(homePage,text="Profile",command=btnProfile_click,bg="#ffaa12",font=("times",15))
    # btnProfile.place(x=1000,y=50)
    #
    # btnLogOut = tkinter.Button(homePage, text="Log out", command=btnLogOut_click, bg="#ffaa12", font=("times", 15))
    # btnLogOut.place(x=1150,y=50)

    lblH1=tkinter.Label(textFrame,text="THE ONLINE QUIZ",fg="black",font=("arial",35,"bold"),bg="#e6e600")
    lblH1.place(relx=0.1,rely=0.15)

    lblH2 = tkinter.Label(textFrame, text="If you get a high score,you probably spend too much time on Wikipedia", fg="white", font=("arial", 25,),wraplength=480,justify="left",bg="#e6e600")
    lblH2.place(relx=0.1, rely=0.30)

    lblH2 = tkinter.Label(textFrame, text="Start now to achieve your own high score",
                          fg="black", font=("arial", 17,), wraplength=500,bg="#e6e600")
    lblH2.place(relx=0.1, rely=0.55)

    btnStart=tkinter.Button(textFrame,text="START NOW",fg="white",bg="black",font=("arial",30,"bold"),width=18)
    if(flag==1):
        btnStart.config(command=btnProfile_click)
    else:
        btnStart.config(command=homePageUser)
    btnStart.place(relx=0.1,rely=0.7)

    startPage.mainloop()


# profile page
def btnProfile_click():

    def btnSave_click():
        profileObj.fname = firstName.get()
        profileObj.lname=lastName.get()
        profileObj.age=age.get()
        profileObj.mob_no=mob_no.get()
        profileObj.gender=radio1.get()

        global signUpObj
        op=profileObj.check_input()
        if(op==True):

            res=profileObj.add_user(signUpObj)
            if(res==True):
                tkinter.messagebox.showinfo("Success","profile succesfully completed")
                homePageUser()

        elif(op=="invalid name"):
            tkinter.messagebox.showerror("Error","Invalid name")
        elif(op=="invalid age"):
            tkinter.messagebox.showerror("Error","Invalid age")
        elif(op=="invalid mob_no"):
            tkinter.messagebox.showerror("Error","Invalid Mobile Number")
        elif(op=="invalid gender"):
            tkinter.messagebox.showerror("Error", "Invalid gender")

    global startPage
    profile = Toplevel(startPage)
    profile.config(bg="#ffffcc")
    profile.state("z")

    profileObj = profilePage()
    firstName = StringVar()
    lastName = StringVar()
    age = StringVar()
    mob_no = StringVar()
    radio1 = IntVar()

    lblHeading = tkinter.Label(profile, text="Profile", bg="#ffffcc", fg="#4dd2ff", font=("Times", 55, "italic"))
    lblHeading.place(x=610, y=30)

    lblFirstName = tkinter.Label(profile, text="First Name", fg="#fa2cec", font=("times", 20, "italic"), bg="#ffffcc")
    lblFirstName.place(relx=0.3, rely=0.25)

    lblLastName = tkinter.Label(profile, text="Last Name", fg="#fa2cec", font=("times", 20, "italic"), bg="#ffffcc")
    lblLastName.place(relx=0.6, rely=0.25)

    txtFirstName = Entry(profile, width=20, textvariable=firstName, font=12)
    txtFirstName.place(relx=0.42, rely=0.265)

    txtLastName = Entry(profile, width=20, textvariable=lastName, font=12)
    txtLastName.place(relx=0.72, rely=0.265)

    lblAge = tkinter.Label(profile, text="Age", fg="#fa2cec", font=("times", 20, "italic"), bg="#ffffcc")
    lblAge.place(relx=0.3, rely=0.38)

    txtAge = Entry(profile, width=15, textvariable=age, justify="right", font=15)
    age.set("")
    txtAge.place(relx=0.37, rely=0.4)

    lblGender = tkinter.Label(profile, text="Gender", fg="#fa2cec", font=("times", 20, "italic"), bg="#ffffcc")
    lblGender.place(relx=0.3, rely=0.52)

    genderRadio1 = tkinter.Radiobutton(profile, text="Male", fg="#fa2cec", font=("times", 17, "italic"), value=1,
                                       variable=radio1, bg="#ffffcc")
    genderRadio1.place(relx=0.4, rely=0.52)

    genderRadio2 = tkinter.Radiobutton(profile, text="Female", fg="#fa2cec", font=("times", 17, "italic"), value=2,
                                       variable=radio1, bg="#ffffcc")
    genderRadio2.place(relx=0.5, rely=0.52)

    lblMob = tkinter.Label(profile, text="Mobile Number", fg="#fa2cec", font=("times", 20, "italic"), bg="#ffffcc")
    lblMob.place(relx=0.3, rely=0.65)

    txtMob = Entry(profile, width=20, textvariable=mob_no, justify="right", font=15)
    mob_no.set("")
    txtMob.place(relx=0.46, rely=0.66)

    btnSave = tkinter.Button(profile, text="Save", command=btnSave_click, bg="#4dd2ff", fg="white",
                             font=("times", 18, "bold"), width=15)
    btnSave.place(relx=0.4, rely=0.8)


    profile.mainloop()



# home page view

def homePageUser():

    def moduleView():
        global frameView
        frameView = tkinter.Frame(userView, bg="white", height=450, width=950)
        frameView.pack()
        frameView.pack_propagate(0)
        lblColor2=tkinter.Label(frameView,bg="#eafbcc",height=6)
        lblColor2.pack(fill=X)
        lblTopic=tkinter.Label(lblColor2,text="Topics", fg="orange", bg="#eafbcc", font=("comic", 30, "italic"))
        lblTopic.place(relx=0.4,rely=0.2)
        modData = quiz_userview.get_mod()
        # x = 0.1
        # y = 0.3
        def getMod(i):
            global mod
            mod=modData[i][0]
            instrution()

        btnM = tkinter.Button(frameView, text=modData[0][0], font=("Times", 30, "bold"), fg="blue", bg="#ffffca",padx=2,pady=1,
                               height=1,command=lambda :getMod(0))
        btnM.place(relx=0.1,rely=0.3)
        # btnM = tkinter.Button(frameView, text=modData[1][0], font=("Times", 30, "bold"), fg="blue", bg="#ffffca",
        #                       padx=2, pady=1,
        #                       height=1, command=lambda: getMod(1))
        # btnM.place(relx=0.1, rely=0.3)
        # btnM = tkinter.Button(frameView, text=modData[2][0], font=("Times", 30, "bold"), fg="blue", bg="#ffffca",
        #                       padx=2, pady=1,
        #                       height=1, command=lambda: getMod(2))
        # btnM.place(relx=0.4, rely=0.5)
        # btnM = tkinter.Button(frameView, text=modData[3][0], font=("Times", 30, "bold"), fg="blue", bg="#ffffca",
        #                       padx=2, pady=1,
        #                       height=1, command=lambda: getMod(3))
        # btnM.place(relx=0.4, rely=0.5)
        # # btnM = tkinter.Button(frameView, text=modData[1][0], font=("Times", 30, "bold"), fg="blue", bg="#ffffca",
        #                       padx=2, pady=1,
        #                       height=1, command=lambda: getMod(1))
        # btnM.place(relx=0.4, rely=0.3)
        # btnM = tkinter.Button(frameView, text=modData[2][0], font=("Times", 30, "bold"), fg="blue", bg="#ffffca",
        #                       padx=2, pady=1,
        #                       height=1, command=lambda: getMod(2))
        # btnM.place(relx=0.7, rely=0.3)
        # btnM = tkinter.Button(frameView, text=modData[3][0], font=("Times", 30, "bold"), fg="blue", bg="#ffffca",
        #                       padx=2, pady=1,
        #                       height=1, command=lambda: getMod(3))
        # btnM.place(relx=0.1, rely=0.5)

            # x=x+0.3
            # if(x>0.7):
            #     x=0.1
            #     y=y+0.2

    # def subModuleView(mod):
    #     global frameView
    #     frameView.destroy()
    #     frameView = tkinter.Frame(userView, bg="white", height=450, width=950)
    #     frameView.pack()
    #     frameView.pack_propagate(0)
    #     lblColor2 = tkinter.Label(frameView, bg="#eafbcc", height=6)
    #     lblColor2.pack(fill=X)
    #     lblTopic = tkinter.Label(lblColor2, text="Sub Topics", fg="orange", bg="#eafbcc", font=("comic", 30, "italic"))
    #     lblTopic.place(relx=0.4, rely=0.2)
    #     submodData = quiz_userview.get_subMod(mod)
    #     x = 0.1
    #     y = 0.3
    #     for e in submodData:
    #         btnM1 = tkinter.Button(frameView, text=e[0], font=("Times", 30, "bold"), fg="blue", bg="#ffffca", padx=2,
    #                                pady=1,
    #                                height=1)
    #         btnM1.place(relx=x, rely=y)
    #         x = x + 0.3
    #         if (x > 0.7):
    #             x = 0.1
    #             y = y + 0.2
    #     btnSubmit = tkinter.Button(frameView, text="Take Test", bg="grey", fg="white",
    #                                font=("Times", 15, "bold"), state=DISABLED)
    #     btnSubmit.place(relx=0.45, rely=0.75)
    #
    #     btnPrev = tkinter.Button(frameView, text="Back", bg="red", fg="white",
    #                              font=("Times", 25, "bold"),command=moduleView)
    #     btnPrev.place(relx=0.25, rely=0.75)

    userView = Toplevel(root)
    userView.config(bg="#ffffcc")
    userView.state("z")
    lblColor = tkinter.Label(userView, bg="#ffccdd", height=12)
    lblColor.pack(fill=X)
    lblHead = tkinter.Label(userView, text="Online Quiz", fg="#bcdeaa", bg="#ffccdd", font=("arial", 80, "italic"))
    lblHead.place(relx=0.35, rely=0.07)
    btnHome = tkinter.Button(userView, text="Home", bg="#22ccee", font=("times", 16), width=7)
    btnHome.place(relx=0.9, rely=0.3)
    btnEdit = tkinter.Button(userView, text="Edit profile", bg="#22ccee", font=("times", 16), width=10)
    btnEdit.place(relx=0.9, rely=0.4)
    btnLogOut = tkinter.Button(userView, text="Log Out", bg="#22ccee", font=("times", 16), width=7)
    btnLogOut.place(relx=0.9, rely=0.5)
    # global frameView
    # frameView = tkinter.Frame(userView, bg="white", height=450, width=950)
    # frameView.pack()
    # frameView.pack_propagate(0)
    moduleView()
    userView.mainloop()

# def userViewWin():
#     def logOut_click():
#         # userViewMod.destroy()
#         # homePage.destroy()
#         # userViewSub.destroy()
#         pass
#
#     def btnHome_click():
#         pass
#
#     def btnProfile_click():
#         pass
#
#     global startPage
#     userViewMod = Toplevel(startPage)
#     userViewMod.state("z")
#     lblMod = tkinter.Label(userViewMod, text="Online Quiz", font=("Tahoma", 50, "bold"), fg="#aa2112")
#     lblMod.place(relx=0.35, rely=0.05)
#     btnLogOut = tkinter.Button(userViewMod, text="Log out", command=logOut_click, bg="#ffaa12", font=("times", 15))
#     btnEdit = tkinter.Button(userViewMod, text="Edit profile", command=btnProfile_click, bg="#ffaa12",
#                              font=("times", 15))
#     btnHome = tkinter.Button(userViewMod, text="Home", command=btnHome_click, bg="#ffaa12",
#                              font=("times", 15))
#     btnHome.place(x=1220, y=150)
#     btnEdit.place(x=1200, y=200)
#     btnLogOut.place(x=1220, y=250)
#
#     modData = quiz_userview.get_mod()
#     j = 0
#     i = 0
#     for e in modData:
#
#         btnM1 = tkinter.Button(userViewMod, text=e[0], font=("Times", 25, "bold"), fg="blue", bg="#ffffca", width=5,
#                                height=1)
#         btnM1.grid(row=i, column=j)
#         j += 1
#         if (j == 2):
#             j = 0
#             i += 1

    # userViewMod.mainloop()

    # module2 = tkinter.Frame(userViewMod, width=240, height=200, background="#ffffca")
    # module2.place(relx=0.27, rely=0.3)
    # module2.pack_propagate(0)
    # btnM2 = tkinter.Button(module2, text="Logical Reasoning", font=("Times", 20, "bold"), fg="blue", bg="#ffffca",
    #                        command=lambda: userSubMod(1))
    # btnM2.pack(fill="both", expand=True)
    #
    # module3 = tkinter.Frame(userViewMod, width=260, height=200, background="#ffffca")
    # module3.place(relx=0.5, rely=0.3)
    # module3.pack_propagate(0)
    # btnM3 = tkinter.Button(module3, text="Quantative Aptitude", font=("Times", 20, "bold"), fg="blue", bg="#ffffca",
    #                        command=lambda: userSubMod(2))
    # btnM3.pack(fill="both", expand=True)
    #
    # module4 = tkinter.Frame(userViewMod, width=250, height=200, background="#ffffca")
    # module4.place(relx=0.75, rely=0.3)
    # module4.pack_propagate(0)
    # btnM4 = tkinter.Button(module4, text="General Knowledge", font=("Times", 20, "bold"), fg="blue", bg="#ffffca",
    #                        command=lambda: userSubMod(3))
    # btnM4.pack(fill="both", expand=True)
    #
    # module5 = tkinter.Frame(userViewMod, width=220, height=190)
    # module5.place(relx=0.05, rely=0.65)
    # module5.pack_propagate(0)
    # btnM5 = tkinter.Button(module5, text="Mathematics", font=("Times", 20, "bold"), fg="blue", bg="#ffffca",
    #                        command=lambda: userSubMod(4))
    # btnM5.pack(fill="both", expand=True)


#sub_module view

# def userSubMod(index):
#
#     listMod=["Programming","Logical Reasoning","Quantative Aptitude","General Knowledge","Mathematics"]
#     listSub=[["Python","C","Java","Javascript"],["Seating Arrangement problems","Circular Arrangements","Blood Relations","Selection and Conditionals"],["Profit and Loss","Work and Time","Sequence and Series","Time and Distance"],["Geography","History","Politics","Economy"],["Algebra","Calculus","Permutations","Number Theory"]]
#
#     def logOut_click():
#         # userViewSub.destroy()
#         # userViewMod.destroy()
#         # homePage.destroy()
#         pass
#
#     # def home_click():
#     #     pass
#
#     def previous_click():
#         userViewWin()
#
#     def call_selectedSub(s):
#         global SelectedSubModule
#         SelectedSubModule = listSub[index][s]
#         instrution()
#
#     userViewSub=Toplevel(root)
#     userViewSub.state("z")
#     lblSub=tkinter.Label(userViewSub,text=listMod[index],font=("Tahoma",40,"bold"),fg="#aa2112")
#     lblSub.place(relx=0.1,rely=0.05)
#
#     btnLogOut=tkinter.Button(userViewSub,text="Log out",command=logOut_click,bg="#ffaa12",font=("times",15))
#     btnHome = tkinter.Button(userViewSub, text="Edit profile", command=btnProfile_click,bg="#ffaa12",font=("times",15))
#     btnPrevious = tkinter.Button(userViewSub, text="Previous", command=previous_click, bg="#ffaa12", font=("times", 15))
#     btnHome.place(x=900,y=50)
#     btnLogOut.place(x=1050,y=50)
#     btnPrevious.place(x=1200, y=50)
#
#
#     subModule1=tkinter.Frame(userViewSub,width=400,height=100,background="#ffffca")
#     subModule1.place(relx=0.1, rely=0.3)
#     subModule1.pack_propagate(0)
#     btnM1=tkinter.Button(subModule1,text=listSub[index][0],font=("Times",20,"bold"),fg="blue",bg="#ffffca",command=lambda :call_selectedSub(0))
#     btnM1.pack(fill="both", expand=True)
#
#     subModule2 = tkinter.Frame(userViewSub, width=400, height=100, background="#ffffca")
#     subModule2.place(relx=0.5, rely=0.3)
#     subModule2.pack_propagate(0)
#     btnM2 = tkinter.Button(subModule2, text=listSub[index][1], font=("Times", 20, "bold"), fg="blue", bg="#ffffca",command=lambda : call_selectedSub(1))
#     btnM2.pack(fill="both", expand=True)
#
#     subModule3 = tkinter.Frame(userViewSub, width=400, height=100, background="#ffffca")
#     subModule3.place(relx=0.1, rely=0.5)
#     subModule3.pack_propagate(0)
#     btnM3 = tkinter.Button(subModule3, text=listSub[index][2], font=("Times", 20, "bold"), fg="blue", bg="#ffffca",command=lambda : call_selectedSub(2))
#     btnM3.pack(fill="both", expand=True)
#
#     subModule4 = tkinter.Frame(userViewSub, width=400, height=100, background="#ffffca")
#     subModule4.place(relx=0.5, rely=0.5)
#     subModule4.pack_propagate(0)
#     btnM4 = tkinter.Button(subModule4, text=listSub[index][3], font=("Times", 20, "bold"), fg="blue", bg="#ffffca",command=lambda : call_selectedSub(3))
#     btnM4.pack(fill="both", expand=True)
#
#     userViewSub.mainloop()

#instructions
def instrution():
    global index
    inst = Toplevel(root)
    inst.state("z")
    lblColor = tkinter.Label(inst, bg="blue", height=3)
    lblColor.pack(fill=X)
    lblColorb = tkinter.Label(inst, bg="blue", height=3)
    lblColorb.pack(fill=X, side="bottom")
    lblColor2 = tkinter.Label(inst, bg="yellow", height=3)
    lblColor2.pack(fill=X)
    lblColor2b = tkinter.Label(inst, bg="yellow", height=2)
    lblColor2b.pack(fill=X, side="bottom")
    lblH1 = tkinter.Label(lblColor2, text="Instructions", bg="yellow", font=("times", 15), padx=15)
    lblH1.pack(side="left")
    lblH2 = tkinter.Label(lblColor2, text="Duration:10 Mins", bg="yellow", font=("times", 15), padx=15)
    lblH2.pack(side="right")

    lblH = Label(inst, text="Please read the instructions carefully", font=("arial", 15, "bold"))
    lblH.place(relx=0.35, rely=0.2)
    msg1 = Message(inst, text="1. The duration of the quiz is 10 mins.", font=("tahoma", 13), padx=20, width=400)
    msg1.place(relx=0.1, rely=0.3)

    msg2 = Message(inst, text="2. The quiz contains 10 multiple choice questions out of which only one is correct.",
                   font=("tahoma", 13), padx=20, width=800)
    msg2.place(relx=0.1, rely=0.35)

    msg3 = Message(inst,
                   text="3. The countdown timer in the top right corner of screen will display the remaining time to complete the quiz.",
                   font=("tahoma", 13), padx=20, width=900)
    msg3.place(relx=0.1, rely=0.4)

    msg4 = Message(inst, text="4. When the time ends the quiz will end by itself. ", font=("tahoma", 13), padx=20,
                   width=400)
    msg4.place(relx=0.1, rely=0.45)

    msg5 = Message(inst, text="5.Click save and next to save your answer for the current question.",
                   font=("tahoma", 13), padx=20, width=600)
    msg5.place(relx=0.1, rely=0.5)

    btnSubmit = tkinter.Button(inst, text="OK,Begin Test", bg="grey", fg="white",
                               font=("Times", 15, "bold"), state=DISABLED)
    btnSubmit.place(relx=0.45, rely=0.75)

    btnPrev = tkinter.Button(inst, text="Previous", bg="red", fg="white",
                             font=("Times", 15, "bold"))
    btnPrev.place(relx=0.25, rely=0.75)

    checkAns = IntVar()

    def check_click():
        if (checkAns.get() == 0):
            btnSubmit.config(bg="grey", fg="white", state=DISABLED)
        elif (checkAns.get() == 1):
            btnSubmit.config(bg="green", fg="white", state=NORMAL,command=call_mainQuiz)

    checkBtn = tkinter.Checkbutton(inst, text="I have read the instructions carefully", variable=checkAns,
                                   font=("tahoma", 12, "bold"), command=check_click)
    checkBtn.place(relx=0.11, rely=0.6)

    inst.mainloop()

#main quiz
def call_mainQuiz():
    global mod,ques_no,attempted,correct,incorrect,score,save
    ques_no = 0;attempted=0;correct=0;incorrect=0;score=0
    save=[]
    def easyBtnclick():
        global ques_no
        ques_no = 0
        showQues()
        lblR["text"]="Easy"
        btns1["text"]="1"
        btns2["text"] = "2"
        btns3["text"] = "3"
        btns4["text"] = "4"
        btns5["text"] = "5"

    def mediumBtnclick():
        global ques_no
        ques_no=5
        showQues()
        lblR["text"] = "Medium"
        btns1["text"] = "6"
        btns2["text"] = "7"
        btns3["text"] = "8"
        btns4["text"] = "9"
        btns5["text"] = "10"


    def hardBtnclick():
        global ques_no
        ques_no=10
        showQues()
        lblR["text"] = "Hard"
        btns1["text"] = "11"
        btns2["text"] = "12"
        btns3["text"] = "13"
        btns4["text"] = "14"
        btns5["text"] = "15"


    def Btnclick_next():
        global ques_no
        ques_no+=1
        res=checkAns(quesData[ques_no][7])
        if(res!=False):
            var.set(res)
            btnSave.config(bg="yellow", fg="white", state=DISABLED)
            btnClear.config(bg="yellow", fg="white", state=DISABLED)
        else:
            Btnclick_clear()
        showQues()


    def Btnclick_previous():
        global ques_no
        ques_no -= 1
        res = checkAns(quesData[ques_no][7])
        if (res != False):
            var.set(res)
            btnSave.config(bg="yellow", fg="white", state=DISABLED)
            btnClear.config(bg="yellow", fg="white", state=DISABLED)
        else:
            Btnclick_clear()
        showQues()


    def check_radio():
        btnSave.config(bg="green", fg="white", state=NORMAL)
        btnClear.config(bg="green",fg="white",state=NORMAL)

    def Btnclick_save():
        global attempted,correct,score,incorrect
        attempted += 1
        if(quesData[ques_no][8]==var.get()):
            correct+=1
            score+=int(quesData[ques_no][5])
        else:
            incorrect+=1
            score-=int(quesData[ques_no][6])
        print(attempted,correct,incorrect,score)
        addAns(quesData[ques_no][7],var.get())
        Btnclick_next()


    def Btnclick_clear():
        var.set("empty")
        btnSave.config(bg="yellow", fg="white", state=DISABLED)
        btnClear.config(bg="yellow", fg="white", state=DISABLED)

    def BtnSubmit_click():
        res=tkinter.messagebox.askyesnocancel("Message","Are you sure you want to submit")
        if(res==True):
            result()

    def btnMenu_click(quesNo):
        pass


    def showQues():
        ques=ques_no+1
        lblQues["text"] = "Question " + str(ques)
        lblMark["text"] = "Positive: " + str(quesData[ques_no][5]) + " Marks  Negative: " + str(
            quesData[ques_no][6]) + " Marks"
        lblQ["text"] = quesData[ques_no][0]
        radio1.config(text=quesData[ques_no][1],value=quesData[ques_no][1])
        radio2.config(text=quesData[ques_no][2],value=quesData[ques_no][2])
        radio3.config(text=quesData[ques_no][3],value=quesData[ques_no][3])
        radio4.config(text=quesData[ques_no][4],value=quesData[ques_no][4])

    quesData = quiz_userview.get_ques(mod)
    mainQuiz=Toplevel(root)
    mainQuiz.state("z")
    lblColor=tkinter.Label(mainQuiz,bg="white",height=3)
    lblColor.pack(fill=X)
    lblhead1=tkinter.Label(lblColor,text="Quiz on "+mod,font=("tahoma",20,"bold"),bg="white")
    lblhead1.place(x=10,y=0)
    lblColor2=tkinter.Label(mainQuiz,bg="grey",height=2)
    lblColor2.pack(fill=X)
    lblColor3=tkinter.Label(mainQuiz,bg="black",height=2,width=150)
    lblColor3.place(relx=0,rely=0.123)
    lblColor4=tkinter.Label(mainQuiz,bg="white",height=2,width=150)
    lblColor4.place(relx=0,rely=0.175)
    lblColor4.pack_propagate(0)
    lblColor5=tkinter.Label(mainQuiz,bg="grey",height=2,width=150)
    lblColor5.place(relx=0,rely=0.225)
    lblColor5.pack_propagate(0)
    btn1=tkinter.Button(lblColor5,text="Easy",bg="yellow",font=("arial",15,"bold"),width=8,command=easyBtnclick)
    btn1.pack(side="left")
    btn2=tkinter.Button(lblColor5,text="Medium",bg="yellow",font=("arial",15,"bold"),width=8,command=mediumBtnclick)
    btn2.pack(side="left")
    btn3=tkinter.Button(lblColor5,text="Hard",bg="yellow",font=("arial",15,"bold"),width=8,command=hardBtnclick)
    btn3.pack(side="left")
    lblColor6=tkinter.Label(mainQuiz,bg="blue",height=2,width=150)
    lblColor6.place(relx=0,rely=0.275)
    lblColor7=tkinter.Label(mainQuiz,bg="grey",height=2,width=150)
    lblColor7.place(relx=0,rely=0.32)
    lblColor7.pack_propagate(0)
    lblQues=tkinter.Label(lblColor7,bg="grey",font=("arial",15,"bold"))
    lblQues.pack(side="left",padx=10)
    lblMark=tkinter.Label(lblColor7,bg="grey",font=("arial",15,"bold"),fg="red")
    lblMark.pack(side="right",padx=10)
    lblQFrame=tkinter.Frame(mainQuiz,height=500,width=1200,bg="white")
    lblQFrame.place(relx=0,rely=0.37)
    lblQFrame.pack_propagate(0)
    lblQ=tkinter.Label(lblQFrame,font=("arial",15,"bold"),bg="white")
    lblQ.place(relx=0.03,rely=0.05)
    var=StringVar()
    var.set("empty")
    radio1=tkinter.Radiobutton(lblQFrame,variable=var,bg="white",font=("arial",13,'bold'),command=check_radio)
    radio2=tkinter.Radiobutton(lblQFrame,variable=var,bg="white",font=("arial",13,'bold'),command=check_radio)
    radio3=tkinter.Radiobutton(lblQFrame,variable=var,bg="white",font=("arial",13,'bold'),command=check_radio)
    radio4=tkinter.Radiobutton(lblQFrame,variable=var,bg="white",font=("arial",13,'bold'),command=check_radio)
    radio1.place(relx=0.03,rely=0.2)
    radio2.place(relx=0.03,rely=0.3)
    radio3.place(relx=0.03,rely=0.4)
    radio4.place(relx=0.03,rely=0.5)

    lblColor8=tkinter.Label(mainQuiz,bg="grey",width=150,height=2)
    lblColor8.place(relx=0,rely=0.9)
    lblColor8.pack_propagate(0)
    btnPre=tkinter.Button(lblColor8,text="Previous",bg="yellow",font=("arial",15,"bold"),width=8,command=Btnclick_previous,state=NORMAL)
    btnPre.pack(side="left",padx=20)
    btnNext=tkinter.Button(lblColor8,text="Next",bg="yellow",font=("arial",15,"bold"),width=8,state=NORMAL,command=Btnclick_next)
    btnNext.pack(side="left")
    btnSave=tkinter.Button(lblColor8,text="Save and Next",bg="yellow",font=("arial",15,"bold"),command=Btnclick_save,state=DISABLED)
    btnSave.pack(side="right",padx=20)
    btnClear=tkinter.Button(lblColor8,text="Clear Response",bg="yellow",font=("arial",15,"bold"),command=Btnclick_clear,state=DISABLED)
    btnClear.pack(side="top")
    lblColor9=tkinter.Label(mainQuiz,bg="blue",height=2,width=200)
    lblColor9.pack(side="bottom")
    rFrame=tkinter.Frame(mainQuiz,width=310,bg="green")
    rFrame.pack(fill=Y,side="right")
    rFrame.pack_propagate(0)
    lblR=tkinter.Label(rFrame,text="Easy",bg="blue",height=1,font=("arial",20),fg="white")
    lblR.pack(side="left",fill=X,expand=True)

    btns1=tkinter.Button(rFrame,font=("arial",15,"bold"),height=1,width=3,command=lambda :btnMenu_click(1))
    btns1.place(relx=0.1,rely=0.57)
    btns2=tkinter.Button(rFrame,font=("arial",15,"bold"),height=1,width=3,command=lambda :btnMenu_click(2))
    btns2.place(relx=0.35,rely=0.57)
    btns3=tkinter.Button(rFrame,font=("arial",15,"bold"),height=1,width=3,command=lambda :btnMenu_click(3))
    btns3.place(relx=0.6,rely=0.57)
    btns4=tkinter.Button(rFrame,font=("arial",15,"bold"),height=1,width=3,command=lambda :btnMenu_click(4))
    btns4.place(relx=0.82,rely=0.57)
    btns5=tkinter.Button(rFrame,font=("arial",15,"bold"),height=1,width=3,command=lambda :btnMenu_click(5))
    btns5.place(relx=0.1,rely=0.7)

    btnSubmit=tkinter.Button(rFrame,text="Submit",font=("arial",15,"bold"),width=13,bg="blue",command=BtnSubmit_click)
    btnSubmit.place(relx=0.3,rely=0.9)
    easyBtnclick()

    # Btnclick_clear()

    # global totalMin
    # global totalSec
    # global totalTime
    # totalMin = 1
    # totalSec = 60
    #
    # def changeTime():
    #
    #     if (len(str(totalMin)) == 1 and len(str(totalSec)) != 1):
    #         totalTime = "0" + str(totalMin) + ":" + str(totalSec)
    #     elif (len(str(totalSec)) == 1 and len(str(totalMin)) != 1):
    #         totalTime = str(totalMin) + ": 0" + str(totalSec)
    #     elif (len(str(totalMin)) == 1 and len(str(totalSec)) == 1):
    #         totalTime = "0" + str(totalMin) + ": 0" + str(totalSec)
    #     else:
    #         totalTime = str(totalMin) + ":" + str(totalSec)
    #     lblTime["text"]="Time Left: " + totalTime
    #
    # totalTime = "0" + str((totalMin + 1)) + ": 0" + str((totalSec - 60))
    # lblTime = tkinter.Label(lblColor4, text="Time Left: " + totalTime, bg="white", font=("arial", 15, "bold"))
    # lblTime.pack(side="right")
    #
    # while (totalSec != 0):
    #     time.sleep(1)
    #     totalSec -= 1
    #     if (totalSec == 0 and totalMin != 0):
    #         changeTime()
    #         totalMin -= 1
    #         totalSec = 59
    #         time.sleep(1)
    #     elif (totalSec == 0 and totalMin == 0):
    #         changeTime()
    #         break
    #
    #     changeTime()
    # print("time over")

    mainQuiz.mainloop()

def result():
    global attempted, correct, score, incorrect
    resultPage=Toplevel(root,bg="white")
    resultPage.state("z")
    lblR=tkinter.Label(resultPage,text="Your Result",font=("times",50,"bold"),bg="white")
    lblR.place(relx=0.4,rely=0.1)
    lblR1 = tkinter.Label(resultPage, text="Total questions attempted"+"\t"+str(attempted), font=("times", 20, "bold"),bg="white")
    lblR1.place(relx=0.3, rely=0.3)
    lblR2 = tkinter.Label(resultPage, text="Total correct answers"+"\t"+str(correct), font=("times", 20, "bold"),bg="white")
    lblR2.place(relx=0.3, rely=0.4)
    lblR3 = tkinter.Label(resultPage, text="Total wrong answers"+"\t"+str(incorrect), font=("times", 20, "bold"),bg="white")
    lblR3.place(relx=0.3, rely=0.5)
    lblR4 = tkinter.Label(resultPage, text="Score"+"\t"+str(score), font=("times", 30, "bold"),bg="white")
    lblR4.place(relx=0.4, rely=0.6)
    lblBtn=tkinter.Button(resultPage,text="Play again",font=("times",20,"bold"))
    lblBtn.config(bg="green", fg="white", command=homePageUser)
    lblBtn.place(relx=0.45,rely=0.8)
    resultPage.mainloop()
# main code

root.state("zoomed")
lblHead = tkinter.Label(root, text="ONLINE QUIZ SYSTEM", fg="#4dd2ff", bg="#ffffcc")
lblHead.config(font=("Times", 50, "italic"))
lblHead.place(x=340, y=60)
root.config(bg="#ffffcc")
first_page()
root.mainloop()
