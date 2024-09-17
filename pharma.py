from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")

        lbltitle = Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=RIDGE,
                         bg='white', fg="darkgreen", font=("times new roman", 50, "bold"), padx=2, pady=4)
        lbltitle.pack(side=TOP, fill=X)

        # Example of using ImageTk
        img = Image.open(r"C:\Users\sai jagannath\OneDrive\Desktop\webdev\Pharmacymanagementsystemprojectinpython\1.png")
        img = img.resize((100, 100), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        
        btnImage = Button(self.root, image=photo, compound=LEFT)
        btnImage.image = photo  # Keep a reference to avoid garbage collection
        btnImage.place(x=10, y=10)  # Adjust the position as needed

        DataFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20, bg='lightgrey')
        DataFrame.place(x=0, y=120, height=400, width=1550)

        DataFrameLeft = LabelFrame(DataFrame, bd=50, relief=RIDGE, padx=5, text="Medicine Information",
                                   fg="darkgreen", font=("arial", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)


       



        #================buttonFram===================
        ButtonFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20, bg='lightgrey')
        ButtonFrame.place(x=0, y=520, width=1550, height=65)  # Adjusted width and height for horizontal alignment

        #===MAin Button===
        btnAddData = Button(ButtonFrame, text="Medicine Add", font=("arial", 14, "bold"), bg="darkgreen", fg="white")
        btnAddData.grid(row=0, column=0)  # Corrected 'coloumn' to 'column'
        btnupdateMed = Button(ButtonFrame, text="UPDATE", font=("arial", 12, "bold"), bg="darkgreen", fg="white")
        btnupdateMed.grid(row=0, column=1)  # Corrected 'coloumn' to 'column'
        btnDeleteMed = Button(ButtonFrame, text="DELETE", font=("arial", 13, "bold"), bg="darkgreen", fg="white")
        btnDeleteMed.grid(row=0, column=2)  # Corrected 'coloumn' to 'column'
        btnResetMed = Button(ButtonFrame, text="RESET", font=("arial", 12, "bold"), bg="darkgreen", fg="white")
        btnResetMed.grid(row=0, column=3)  # Corrected 'coloumn' to 'column'
        btnExitMed = Button(ButtonFrame, text="EXIT", font=("arial", 11, "bold"), bg="darkgreen", fg="white")
        btnExitMed.grid(row=0, column=4) # Corrected 'coloumn' to 'column'


        #===SEarch by=====

        lblSearch = Label(ButtonFrame, font=("arial", 25, "bold"), text="Search By", padx=2, bg="red", fg="white")
        lblSearch.grid(row=0, column=5, sticky=W)  # Use 'W' for west alignment


        search_combo=ttk.Combobox(ButtonFrame,width=12,font=("arial",15,"bold"),state="readonly")
        search_combo.grid(row=0,column=6)
        search_combo["values"]=("ref","Medname","Lot")
        search_combo.current(0)


        txtSerch=Entry(ButtonFrame,bd=3,relief=RIDGE,width=40,font=("arial",16,"bold"))
        txtSerch.grid(row=0, column=7)


        searchBtn = Button(ButtonFrame, text="SEARCH", font=("arial", 14, "bold"), bg="darkgreen", fg="white")
        searchBtn.grid(row=0, column=8)  # Corrected 'coloumn' to 'column'

        showallBtn = Button(ButtonFrame, text="SHOW ALL", font=("arial", 15, "bold"), bg="darkgreen", fg="white")
        showallBtn.grid(row=0, column=9) # Corrected 'coloumn' to 'column'

        # ============== label and entry============
        lblrefno = Label(DataFrameLeft, font=("arial" ,10 , "bold"), text="Reference No.", padx=2)
        lblrefno.grid(row=1, column=0, sticky=W)  # Use 'W' for west alignment


        ref_combo = ttk.Combobox(DataFrameLeft, width=12, font=("arial", 10, "bold"), state="readonly")
        ref_combo.grid(row=1, column=1)
        ref_combo["values"] = ("Ref", "Medname", "Lot")
        ref_combo.current(0)
        
        
        lblCompanyName = Label(DataFrameLeft, font=("arial", 10, "bold"), text="CompanyName:", padx=5, pady=4)
        lblCompanyName.grid(row=2, column=0, sticky=W)
        txtCompanyName = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtCompanyName.grid(row=2, column=1)


        lbTypeOfMedicine = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Type Of Medicine", padx=5, pady=4)
        lbTypeOfMedicine.grid(row=3, column=0, sticky=W)
        comTypeOfMedicine = ttk.Combobox(DataFrameLeft, state="readonly", font=("arial", 10, "bold"), width=27)
        comTypeOfMedicine["values"] = ("nice", "novel")
        comTypeOfMedicine.current(0)
        comTypeOfMedicine.grid(row=3, column=1)


# Medicine Name Label and Combobox
        lblMedicineName = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Medicine Name", padx=5, pady=4)
        lblMedicineName.grid(row=4, column=0, sticky=W)
        comMedicineName = ttk.Combobox(DataFrameLeft, state="readonly", font=("arial", 10, "bold"), width=27)
        comMedicineName["values"] = ("nice", "novel")
        comMedicineName.current(0)
        comMedicineName.grid(row=4, column=1)

# Lot No Label and Entry
        lblLotNo = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Lot No:", padx=5, pady=4)
        lblLotNo.grid(row=5, column=0, sticky=W)
        txtLotNo = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtLotNo.grid(row=5, column=1)

# Issue Date Label and Entry
        lblIssueDate = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Issue Date:", padx=5, pady=4)
        lblIssueDate.grid(row=6, column=0, sticky=W)
        txtIssueDate = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtIssueDate.grid(row=6, column=1)

# Expiry Date Label and Entry
        lblExpDate = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Exp Date:", padx=5, pady=4)
        lblExpDate.grid(row=7, column=0, sticky=W)
        txtExpDate = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtExpDate.grid(row=7, column=1)


        lblUses = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Uses:", padx=5, pady=4)
        lblUses.grid(row=8, column=0, sticky=W)
        txtUses = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtUses.grid(row=8, column=1)



        lblSideEffect = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Side Effect:", padx=5, pady=4)
        lblSideEffect.grid(row=9, column=0, sticky=W)
        txtSideEffect = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtSideEffect.grid(row=9, column=1)


        lblPrecWarning = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Prec & Warning:", padx=15)
        lblPrecWarning.grid(row=1, column=2, sticky=W)
        txtPrecWarning = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtPrecWarning.grid(row=1, column=3)


        lblDosage = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Dosage:", padx=15)
        lblDosage.grid(row=2, column=2, sticky=W)
        txtDosage = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtDosage.grid(row=2, column=3)


        lblPrice = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Price:", padx=15)
        lblPrice.grid(row=3, column=2, sticky=W)
        txtPrice = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtPrice.grid(row=3, column=3)



        lblProductQt = Label(DataFrameLeft, font=("arial", 10, "bold"), text="Product QT", padx=15)
        lblProductQt.grid(row=4, column=2, sticky=W)
        txtProductQt = Entry(DataFrameLeft, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtProductQt.grid(row=4, column=3)
    #=======images=================
        lblhome = Label(DataFrameLeft, font=("arial", 15, "bold"), text="Stay Home Stay Safe", padx=1,pady=5,bg="white",fg="red",width=20)
        lblhome.place(x=460,y=120)


        img2 = Image.open(r"C:\Users\sai jagannath\OneDrive\Desktop\webdev\Pharmacymanagementsystemprojectinpython\2.png")
        img2 = img2.resize((100, 100), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img2)

# Create a button with the image
        btnImage = Button(root, image=photo, compound=LEFT)
        btnImage.image = photo  # Keep a reference to avoid garbage collection
        btnImage.place(x=530, y=350)

        img3 = Image.open("C:/Users/sai jagannath/OneDrive/Desktop/webdev/Pharmacymanagementsystemprojectinpython/3.png")
        img3= img3.resize((100, 100), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img3)

# Create a button with the image
        btnImage = Button(root, image=photo, compound=LEFT)
        btnImage.image = photo  # Keep a reference to avoid garbage collection
        btnImage.place(x=630, y=350)


        img4 = Image.open("C:/Users/sai jagannath/OneDrive/Desktop/webdev/Pharmacymanagementsystemprojectinpython/4.png")
        img4 = img4.resize((100, 100), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img4)

# Create a button with the image
        btnImage = Button(root, image=photo, compound=LEFT)
        btnImage.image = photo  # Keep a reference to avoid garbage collection
        btnImage.place(x=730, y=350)

        #=====dataframe right======


        DataFrameRight = LabelFrame(DataFrame, bd=50, relief=RIDGE, padx=20, text="Medicine Add Department",
                                   fg="darkgreen", font=("arial", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=540, height=350)


        img5 = Image.open("C:/Users/sai jagannath/OneDrive/Desktop/webdev/Pharmacymanagementsystemprojectinpython/5.png")
        img5 = img5.resize((150, 75), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img5)

# Create a button with the image
        btnImage = Button(root, image=photo, compound=LEFT)
        btnImage.image = photo  # Keep a reference to avoid garbage collection
        btnImage.place(x=1000, y=200)
        

        img6 = Image.open("C:/Users/sai jagannath/OneDrive/Desktop/webdev/Pharmacymanagementsystemprojectinpython/5.png")
        img6 = img6.resize((100, 75), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img6)

# Create a button with the image
        btnImage = Button(root, image=photo, compound=LEFT)
        btnImage.image = photo  # Keep a reference to avoid garbage collection
        btnImage.place(x=1150, y=200)


        img7 = Image.open("C:/Users/sai jagannath/OneDrive/Desktop/webdev/Pharmacymanagementsystemprojectinpython/3.png")
        img7= img3.resize((150, 100), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img7)

# Create a button with the image
        btnImage = Button(root, image=photo, compound=LEFT)
        btnImage.image = photo  # Keep a reference to avoid garbage collection
        btnImage.place(x=1265, y=200)
        

        lblrefno = Label(DataFrameRight, font=("arial", 10, "bold"), text="Reference No:")
        lblrefno.place(x=5, y=95)
        txtrefno = Entry(DataFrameRight, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=20)
        txtrefno.place(x=100, y=95)

        lblmedname = Label(DataFrameRight, font=("arial", 10, "bold"), text="Medicine name:")
        lblmedname.place(x=0, y=125)
        txtmedname = Entry(DataFrameRight, font=("arial", 10, "bold"), bg="white", bd=2, relief=RIDGE, width=20)
        txtmedname.place(x=105, y=125)



        #======side frame====
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=290,height=105) 

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_y.pack(side=BOTTOM,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)











        



         


if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()
