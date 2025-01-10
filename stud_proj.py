from tkinter import *
from stu_db_conn import *
window = Tk()
window.title("Besant Technologies")
window.configure(background="sky blue")
window.geometry("600x480")

# Define variables for form fields
dtvar = StringVar()
fNvar = StringVar()
MbNvar = StringVar()
Altnvar = StringVar()
Eidvar = StringVar()
Adrsvar = StringVar()
coursevar = StringVar()
Batchvar = StringVar()
camevar = StringVar()
expvar = StringVar()
contactvar = StringVar()
counsvar = StringVar()
Feesvar = StringVar()
commentvar = StringVar()

# Check button variables
enquiry_var = IntVar()
registration_var = IntVar()

def get_data():
    # Retrieve data 
    Dat = dtvar.get()
    fNam = fNvar.get()
    MbN = MbNvar.get()
    Altn = Altnvar.get()
    Eid = Eidvar.get()
    Adrs = Adrsvar.get()
    course = coursevar.get()
    batch = Batchvar.get()
    came = camevar.get()
    exp = expvar.get()
    contact = contactvar.get()
    couns = counsvar.get()
    Fees = Feesvar.get()
    comment = commentvar.get()
    return (Dat, fNam, MbN, Altn, Eid, Adrs, course, batch, came, exp, contact, couns, Fees, comment)

def insert_values_db(Dat, fNam, MbN, Altn, Eid, Adrs, course, batch, came, exp, contact, couns, Fees, comment):
    connection = pymysql.connect(host="127.0.0.1", user="root", password="", database="student")
    cursor = connection.cursor()
    
    insertdata = '''insert into studdata(date, name, Mb_no, Alter_no, Email_id, Address, course, batch, came, exp, contact_per, couns, Fees, comment)
                    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    
    cursor.execute(insertdata, (Dat, fNam, MbN, Altn, Eid, Adrs, course, batch, came, exp, contact, couns, Fees, comment))
    connection.commit()
    print("Record added successfully")
    connection.close()

def store_in_txt(Dat, fNam, MbN, Altn, Eid, Adrs, course, batch, came, exp, contact, couns, Fees, comment):
    with open("student.txt", "a") as fobj:
        #fobj.write("DATE\tNAME\tMOBILE_NO\tALT_NO\tEMAIL_ID\tADRS\tCOURSE_INT\tBATCH\tCAME_TO_KNOW\tEXP\tCONTACT_PER\tCOUNSELOR\tCOURSE_FEES\tCOMMENT\n")
        #fobj.write(f"{Dat}\t{fNam}\t{MbN}\t{Altn}\t{Eid}\t{Adrs}\t{course}\t{batch}\t{came}\t{exp}\t{contact}\t{couns}\t{Fees}\t{comment}\n")
        #fobj.write(f"{'DATE':<15}{'NAME':<10}{'MOBILE_NO':<15}{'ALT_NO':<10}{'EMAIL_ID':<30}{'ADRS':<10}{'COURSE_INT':<10}{'BATCH':<5}{'CAME_TO_KNOW':<20}{'EXP':<10}{'CONTACT_PER':<15}{'COUNSELOR':<15}{'COURSE_FEES':<10}{'COMMENT':<20}\n")
        #fobj.write(f"{Dat:<15}{fNam:<10}{MbN:<15}{Altn:<10}{Eid:<30}{Adrs:<10}{course:<10}{batch:<5}{came:<20}{exp:<10}{contact:<15}{couns:<15}{Fees:<10}{comment:<20}\n")
        fobj.write(f"{'DATE':<12}{'NAME':<12}{'MOBILE_NO':<12}{'ALT_NO':<12}{'EMAIL_ID':<25}{'ADRS':<8}{'COURSE_INT':<15}{'BATCH':<5}{'CAME_TO_KNOW':<15}{'EXP':<8}{'CONTACT_PER':<12}{'COUNSELOR':<12}{'COURSE_FEES':<8}{'COMMENT':<30}\n")
        fobj.write(f"{Dat:<12}{fNam:<12}{MbN:<12}{Altn:<12}{Eid:<25}{Adrs:<8}{course:<15}{batch:<5}{came:<15}{exp:<8}{contact:<12}{couns:<12}{Fees:<8}{comment:<30}\n")


def print_data(Dat, fNam, MbN, Altn, Eid, Adrs, course, batch, came, exp, contact, couns, Fees, comment): 
    # Prin
    print("Date:", Dat)
    print("Name:", fNam)
    print("Mobile No:", MbN)
    print("Alternate No:", Altn)
    print("Email ID:", Eid)
    print("Address:", Adrs)
    print("Course Interested:", course)
    print("Batch Preferred:", batch)
    print("How you came to know:", came)
    print("Experience:", exp)
    print("Contact Person:", contact)
    print("Counselor:", couns)
    print("Course Fees:", Fees)
    print("Comment:", comment)
    
def display():
    # Call get_data to fetch values from form
    Dat, fNam, MbN, Altn, Eid, Adrs, course, batch, came, exp, contact, couns, Fees, comment = get_data()
    
    # Store data in DB, text file, and print it
    insert_values_db(Dat, fNam, MbN, Altn, Eid, Adrs, course, batch, came, exp, contact, couns, Fees, comment)
    store_in_txt(Dat, fNam, MbN, Altn, Eid, Adrs, course, batch, came, exp, contact, couns, Fees, comment)
    print_data(Dat, fNam, MbN, Altn, Eid, Adrs, course, batch, came, exp, contact, couns, Fees, comment)
    
def signup():
    Label(window, text="Besant Technologies\nEnquiry Form", bg="grey").grid(row=0, column=1)

    Label(window, text="Date:").grid(row=1, column=0, sticky=W)
    Label(window, text="Name:").grid(row=2, column=0, sticky=W)
    Label(window, text="Mobile No:").grid(row=3, column=0, sticky=W)
    Label(window, text="Alternate No:").grid(row=4, column=0, sticky=W)
    Label(window, text="Email ID:").grid(row=5, column=0, sticky=W)
    Label(window, text="Address:").grid(row=6, column=0, sticky=W)
    Label(window, text="Course Interested:").grid(row=7, column=0, sticky=W)
    Label(window, text="Batch Preferred:").grid(row=8, column=0, sticky=W)
    Label(window, text="How you came to know:").grid(row=9, column=0, sticky=W)
    Label(window, text="Experience:").grid(row=10, column=0, sticky=W)
    Label(window, text="Contact Person:").grid(row=11, column=0, sticky=W)
    Label(window, text="Counselor:").grid(row=12, column=0, sticky=W)
    Label(window, text="Fees:").grid(row=13, column=0, sticky=W)
    Label(window, text="Comment:").grid(row=14, column=0, sticky=W)
    
    Entry(window, textvariable=dtvar).grid(row=1, column=1, ipadx=80)
    Entry(window, textvariable=fNvar).grid(row=2, column=1, ipadx=80)
    Entry(window, textvariable=MbNvar).grid(row=3, column=1, ipadx=80)
    Entry(window, textvariable=Altnvar).grid(row=4, column=1, ipadx=80)
    Entry(window, textvariable=Eidvar).grid(row=5, column=1, ipadx=80)
    Entry(window, textvariable=Adrsvar).grid(row=6, column=1, ipadx=80)
    Entry(window, textvariable=coursevar).grid(row=7, column=1, ipadx=80)
    Entry(window, textvariable=Batchvar).grid(row=8, column=1, ipadx=80)
    Entry(window, textvariable=camevar).grid(row=9, column=1, ipadx=80)
    Entry(window, textvariable=expvar).grid(row=10, column=1, ipadx=80)
    Entry(window, textvariable=contactvar).grid(row=11, column=1, ipadx=80)
    Entry(window, textvariable=counsvar).grid(row=12, column=1, ipadx=80)
    Entry(window, textvariable=Feesvar).grid(row=13, column=1, ipadx=80)
    Entry(window, textvariable=commentvar).grid(row=14, column=1, ipadx=80)

    Checkbutton(window, text="Enquiry", variable=enquiry_var).grid(row=15, column=1, sticky=W)
    Checkbutton(window, text="Registration", variable=registration_var).grid(row=15, column=1, sticky=E)
    Button(window, text="Submit", bg="green", fg="blue", command=display).grid(row=17, column=1, ipadx=40, sticky=W)
    Button(window, text="Quit", bg="red", fg="white", command=window.destroy).grid(row=17, column=1, ipadx=50, sticky=E)

signup()

window.mainloop()








































