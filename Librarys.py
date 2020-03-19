from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Library:

    def __init__(self, root ):
        self.root = root
        self.root.configure(background='#DAE0E2')
        self.root.geometry('1350x750+0+0')
        self.root.title("Library Management System")

        Mtype = StringVar()
        Ref = StringVar()
        Title = StringVar()
        FirstName = StringVar()
        SurName = StringVar()
        Address1 = StringVar()
        Address2 = StringVar()
        PostCode = StringVar()
        MobileNo = StringVar()
        BookId = StringVar()
        Author = StringVar()
        BookTitle = StringVar()
        DateBorrowed = StringVar()
        DateDue = StringVar()
        LateReturnFine = StringVar()
        DateOverDue = StringVar()
        DaysOnLoan = StringVar()
        SellingP = StringVar()
        
        def iReset():
            Mtype.set("")
            Ref.set("")
            BookTitle.set("")
            Title.set("")
            FirstName.set("")
            SurName.set("")
            Address1.set("")
            Address2.set("")
            PostCode.set("")
            MobileNo.set("")
            BookId.set("")
            Author.set("")
            DateBorrowed.set("")
            DateDue.set("")
            LateReturnFine.set("")
            DateOverDue.set("")
            DaysOnLoan.set("")
            SellingP.set("")

        def iExit():
            exit = messagebox.askyesno("Library Management System","Are you sure ?")
            if exit:
                root.destroy()
                return

        def ireceipt():
            self.TextArea.insert(END,"Member Type \t\t" + Mtype.get()+"\n")
            self.TextArea.insert(END,"Ref No  \t\t" + Ref.get()+"\n")
            self.TextArea.insert(END,"Title \t\t" + Title.get()+"\n")
            self.TextArea.insert(END,"FirstName  \t\t" + FirstName.get()+"\n")
            self.TextArea.insert(END,"SurName  \t\t" + SurName.get()+"\n")
            self.TextArea.insert(END,"Address1  \t\t" + Address1.get()+"\n")
            self.TextArea.insert(END,"Address2  \t\t" + Address2.get()+"\n")
            self.TextArea.insert(END,"PostCode  \t\t" + PostCode.get()+"\n")
            self.TextArea.insert(END,"MobileNo  \t\t" + MobileNo.get()+"\n")
            self.TextArea.insert(END,"BookId  \t\t" + BookId.get()+"\n")
            self.TextArea.insert(END,"BookTitle  \t\t" + BookTitle.get()+"\n")
            self.TextArea.insert(END,"Author  \t\t" + Author.get()+"\n")
            self.TextArea.insert(END,"DateBorrowed  \t\t" + DateBorrowed.get()+"\n")

        def idelete():
            self.TextArea.delete("1.0",END)
            self.TextAreaa.delete("1.0",END)

        def idisplay():
            self.TextAreaa.insert(END,Mtype.get()+"\t\t" +Ref.get()+"\t" + Title.get()+ "\t"+FirstName.get() +"\t" + SurName.get()  +"\t\t" +Address1.get() +"\t\t" + Address2.get()  +"\t" +PostCode.get() +"\t" + BookTitle.get()  +"\t\t" +DateBorrowed.get() +"\t\t" +DaysOnLoan.get() + "\n")


        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame( MainFrame ,bd = 15 , padx = 10 , width = 1350,relief = RIDGE ,bg='#EAF0F1' )
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label( TitleFrame , text = " Library Management System " , font = ( "arial", 40 , "bold" ), padx = 12,width = 40 ,bg='#EAF0F1')
        self.lblTitle.grid()

        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^MainFrame^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

        ItemFrame = Frame( MainFrame , height = 400 , bd = 15 , padx=20 , width =1350 ,relief = RIDGE,bg='#EAF0F1')
        ItemFrame.pack()

        LeftFrame = LabelFrame( ItemFrame ,font = ( "Taharialoma", 15 , "bold" ) ,bd = 10,width = 800 ,height = 300 , padx = 20 ,relief = RIDGE , text = "Library Management Info: " )
        LeftFrame.pack(side=LEFT)

        RightFrame = LabelFrame( ItemFrame , font = ( "arial", 10 , "bold" ),bd = 15 , padx = 20 ,width = 450 ,height = 300 , relief = RIDGE , text = "Book Details: " )
        RightFrame.pack(side=RIGHT)

        ButtonFrame = Frame( MainFrame , width = 1300 , bd = 15 , height = 100,padx = 20 , relief = RIDGE,bg='#EAF0F1' )
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail = Frame( MainFrame , width = 1300 , bd = 15 , height = 100 ,padx = 20, relief = RIDGE,bg='#EAF0F1' )
        FrameDetail.pack(side=BOTTOM)

        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^FRAMEDETAIL^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

        self.lblLabel = Label( FrameDetail , font = ('arial' ,10 , 'bold' ) , pady = 7 , text = "Member Type \t Reference No.\t Title \t Firstname \t Surname \t Address 1\t Address 2 \t Post Code \t Book Title \t Date Borrowed \ Days On Loan ")
        self.lblLabel.grid(row = 0 , column = 0 )

        self.TextAreaa = Text( FrameDetail  , font = ("arial",12,"bold"),width = 126  ,padx = 4 ,pady = 1, height = 4  )
        self.TextAreaa.grid(row = 1 , column = 0 )


        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^LIST^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
        scroll = Scrollbar(RightFrame)
        scroll.grid( row = 0 , column = 1 , sticky = 'ns' )

        ListOfBooks = ["Cinderella","Game Design","Ancient Rome" , "Made in Africa","Sleeping Beauty","London ","Nigeria","Snow White","Om Shanti Om" ,"Angare Bane Sole","Invisible Man" , "You nad Me " ,"WHo was that","Nobody cares","But WHo are You",]



        def SelectedBook(evt):
            value = str(InbuiltBox.get(InbuiltBox.curselection()))
            w = value
            
            if w == "Cinderella":
                BookId.set("ISBN 754777534")
                BookTitle.set("God is King")
                Author.set("Paul Parker")

                LateReturnFine.set("$2.5")
                SellingP.set("$2.5")
                DaysOnLoan.set(14)
                ireceipt()

                import datetime
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = (d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DateOverDue.set("No")

        InbuiltBox = Listbox(RightFrame , width = 20 , height = 13, font = ("arial",12,"bold"))
        InbuiltBox.bind('<<ListboxSelect>>' , SelectedBook)
        InbuiltBox.grid( row = 0 , column = 0 )
        scroll.config( command = InbuiltBox.yview)


        for books in ListOfBooks:
            InbuiltBox.insert( END , books )
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^TEXTAREA^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

        self.TextArea = Text( RightFrame ,width = 32 ,height = 13, font = ("arial",12,"bold"),padx = 8 , pady = 20)
        self.TextArea.grid(row = 0 , column = 2)

        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^BUTTONS^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
        ButtonDisplay = Button( ButtonFrame , width =  30 ,bd = 2, text = " Display Data " , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,command = lambda : idisplay())
        ButtonDisplay.grid(row = 0 , column = 0)

        ButtonDelete = Button( ButtonFrame , width =  30 ,bd = 2, text = " Delete " , font = ("arial",12,"bold"),padx = 2 , pady = 2 , command = lambda : idelete())
        ButtonDelete.grid(row = 0 , column = 2)

        ButtonReset = Button( ButtonFrame , width =  30,bd = 2 , text = " Reset " , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,command = lambda : iReset())
        ButtonReset.grid(row = 0 , column = 4)

        ButtonExit = Button( ButtonFrame , width =  30,bd = 2 , text = " Exit " , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,command = lambda : iExit())
        ButtonExit.grid(row = 0 , column = 6)

        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^WIDGETS^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

        self.lblMemberType = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Member Type")
        self.lblMemberType.grid(row = 0 , column = 0 , sticky = W )

        self.lblMemberType = ttk.Combobox( LeftFrame , font = ("arial",12,"bold"),width = 23 ,textvariable = Mtype)
        self.lblMemberType['value']=('' ,'Student','Lecturer','Admin Staff')
        self.lblMemberType.current(0)
        self.lblMemberType.grid(row = 0 , column = 1 )

        self.lblBookId = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Book ID:  ")
        self.lblBookId.grid(row = 0 , column = 2 , sticky = W )

        self.lblBookId = Entry( LeftFrame , font = ("arial",12,"bold"),width = 25 ,textvariable = BookId)
        self.lblBookId.grid(row = 0 , column = 3 )
        

        self.lblRefernce = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Reference No. ")
        self.lblRefernce.grid(row = 1 , column = 0 , sticky = W )

        self.lblRefernce = Entry( LeftFrame , font = ("arial",12,"bold"),width = 25 ,textvariable = Ref)
        self.lblRefernce.grid(row = 1 , column = 1 )
        
        self.lblBookTitle = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Book Title:  ")
        self.lblBookTitle.grid(row = 1 , column = 2 , sticky = W )

        self.lblBookTitle = Entry( LeftFrame , font = ("arial",12,"bold"),width = 25 ,textvariable = BookTitle)
        self.lblBookTitle.grid(row = 1 , column = 3 )
        
        self.lblTitle = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Title:  ")
        self.lblTitle.grid(row = 2 , column = 0 , sticky = W )

        self.lblTitle = ttk.Combobox( LeftFrame , font = ("arial",12,"bold"),width = 23 ,textvariable = Title)
        self.lblTitle['value'] = ('' ,' Mr. ',' Mrs. ' , ' Miss ' , ' Capt. ' , ' Ms. ' )
        self.lblTitle.current(0)
        self.lblTitle.grid(row = 2 , column = 1 )
        
        self.lblBookId = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Author:  ")
        self.lblBookId.grid(row = 2 , column = 2 , sticky = W )

        self.lblBookId = Entry( LeftFrame , font = ("arial",12,"bold"),width = 25,textvariable = Author )
        self.lblBookId.grid(row = 2 , column = 3 )
        
        
        self.lblFname = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "First Name:  ")
        self.lblFname.grid(row = 3 , column = 0 , sticky = W )

        self.lblFname = Entry( LeftFrame , font = ("arial",12,"bold"),width = 25 ,textvariable = FirstName)
        self.lblFname.grid(row = 3 , column = 1 )
        
        self.lblDBoror = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Date Borrowed: ")
        self.lblDBoror.grid(row = 3 , column = 2 , sticky = W )

        self.lblDBoror = Entry( LeftFrame , font = ("arial",12,"bold"),width = 25 ,textvariable = DateBorrowed)
        self.lblDBoror.grid(row = 3 , column = 3 )

        
        self.Surname = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Surname:  ")
        self.Surname.grid(row = 4 , column = 0 , sticky = W )

        self.Surname = Entry( LeftFrame , font = ("arial",12,"bold"),width = 25 ,textvariable = SurName)
        self.Surname.grid(row = 4 , column = 1 )
        
        self.Date = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Date Due: ")
        self.Date.grid(row = 4 , column = 2 , sticky = W )

        self.Date = Entry( LeftFrame , font = ("arial",12,"bold"),width = 25 ,textvariable = DateDue)
        self.Date.grid(row = 4 , column = 3 )

        
        self.Address = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Address 1: ")
        self.Address.grid(row = 5 , column = 0 , sticky = W )

        self.Address = Entry( LeftFrame , font = ("arial",12,"bold"),width = 25 ,textvariable = Address1)
        self.Address.grid(row = 5 , column = 1 )
        
        self.Days = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Days on loan: ")
        self.Days.grid(row = 5 , column = 2 , sticky = W )

        self.Days = Entry( LeftFrame , font = ("arial",12,"bold"),width = 25,textvariable = DaysOnLoan )
        self.Days.grid(row = 5 , column = 3 )

        self.Address2 = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Address 2: ")
        self.Address2.grid(row = 6 , column = 0 , sticky = W )

        self.Address2 = Entry( LeftFrame , font = ("arial",12,"bold"),width = 25 ,textvariable = Address2)
        self.Address2.grid(row = 6 , column = 1 )
        
        self.fine = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Late Return Fine: ")
        self.fine.grid(row = 6 , column = 2 , sticky = W )

        self.fine = Entry( LeftFrame , font = ("arial",12,"bold"),width = 25 ,textvariable = LateReturnFine)
        self.fine.grid(row = 6 , column = 3 )

        self.Code = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Post Code: ")
        self.Code.grid(row = 7 , column = 0 , sticky = W )

        self.Code = Entry( LeftFrame , font = ("arial",12,"bold"),width = 25 ,textvariable = PostCode)
        self.Code.grid(row = 7 , column = 1 )
        
        self.Over = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Date Over Due: ")
        self.Over.grid(row = 7 , column = 2 , sticky = W )

        self.Over = Entry( LeftFrame , font = ("arial",12,"bold"),width = 25 ,textvariable = DateDue)
        self.Over.grid(row = 7 , column = 3 )

        self.Moblie = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Moblie No.: ")
        self.Moblie.grid(row = 8 , column = 0 , sticky = W )

        self.Moblie = Entry( LeftFrame , font = ("arial",12,"bold"),width = 25 ,textvariable = MobileNo)
        self.Moblie.grid(row = 8 , column = 1 )
        
        self.Selling = Label( LeftFrame , font = ("arial",12,"bold"),padx = 2 , pady = 2 ,text = "Selling Price: ")
        self.Selling.grid(row = 8 , column = 2 , sticky = W )

        self.Selling = Entry( LeftFrame , font = ("arial",12,"bold"),width = 25,textvariable = SellingP )
        self.Selling.grid(row = 8 , column = 3 )



if __name__ == '__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()
    