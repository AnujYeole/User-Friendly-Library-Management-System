from importlib.resources import contents
from tkinter import*
from tkinter import ttk
from tkinter import Scrollbar
import tkinter
import mysql.connector
from tkinter import messagebox
import datetime

from sql import Values


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("GES's HPT ARTS AND RYK SCIENCE COLLEGE,NASHIK,05")
        self.root.geometry("1550x800+0+0")

        '''VARIABLE'''
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.title_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.pincode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.auther_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latefine_var = StringVar()
        self.dateoverduue_var = StringVar()
        self.actualprice_var = StringVar()

        lbltitle = Label(self.root, text="BHAUSAHEB VARTAK LIBRARY", bg="powder blue", fg="green",
                         bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE,
                      padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)
        # ============================Dataframeleft=================================
        DataFrameLeft = LabelFrame(frame, text="Library Membership information", bg="powder blue",
                                   fg="black", bd=12, relief=RIDGE, font=("times new roman", 12, "bold"), padx=2, pady=6)
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblMember = Label(DataFrameLeft, bg="powder blue", text="Member type", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.member_var, width=27, state="readonly")
        comMember["value"] = ("Admin Staff", "Teaching Staff", "Student")
        comMember.grid(row=0, column=1)

        lblPRN_No = Label(DataFrameLeft, bg="powder blue", text="PRN NO", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.prn_var, width=29)
        txtPRN_No.grid(row=1, column=1)

        lblTitle = Label(DataFrameLeft, bg="powder blue", text="Dept Name", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.title_var, width=29)
        txtTitle.grid(row=2, column=1)

        comMember1 = ttk.Combobox(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.title_var, width=27, state="readonly")
        comMember1["value"] = ("Computer Science", "Physics", "Microbiology")
        comMember1.grid(row=2, column=1)

        lblFirstname = Label(DataFrameLeft, bg="powder blue", text="First Name", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblFirstname.grid(row=3, column=0, sticky=W)
        txtFirstname = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.firstname_var, width=29)
        txtFirstname.grid(row=3, column=1)

        lblLastname = Label(DataFrameLeft, bg="powder blue", text="Last Name", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblLastname.grid(row=4, column=0, sticky=W)
        txtLastname = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.lastname_var, width=29)
        txtLastname.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, bg="powder blue", text="Address1", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.address1_var, width=29)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, bg="powder blue", text="Address2", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.address2_var, width=29)
        txtAddress2.grid(row=6, column=1)

        lblPincode = Label(DataFrameLeft, bg="powder blue", text="Pin Code", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblPincode.grid(row=7, column=0, sticky=W)
        txtPincode = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.pincode_var, width=29)
        txtPincode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, bg="powder blue", text="Mobile No", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.mobile_var, width=29)
        txtMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, bg="powder blue", text="Book ID", font=(
            "times new roman", 12, "bold"), padx=2)
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.bookid_var, width=29)
        txtBookId.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, bg="powder blue", text="Book Title", font=(
            "times new roman", 12, "bold"), padx=2)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.booktitle_var, width=29)
        txtBookTitle.grid(row=1, column=3)

        lblAuthor = Label(DataFrameLeft, bg="powder blue", text="Author Name", font=(
            "times new roman", 12, "bold"), padx=2)
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.auther_var, width=29)
        txtAuthor.grid(row=2, column=3)

        lblDateBorrowed = Label(DataFrameLeft, bg="powder blue", text="Date Borrowed", font=(
            "times new roman", 12, "bold"), padx=2)
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.dateborrowed_var, width=29)
        txtDateBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, bg="powder blue", text="Date Due", font=(
            "times new roman", 12, "bold"), padx=2)
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.dateoverduue_var, width=29)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, bg="powder blue", text="Days On Book", font=(
            "times new roman", 12, "bold"), padx=2)
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.daysonbook_var, width=29)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, bg="powder blue", text="Late Return Fine", font=(
            "times new roman", 12, "bold"), padx=2)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.latefine_var, width=29)
        txtLateReturnFine.grid(row=6, column=3)

        lblOverDue = Label(DataFrameLeft, bg="powder blue", text="Status", font=(
            "times new roman", 12, "bold"), padx=2)
        lblOverDue.grid(row=7, column=2, sticky=W)
        txtOverDue = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.dateoverduue_var, width=29)
        txtOverDue.grid(row=7, column=3)
        comMember = ttk.Combobox(DataFrameLeft, font=(
            "times new roman", 12, "bold"), width=27, state="readonly")
        comMember["value"] = ("ISSUED", "RETURNED")
        comMember.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, bg="powder blue", text="Actual Price", font=(
            "times new roman", 12, "bold"), padx=2)
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=(
            "times new roman", 12, "bold"), textvariable=self.actualprice_var, width=29)
        txtActualPrice.grid(row=8, column=3)

# ====================================DataFrameRiGht===================================================
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue",
                                    fg="black", bd=12, relief=RIDGE, font=("arial", 12, "bold"), padx=2, pady=6)
        DataFrameRight.place(x=870, y=5, width=580, height=350)

        self.txtBox = Text(DataFrameRight, font=(
            "arial", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollBar = Scrollbar(DataFrameRight)
        listScrollBar.grid(row=0, column=1, sticky="ns")

        listBooks = ["PHP", "Python", "DBMS",
                     "FDS", "TCS", "BT", "OOP", "OS", "CN","The Feynman",
                     "Relativity","Basic Physics","Medical Microbiology",
                     "Clinical Microbiology","Medical","Clean Code","AI","ML","Java Script"]

        def SelectBook(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if(x == 'PHP'):
                self.bookid_var.set("BKID54")
                self.booktitle_var.set("Web Technologies")
                self.auther_var.set("Prof Shaikh")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.datedue_var.set("NO")
                self.actualprice_var.set("Rs.788")

            elif(x == 'Python'):
                self.bookid_var.set("BKID55")
                self.booktitle_var.set("Pytho Programming")
                self.auther_var.set(" Prof Nikam")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.datedue_var.set("NO")
                self.actualprice_var.set("Rs.700")

            elif(x == 'DBMS'):
                self.bookid_var.set("BKID56")
                self.booktitle_var.set("Mysql")
                self.auther_var.set("Mrs Joshi")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.datedue_var.set("NO")
                self.actualprice_var.set("Rs.700")

            elif(x == 'FDS'):
                self.bookid_var.set("BKID57")
                self.booktitle_var.set("Foundation of Data Science")
                self.auther_var.set("Prof Mrs Chavan")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.datedue_var.set("NO")
                self.actualprice_var.set("Rs.800")

            elif(x == 'TCS'):
                self.bookid_var.set("BKID58")
                self.booktitle_var.set("Theory of Computer Sciencee")
                self.auther_var.set("Prof Mrs Dhande")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.datedue_var.set("NO")
                self.actualprice_var.set("Rs.800")

            elif(x == 'BT'):
                self.bookid_var.set("BKID59")
                self.booktitle_var.set("Blockchain Technology")
                self.auther_var.set("Prof Mrs Joshi")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.datedue_var.set("NO")
                self.actualprice_var.set("Rs.800")

            elif(x == 'OOP'):
                self.bookid_var.set("BKID60")
                self.booktitle_var.set("OOP's Using Java")
                self.auther_var.set("Prof Mrs Kawale")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.datedue_var.set("NO")
                self.actualprice_var.set("Rs.850")

            elif(x == 'OS'):
                self.bookid_var.set("BKID61")
                self.booktitle_var.set("Operating System")
                self.auther_var.set("Prof Mrs kinge")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.datedue_var.set("NO")
                self.actualprice_var.set("Rs.800")

            elif(x == 'CN'):
                self.bookid_var.set("BKID62")
                self.booktitle_var.set("Computer Networking")
                self.auther_var.set("Prof Mrs Kulkarni")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latefine_var.set("Rs.50")
                self.datedue_var.set("NO")
                self.actualprice_var.set("Rs.800")

        listBox = Listbox(DataFrameRight, font=(
            "arial", 12, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollBar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)
      # =====================================BUTTONS FRAME==================================
        Framebutton = Frame(self.root, bd=12, relief=RIDGE,
                            padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)

        btnAddData = Button(Framebutton, command=self.adda_data, text="Add Data", font=(
            "arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=0)

        btnAddData = Button(Framebutton, text="Show Data", command=self.showData, font=(
            "arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(Framebutton, text="Update", font=(
            "arial", 12, "bold"), command=self.update, width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(Framebutton, text="Delete", command=self.delete, font=(
            "arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(Framebutton, text="Reset", font=(
            "arial", 12, "bold"), command=self.reset, width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(Framebutton, text="Exit", font=(
            "arial", 12, "bold"), command=self.iExit, width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=5)
      # =====================================InFormation Frame==================================
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE,
                             padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=600, width=1530, height=195)

        Table_frame = Frame(FrameDetails, bd=12,
                            relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=170)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        self.library_table = ttk.Treeview(Table_frame, column=("membertype", "prnno", "title", "firstname", "lastname", "address1",
                                                               "address2", "postid", "mobile", "bookid", "booktitle",
                                                               "auther", "dateborrowed", "datedue", "days",
                                                               "latereturnfine", "dateoverdue", "finalprice"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype", text="Member type")
        self.library_table.heading("prnno", text="PRN NO")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address1")
        self.library_table.heading("address2", text="Address2")
        self.library_table.heading("postid", text="Pin Code")
        self.library_table.heading("mobile", text="Mobile No")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("auther", text="Author Name")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days On Book")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        self.library_table.heading("finalprice", text="Actual Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("auther", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    '''db conection'''

    def adda_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="anuj@2306", database="world")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            self.member_var.get(),
            self.prn_var.get(),
            self.title_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.pincode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.auther_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latefine_var.get(),
            self.datedue_var.get(),
            self.actualprice_var.get()
        ))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success", "Member has been inserted successfully")

    def fatch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="anuj@2306", database="world")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.title_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.pincode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.auther_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook_var.set(row[14])
        self.latefine_var.set(row[15])
        self.dateoverduue_var.set(row[16])
        self.actualprice_var.set(row[17])

    def update(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="anuj@2306", database="world")
        my_cursor = conn.cursor()
        my_cursor.execute("update library set Member=%s,Title=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PinCode=%s,MobileNo=%s,BookID=%s,BookTitle=%s,AuthorName=%s,DateBorrowed=%s,DateDue=%s,DaysOnBook=%s,LateReturnFine=%s,DateOverDue=%s,ActualPrice=%s where PRN_NO=%s",(
                           self.member_var.get(),
                           self.title_var.get(),
                           self.firstname_var.get(),
                           self.lastname_var.get(),
                           self.address1_var.get(),
                           self.address2_var.get(),
                           self.pincode_var.get(),
                           self.mobile_var.get(),
                           self.bookid_var.get(),
                           self.booktitle_var.get(),
                           self.auther_var.get(),
                           self.dateborrowed_var.get(),
                           self.datedue_var.get(),
                           self.daysonbook_var.get(),
                           self.latefine_var.get(),
                           self.datedue_var.get(),
                           self.actualprice_var.get(),
                           self.prn_var.get()
                           ))

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success", "Member has been Updated")

    def fatch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="anuj@2306", database="world")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0])
        
        self.title_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.pincode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.auther_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook_var.set(row[14])
        self.latefine_var.set(row[15])
        self.dateoverduue_var.set(row[16])
        self.actualprice_var.set(row[17])
        self.prn_var.set(row[1])

    def showData(self):
        self.txtBox.insert(END, "Member Type:\t\t" +
                           self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN No:\t\t"+self.prn_var.get() + "\n")
        self.txtBox.insert(END, "DepartMent:\t\t"+self.title_var.get() + "\n")
        self.txtBox.insert(END, "FirstName:\t\t" +
                           self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "LastName:\t\t"+self.lastname_var.get() + "\n")
        self.txtBox.insert(END, "Address1:\t\t"+self.address1_var.get() + "\n")
        self.txtBox.insert(END, "Address2:\t\t"+self.address2_var.get() + "\n")
        self.txtBox.insert(END, "PinCode:\t\t"+self.pincode_var.get() + "\n")
        self.txtBox.insert(END, "MobileNo:\t\t"+self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "BookId:\t\t"+self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title:\t\t" +
                           self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Auther:\t\t"+self.auther_var.get() + "\n")
        self.txtBox.insert(END, "DateBorrowed\t\t" +
                           self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "DateDue\t\t"+self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "DaysOnBook\t\t" +
                           self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END, "LateFine\t\t"+self.latefine_var.get() + "\n")
        self.txtBox.insert(END, "DateOverDue\t\t" +
                           self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "Actual Price\t\t" +
                           self.actualprice_var.get() + "\n")

    def reset(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.title_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.pincode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.auther_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook_var.set("")
        self.latefine_var.set("")
        self.dateoverduue_var.set("")
        self.actualprice_var.set("")
        self.txtBox.delete("1.0", END)

    def iExit(self):
        iExit = tkinter.messagebox.askyesno(
            "Library Management System ", "Exit")
        if iExit > 0:
            self.root.destroy()
            return

    def delete(self):

        if self.prn_var.get() == "" or self.title_var.get() == "":
            messagebox.showerror("Error", "First Select the member")

        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="anuj@2306", database="world")
            my_cursor = conn.cursor()
            query = "delete from library where PRN_NO=%s"
            value = (self.prn_var.get(),)
            my_cursor.execute(query, value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success", "Member has been deleted")


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
