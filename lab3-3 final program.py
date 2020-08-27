from tkinter import *
from tkinter.ttk import *
import pymysql
import tkinter.messagebox
import tkinter.font

class Main:
    screen = None
    def __init__(self):
        # 윈도우 창 생성
        self.screen = Tk()
        self.screen.title("League of Legend")
        self.screen.geometry('400x400')
        # MySQL 연결
        self.conn = pymysql.connect(host = 'localhost', user = 'root', password = 'dgu1234!' ,db = 'lab5',autocommit = True)
        self.curs = self.conn.cursor()
        # 처음 시작창

        self.font_first = tkinter.font.Font(size=15)
        self.id_check = StringVar()
        self.id_label = Label(self.screen, text='Please Input your ID',font = self.font_first)
        self.id_entry = Entry(self.screen, textvariable = self.id_check,width = 40)
        self.id_entry.insert(0,'Username')
        self.pw_label = Label(self.screen, text = 'Please Input your PASSWORD',font = self.font_first)
        self.pw_check = StringVar()
        self.pw_entry = Entry(self.screen, show = '*',textvariable = self.pw_check,width = 40)
        self.bt_login = Button(self.screen, text = 'Login',command = self.User_check)
        self.bt_signup = Button(self.screen, text = 'Sign Up',command = self.User_signup)
        self.bt_quit = Button(self.screen, text = 'Exit',command = quit)

        # Sign UP 버튼 누른 경우 보이는 창
        self.id_make = Label(self.screen, text = 'ID : ',font = self.font_first)
        self.id_input = StringVar()
        self.id_make_entry = Entry(self.screen, textvariable = self.id_input)
        self.pw_make = Label(self.screen, text='Password : ',font = self.font_first)
        self.pw_input = StringVar()
        self.pw_make_entry = Entry(self.screen, show = '*',textvariable = self.pw_input)
        self.nm_make = Label(self.screen, text='NAME : ',font = self.font_first)
        self.nm_input = StringVar()
        self.nm_make_entry = Entry(self.screen, textvariable=self.nm_input)
        self.age_make = Label(self.screen, text='Age : ',font = self.font_first)
        self.age_input = StringVar()
        self.age_make_entry = Entry(self.screen, textvariable=self.age_input)
        self.bt_overlap = Button(self.screen, text = 'Check Id',command = self.User_overlap)
        self.bt_make = Button(self.screen, text = 'Make ID!',command = self.User_make)
        self.bt_user_back = Button(self.screen, text = 'Back', command = self.reLogin)
        # 로그인한 후 보이는 창
        self.photo = PhotoImage(file="1q2w.png")
        self.back = Label(self.screen, image=self.photo)
        self.bt_exit = Button(self.screen, text = 'Exit',command = quit)
        self.bt_signout = Button(self.screen, text='LogOut', command = self.Log_out)
        self.bt_bill = Button(self.screen, text = 'Billing/RP\nIssue',command = self.RP_show)
        self.bt_get_tech = Button(self.screen, text = 'GET TECH HELP',command = self.TC_show)
        self.bt_report = Button(self.screen, text = 'REPORT A PLAYER',command = self.RE_show)
        self.lb_question1 = Label(self.screen, text = 'Can’t find what you’re looking for?',font = self.font_first)
        self.lb_question2 = Label(self.screen, text="From tech to tilt, we're here to help you! Submit a Ticket!\n So long as a poro doesn't eat it,\n we'll get back to you soon.",font = self.font_first)
        self.bt_ticket = Button(self.screen, text = 'SUBMIT A TICKET!',command = self.SB_show)
        self.bt_myinfrom = Button(self.screen, text = 'Change\nMy Infromation',command = self.CH_show)

        # RP버튼 누른 후 보이는 창
        self.font_rp = tkinter.font.Font(size = 13)
        self.font_rp2 = tkinter.font.Font(size=20)
        self.list_rp = []
        self.lb_rp_detail = None
        self.lb_rp_content = None
        self.rp_title = Label(self.screen, text = 'RP', font = self.font_rp2)
        self.comb_rp = Combobox(self.screen, values=self.list_rp, width = 200, height = 30)
        self.rp_input = StringVar()
        self.bt_rp = Button(self.screen, text='Click Me',command = self.RP_click)
        self.bt_rp_go_main = Button(self.screen, text = 'Goto Main',command = self.RP_back)
        # Tech버튼 누른 후 보이는 창
        self.font_tc2 = tkinter.font.Font(size=20)
        self.font_tc = tkinter.font.Font(size=13)
        self.list_tc = []
        self.lb_tc_detail = None
        self.lb_tc_content = None
        self.tc_title = Label(self.screen, text='Get Tech Help', font=self.font_tc2)
        self.comb_tc = Combobox(self.screen, values=self.list_tc, width=200, height=30)
        self.tc_input = StringVar()
        self.bt_tc = Button(self.screen, text='Click Me', command=self.TC_click)
        self.bt_tc_go_main = Button(self.screen, text='Goto Main', command=self.TC_back)
        # Report 버튼 누른 후 보이는 창
        self.font_re2 = tkinter.font.Font(size=20)
        self.font_re = tkinter.font.Font(size=13)
        self.list_re = ['NEGATIVE ATTITUDE', 'VERBAL ABUSE', 'LEAVING/AFK', 'ASSISTING ENEMY TEAM','HATE SPEECH']
        self.lb_re_detail = None
        self.lb_re_content = None
        self.re_input = StringVar()
        self.comb_re = Combobox(self.screen, values=self.list_re, textvariable = self.re_input, width=100, state='readonly')
        self.bt_re = Button(self.screen, text='Late Report',command = self.RE_submit)
        self.bt_re_go_main = Button(self.screen, text='Goto Main', command=self.RE_back)
        self.lb_re_name = Label(self.screen, text = 'Nickname')
        self.re_name_input = StringVar()
        self.re_name_entry = Entry(self.screen, textvariable = self.re_name_input, width = 103)
        self.re_reason_input = StringVar()
        self.re_reason_text = Text(self.screen, width = 103, height = 30)
        self.re_reason_input = self.re_reason_text.get('1.0', END)
        #Change My information 버튼 누른 후 보이는 창
        self.font_ch = tkinter.font.Font(size=20)
        self.lb_ch_nickname = Label(self.screen)
        self.lb_ch_nick = Label(self.screen, text = 'Nickname',font = self.font_ch)
        self.lb_ch_password = Label(self.screen, text = 'Password',font = self.font_ch)
        self.lb_ch_name = Label(self.screen, text = 'Name',font = self.font_ch)
        self.lb_ch_age = Label(self.screen, text = 'Age',font = self.font_ch)
        self.ch_password_insert = StringVar()
        self.ch_name_insert = StringVar()
        self.ch_age_insert = StringVar()
        self.ch_password_entry = Entry(self.screen, textvariable = self.ch_password_insert,show = '*')
        self.ch_name_entry = Entry(self.screen, textvariable = self.ch_name_insert)
        self.ch_age_entry = Entry(self.screen, textvariable = self.ch_age_insert)
        self.bt_change = Button(self.screen, text = 'Chage Information',command = self.CH_save)
        self.bt_ch_go_main = Button(self.screen, text = 'Goto Main',command = self.CH_back)
        #submit 제출 버튼 누른 후 보이는 창
        self.font_sb = tkinter.font.Font(size=15)
        self.lb_sb_kind = Label(self.screen, text = '1. CHOOSE A REQUEST TYPE',font = self.font_sb)
        self.sb_input = StringVar()
        self.comb_sb = Combobox(self.screen, values =['Report','Technical', 'RP'], textvariable = self.sb_input, width=100, state='readonly')
        self.lb_sb_subject = Label(self.screen, text = 'Subject',font = self.font_sb)
        self.sb_subject_input = StringVar()
        self.sb_subject_entry = Entry(self.screen, textvariable = self.sb_subject_input)
        self.sb_description_input = StringVar()
        self.sb_description_text = Text(self.screen, width = 103, height = 30)
        self.bt_go_main = Button(self.screen, text = 'Goto Main',command = self.SB_back)
        self.bt_submit = Button(self.screen, text = 'Submit!',command = self.SB_click)




    # 시작 창
    def User(self):

        self.id_label.pack()
        self.id_entry.pack()
        self.pw_label.pack()
        self.pw_entry.pack()
        self.bt_login.pack()
        self.bt_signup.pack()
        self.bt_quit.pack()

    # User 창 삭제
    def User_delete(self):

        self.id_label.pack_forget()
        self.id_entry.pack_forget()
        self.pw_label.pack_forget()
        self.pw_entry.pack_forget()
        self.bt_login.pack_forget()
        self.bt_signup.pack_forget()
        self.bt_quit.pack_forget()

    # Employee버튼 누른 경우 보이는 창
    # def Employee(self):
    #     self.bt_user.pack_forget()
    #     self.bt_employee.pack_forget()

    # User에서 ID, PW 확인
    def User_check(self):
        sql = "select * from Player where nickname=%s and password=%s"
        self.curs.execute(sql, (self.id_check.get(),self.pw_check.get()))
        self.check_id = self.curs.fetchall()
        if self.check_id == tuple():
            tkinter.messagebox.showinfo("WARNNIG","ID OR Password is wrong!!\nPlease check your ID OR Password.")
        else:
            self.User_show()



    # User에서 Singup누른 경우 보이는 창
    def User_signup(self):
        self.User_delete()
        self.id_make.pack()
        self.id_make_entry.pack()
        self.bt_overlap.pack()
        self.pw_make.pack()
        self.pw_make_entry.pack()
        self.nm_make.pack()
        self.nm_make_entry.pack()
        self.age_make.pack()
        self.age_make_entry.pack()
        self.bt_make.pack()
        self.bt_user_back.pack()

    # Sign up창 삭제
    def signup_delete(self):
        self.id_make.pack_forget()
        self.id_make_entry.pack_forget()
        self.bt_overlap.pack_forget()
        self.pw_make.pack_forget()
        self.pw_make_entry.pack_forget()
        self.nm_make.pack_forget()
        self.nm_make_entry.pack_forget()
        self.age_make.pack_forget()
        self.age_make_entry.pack_forget()
        self.bt_make.pack_forget()
        self.bt_user_back.pack_forget()

    # Signup에서 ID중복 확인
    def User_overlap(self):
        sql = "select * from Player where nickname=%s"
        self.curs.execute(sql, (self.id_make_entry.get()))
        self.check = self.curs.fetchall()
        if self.check == tuple():
            tkinter.messagebox.showinfo("Good", "You can use this Id!")
        else:
            tkinter.messagebox.showinfo("Check", "You can't use this Id!\nPlease input another Id.")

    # Sign up 완료 + DB에 추가
    def User_make(self):
        sql = "insert into Player(nickname, name, age, password) values(%s,%s,%s,%s)"
        self.pw_blank = str(self.pw_input.get())
        self.age_blank = str(self.age_input.get())
        self.id_blank = str(self.id_input.get())
        self.nm_blank = str(self.nm_input.get())
        if self.pw_make == '' or self.age_blank == '' or self.id_blank == '' or self.nm_blank == '':
            tkinter.messagebox.showinfo("Error", "Please insert Blank!")
        else:
            self.curs.execute(sql, (self.id_input.get(),self.nm_input.get(),self.age_input.get(),self.pw_input.get()))
            self.check = self.curs.fetchall()
            tkinter.messagebox.showinfo("Good", "Please Login!")
            self.reLogin()

    # Sign up 이후 로그인창
    def reLogin(self):
        self.signup_delete()
        self.User()

    #
    def User_back(self):
        self.User_delete()
        self.Start()

    # User에서 로그인한 경우 보이는 창
    def User_show(self):
        self.User_delete()
        self.screen.geometry('1440x811')
        self.back.pack()
        self.bt_myinfrom.place(x=250, y=300, width=120, height=120)
        self.bt_bill.place(x=450,y=300, width=120, height=120)
        self.bt_get_tech.place(x=850,y=300, width=120, height=120)
        self.bt_report.place(x=1050,y=300, width=120, height=120)
        self.lb_question1.place(x=560,y=500, width=320, height=30)
        self.lb_question2.place(x=560,y=600, width=320)
        self.bt_ticket.place(x=560,y=700, width=320, height=30)
        self.bt_exit.place(x = 1200,y=100)
        self.bt_signout.place(x=1300,y=100)


    # User창 안보이게
    def User_show_delete(self):
        self.bt_bill.place_forget()
        self.bt_get_tech.place_forget()
        self.bt_myinfrom.place_forget()
        self.bt_report.place_forget()
        self.lb_question1.place_forget()
        self.lb_question2.place_forget()
        self.bt_ticket.place_forget()

    def Log_out(self):
        self.User_show_delete()
        self.back.pack_forget()
        self.RP_delete()
        self.TC_delete()
        self.CH_delete()
        self.SB_delete()
        self.screen.geometry('400x400')
        self.User()


    #RP 버튼 클릭후 보이는 창
    def RP_show(self):
        self.User_show_delete()
        sql = "select * from answer where kind=%s"
        self.curs.execute(sql, ('RP'))
        self.check = self.curs.fetchall()
        for i in self.check:
            self.list_rp.append(i[2])
        self.comb_rp = Combobox(self.screen, values=self.list_rp,textvariable = self.rp_input, width = 120, state='readonly')
        self.comb_rp.place(x =100,y=200)
        self.bt_rp.place(x=1000,y=200)
        self.bt_rp_go_main.place(x = 1200, y = 100)

    # RP 내용 보여줌
    def RP_click(self):
        if self.lb_rp_content != None:
            self.lb_rp_content.place_forget()
            self.lb_rp_detail.place_forget()
        self.lb_rp_detail = Label(self.screen, text= self.rp_input.get(),font = self.font_rp)
        self.lb_rp_detail.place(x=100, y=300)
        sql = "select * from answer where detail=%s"
        self.curs.execute(sql, (self.rp_input.get()))
        self.check = self.curs.fetchall()
        for i in self.check:
            self.lb_rp_content = Label(self.screen, text = i[3],font = self.font_rp)
        self.lb_rp_content.place(x=100, y=400)

    # Rp 내용 삭제
    def RP_delete(self):
        self.comb_rp.place_forget()
        self.bt_rp.place_forget()
        self.bt_rp_go_main.place_forget()
        if self.lb_rp_content != None:
            self.lb_rp_content.place_forget()
            self.lb_rp_detail.place_forget()

    # 메인창으로 이동
    def RP_back(self):
        self.RP_delete()
        self.User_show()

    # Tech 버튼 클릭후 보이는 창
    def TC_show(self):
        self.User_show_delete()
        sql = "select * from answer where kind=%s"
        self.curs.execute(sql, ('Get Tech'))
        self.check = self.curs.fetchall()
        for i in self.check:
            self.list_tc.append(i[2])
        self.comb_tc = Combobox(self.screen, values=self.list_tc, textvariable=self.tc_input, width=120, state='readonly')
        self.comb_tc.place(x=100, y=200)
        self.bt_tc.place(x=1000, y=200)
        self.bt_tc_go_main.place(x=1200, y=100)

    # Tech 내용 보여줌
    def TC_click(self):
        if self.lb_tc_content != None:
            self.lb_tc_content.place_forget()
            self.lb_tc_detail.place_forget()
        self.lb_tc_detail = Label(self.screen, text=self.tc_input.get(),font = self.font_ch)
        self.lb_tc_detail.place(x=100, y=300)
        sql = "select * from answer where detail=%s"
        self.curs.execute(sql, (self.tc_input.get()))
        self.check = self.curs.fetchall()
        for i in self.check:
            self.lb_tc_content = Label(self.screen, text=i[3],font = self.font_ch)
        self.lb_tc_content.place(x=100, y=400)

    # Tech 내용 삭제
    def TC_delete(self):
        self.comb_tc.place_forget()
        self.bt_tc.place_forget()
        self.bt_tc_go_main.place_forget()
        if self.lb_tc_content != None:
            self.lb_tc_content.place_forget()
            self.lb_tc_detail.place_forget()

    # 메인창으로 이동
    def TC_back(self):
        self.TC_delete()
        self.User_show()

    #Report 보이는 창
    def RE_show(self):
        self.User_show_delete()
        sql = "select * from answer where kind=%s"
        self.curs.execute(sql, ('Report'))
        self.check = self.curs.fetchall()
        for i in self.check:
            self.lb_re_detail = Label(self.screen, text = i[2],font = self.font_re2)
            self.lb_re_content = Label(self.screen, text=i[3])
        self.lb_re_detail.place(x = 100, y = 50)
        self.lb_re_content.place(x = 100, y = 100)
        self.lb_re_name.place(x = 100,y = 130)
        self.re_name_entry.insert(0,'Nickname')
        self.re_name_entry.place(x = 100, y = 150)
        self.comb_re.place(x=100, y=200)
        self.re_reason_text.place(x=100,y=250)
        self.bt_re.place(x=100, y=700)
        self.bt_re_go_main.place(x=1200, y=100)

    # Report 내용 제출
    def RE_submit(self):
        self.re_reason_input = self.re_reason_text.get('1.0', END)
        self.re_input_blank = str(self.re_input.get())
        self.re_name_blank = str(self.re_name_input.get())
        self.re_reason_blank = str(self.re_reason_input)
        if self.re_input_blank == '' or self.re_name_blank == '' or self.re_reason_blank == '':
            tkinter.messagebox.showinfo("Error", "Please insert Blank!")
        else:
            sql = "insert into qna values (%s,%s,%s, %s, %s)"
            self.detail = str(self.re_input.get()) + " : " + str(self.re_name_input.get())
            self.curs.execute(sql, (0,self.id_check.get(),'Report',self.detail,self.re_reason_input))
            self.check = self.curs.fetchall()
            tkinter.messagebox.showinfo("Complete", "Thank you for Report!")
            self.RE_back()

    # Report 내용 삭제
    def RE_delete(self):
        self.lb_re_detail.place_forget()
        self.lb_re_content.place_forget()
        self.re_name_entry.place_forget()
        self.comb_re.place_forget()
        self.re_reason_text.place_forget()
        self.bt_re.place_forget()
        self.bt_re_go_main.place_forget()
        self.lb_re_name.place_forget()

    # 메인창으로 이동
    def RE_back(self):
        self.RE_delete()
        self.User_show()

    # Change my information
    def CH_show(self):
        self.User_show_delete()
        self.lb_ch_name.place(x = 400, y = 300)
        self.lb_ch_password.place(x = 400, y = 350)
        self.ch_password_entry.place(x=600,y = 350)
        self.lb_ch_name.place(x=400, y=400)
        self.ch_name_entry.place(x=600, y=400)
        self.lb_ch_age.place(x=400, y=450)
        self.ch_age_entry.place(x=600,y=450)
        self.bt_change.place(x = 400, y = 500)
        self.bt_ch_go_main.place(x=1200, y=100)
        sql = "select * from Player where nickname=%s"
        self.curs.execute(sql, (self.id_check.get()))
        self.check = self.curs.fetchall()
        for i in self.check:
            self.lb_ch_nickname = Label(self.screen, text = i[0])
            self.ch_name_entry.delete(0,END)
            self.ch_age_entry.delete(0, END)
            self.ch_name_entry.insert(0,i[1])
            self.ch_age_entry.insert(0,i[2])
        self.lb_ch_nick.place(x=400,y = 250)
        self.lb_ch_nickname.place(x=600,y=250)

    # 변경한 정보 저장
    def CH_save(self):
        sql = "update Player set name = %s , age = %s, password = %s where nickname=%s"
        self.curs.execute(sql, (self.ch_name_insert.get(),self.ch_age_insert.get(),self.ch_password_insert.get(),self.id_check.get()))
        self.check = self.curs.fetchall()
        tkinter.messagebox.showinfo("Good", "Change your information!")
        self.CH_back()

    # CH 창 삭제
    def CH_delete(self):
        self.lb_ch_name.place_forget()
        self.lb_ch_password.place_forget()
        self.ch_password_entry.place_forget()
        self.lb_ch_name.place_forget()
        self.ch_name_entry.place_forget()
        self.lb_ch_age.place_forget()
        self.ch_age_entry.place_forget()
        self.bt_change.place_forget()
        self.bt_ch_go_main.place_forget()
        self.lb_ch_nickname.place_forget()
        self.lb_ch_nick.place_forget()
        self.lb_ch_nickname.place_forget()

    # CH 메인창으로
    def CH_back(self):
        self.CH_delete()
        self.User_show()

    # Submit 제출창
    def SB_show(self):
        self.User_show_delete()
        self.lb_sb_kind.place(x=100,y=50)
        self.comb_sb.place(x=100,y=100)
        self.lb_sb_subject.place(x=100,y=150)
        self.sb_subject_entry.place(x=100,y=200)
        self.sb_description_text.place(x=100,y=250)
        self.bt_go_main.place(x=1200,y=100)
        self.bt_submit.place(x=100,y=700)

    # Submit 제출
    def SB_click(self):
        self.sb_description_input = self.sb_description_text.get('1.0', END)
        self.sb_input_blank = str(self.sb_input.get())
        self.sb_subject_blank = str(self.sb_subject_input.get())
        self.sb_description_blank = str(self.sb_description_input)
        if self.sb_input_blank == '' or self.sb_subject_blank == '' or self.sb_description_blank == '':
            tkinter.messagebox.showinfo("Error", "Please insert Blank!")
        else:
            self.sb_description_input = self.sb_description_text.get('1.0',END)
            sql = "insert into qna values(%s,%s,%s,%s,%s)"
            self.curs.execute(sql, (0,self.id_check.get(),self.sb_input.get(),self.sb_subject_input.get(),self.sb_description_input))
            self.check = self.curs.fetchall()
            tkinter.messagebox.showinfo("Complete", "Thank you for Question!\nwe will reply your submit fastly!")
            self.SB_back()

    # Submit 제출창 없애기
    def SB_delete(self):
        self.lb_sb_kind.place_forget()
        self.comb_sb.place_forget()
        self.lb_sb_subject.place_forget()
        self.sb_subject_entry.place_forget()
        self.sb_description_text.place_forget()
        self.bt_go_main.place_forget()
        self.bt_submit.place_forget()

    # Submit창에서 Main 창으로
    def SB_back(self):
        self.SB_delete()
        self.User_show()

a = Main()
a.User()
a.screen.mainloop()


# screen = Tk()
# screen.geometry('400x400')
#
# bt_user = Button(screen, text='User')
# bt_user.pack()
# bt_employee = Button(screen, text='Employee')
# bt_employee.pack()
#
# screen.mainloop()
# conn = pymysql.connect(host = 'localhost', user = 'root', password = 'dgu1234' ,db = 'lab3')
# # host = DB주소(localhost 또는 ip주소), user = DB id, password = DB password, db = DB명
# curs = conn.cursor()
#
# sql = "SELECT * FROM Department" # 실행 할 쿼리문 입력
# curs.execute(sql) # 쿼리문 실행
#
# rows = curs.fetchall() # 데이터 패치
#
# sql2 = "SELECT * FROM Support WHERE location = %s"
# curs.execute(sql2, ('Hong kong'))
