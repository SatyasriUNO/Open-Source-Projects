#*************** KENDRIYA VIDYALAYA, AIR FORCE STATION, THANE **********************
#************************ HOTEL MANAGEMENT SYSTEM **************************
############################# ADARE MANOR ############################# 
#******* Designed and Maintained By :" 
#******* SHREYA UPADHYAY - XII B – 12221 - [ 2022 - 2023 ]" *****#
import mysql.connector as mysql
# GLOBAL VARIABLES DECLARATION 
con ="" 
cur="" 
userName="" 
password ="" 
roomrent =0 
restaurantbill=0 
gamingbill=0 
fashionbill=0 
totalAmount=0 
cid=""
#FN TO CHECK MYSQL CONNECTIVITY 
def MYSQLconnectionCheck ():
    global con
    global userName
    global password
    userName = input("\n ENTER MYSQL SERVER'S USERNAME: ")
    password = input("\n ENTER MYSQL SERVER'S PASSWORD: ")
    con=mysql.connect(host="localhost", user=userName, passwd=password, auth_plugin='mysql_native_password')
    if con:
        print("\n CONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED !")
        cur=con.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS HMS")
        cur.execute("COMMIT")
        cur.close()
        return con
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD !")
#FN TO CHECK MYSQL CONNECTION
def MYSQLconnection ():
    global userName
    global password
    global con
    global cid
    con=mysql.connect(host="localhost", user=userName, passwd=password, database="HMS" , auth_plugin='mysql_native_password' )
    if con:
        return con
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
        con.close()
#FN TO ENTER DETAILS OF STAYEE
def staydetails():
    global cid
    if con:
        cur=con.cursor()
        createTable ="CREATE TABLE IF NOT EXISTS C_DETAILS(CID VARCHAR(20),C_NAME VARCHAR(30),C_ADDRESS VARCHAR(30),C_AGE VARCHAR(30), C_COUNTRY VARCHAR(30) ,P_NO VARCHAR(30),C_EMAIL VARCHAR(30))"
        cur.execute(createTable)
        cid = input("Enter Customer Identification Number: ")
        name = input("Enter Customer Name: ")
        address = input("Enter Customer Address: ")
        age= input("Enter Customer Age: ")
        nationality = input("Enter Customer Country: ")
        phoneno= input("Enter Customer Contact Number: ")
        email = input("Enter Customer Email: ")
        sql = "INSERT INTO C_Details VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values= (cid,name,address,age,nationality,phoneno,email)
        cur.execute(sql,values)
        cur.execute("COMMIT")
        print("\nNew Customer Entered In The System Successfully !")
        cur.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
 
#FN TO BOOK ROOM
def bookingRoom():
    global cid
    customer=searchCustomer()
    if customer:
        if con:
            cur=con.cursor()
            createTable ="CREATE TABLE IF NOT EXISTS BOOKING_RECORD(CID VARCHAR(20),CHECK_IN DATE ,CHECK_OUT DATE)"
            cur.execute(createTable)
            checkin=input("\n Enter Customer CheckIN Date [ YYYY-MM-DD ] : ")
            checkout=input("\n Enter Customer CheckOUT Date [ YYYY-MM-DD ] : ")
            sql= "INSERT INTO BOOKING_RECORD VALUES(%s,%s,%s)"
            values= (cid,checkin,checkout)
            cur.execute(sql,values)
            cur.execute("COMMIT")
            print("\nCHECK-IN AND CHECK-OUT ENTRY MADED SUCCESSFULLY !")
            cur.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")
#FN T O CALCULATE ROOM RENT
def roomRent():
    global cid
    customer=searchCustomer()
    if customer:
        global room_rent
        if con:
            cur=con.cursor()
            createTable ="CREATE TABLE IF NOT EXISTS ROOM_RENT(CID VARCHAR(20),ROOM_CHOICE INT,NO_OF_DAYS INT,ROOMNO INT ,ROOMRENT INT)"
            cur.execute(createTable)
            print ("\n ##### We have The Following Rooms For You #####")
            print (" 1. Premium --------> 50000 Rs.")
            print (" 2. Suite ----------> 3500 Rs. ")
            print (" 3. Luxury --------> 2000 Rs. ")
            print (" 4. Elite ---------> 1000 Rs")
            print (" 5. Only AC -------> 800Rs")
            print (" 6. Non AC --------> 500Rs")
            room_choice =int(input("Enter Your Option: "))
            room_no=int(input("Enter Customer Room No: "))
            no_of_days=int(input("Enter No. Of Days: "))
            if room_choice==1:
                room_rent = no_of_days * 50000
                print("\nPremium Room Rent : ",roomrent)
            elif room_choice==2:
                room_rent = no_of_days * 3500
                print("\nSuite Room Rent : ",roomrent)
            elif room_choice==3:
                room_rent = no_of_days * 2000
                print("\nLuxury Royal Room Rent : ",roomrent)
            elif room_choice==4:
                room_rent = no_of_days * 1000
                print("\nElite Room Rent : ",roomrent)
            elif room_choice==5:
                room_rent=no_of_days * 800
                print("\nOnly AC Room Rent : ",roomrent)
            elif room_choice==6:
                room_rent=no_of_days * 500
                print("\nNon AC Room Rent : ",roomrent)
            else:
                print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                return
        sql= "INSERT INTO ROOM_RENT VALUES(%s,%s,%s,%s,%s)"
        values=(cid,room_choice,no_of_days,room_no,room_rent,)
        cur.execute(sql,val ues)
        cur.execute("COMMIT")
        print("Thank You , Your Room Has Been Booked For: ", no_of_days, "Days" )
        print("Your Total Room Rent is : Rs. ", room_rent)
        cur.close()
#FN TO GENERATE RESTAURANT BILL
def Restaurant():
    global cid
    customer=searchCustomer()
    if customer:
        global restaurantbill
        if con:
            cur=con.cursor()
            createTable ="""CREATE TABLE IF NOT EXISTS RESTAURANT(CID VARCHAR(20),CUISINE VARCHAR(30),QUANTITY VARCHAR(30),BILL VARCHAR(30)) """
            cur.execute(createTable)
            f1=open("ReadRestaurantMenu.txt")
            print(f1.read())
            choice_dish = int(input("Enter Your Cuisine: "))
            quantity=int(input("Enter Quantity : "))
            f1.close()
            f=open("RestaurantMenu.txt")
            a=f.read()
            b=a.split()
            c=2*choice_dish-2
            d=2*choice_dish-1
            print("\nYOUR ORDER HAS BEEN NOTED: ", b[c])
            restaurantbill = quantity * int(b[d])
            f.close()
            sql= "INSERT INTO RESTAURANT VALUES(%s,%s,%s,%s)"
            values= (cid, choice_dish, quantity, restaurantbill)
            cur.execute(sql,values)
            cur.execute("COMMIT")
            print("Your Total Bill Amount Is : Rs. ", restaurantbill)
            print("\n\n**** WE HOPE YOU WILL ENJOY YOUR MEAL ***\n\n" )
            cur.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")
#FN TO GENENRATE BILL FOR GAMING STORE
def GamingStore():
    global cid
    customer=searchCustomer()
    if customer:
        global gamingbill
        if con :
            cur=con.cursor()
            createTable ="CREATE TABLE IF NOT EXISTS GAMING(CID VARCHAR(20),GAMES VARCHAR(30),HOURS VARCHAR(30),GAMING_BILL VARCHAR(30))"
            cur.execute(createTable)
            print("1. Table Tennis -------------> 150 Rs./HR")
            print("2. Bowling ------------------> 100 Rs./HR")
            print("3. Snooker ------------------> 250 Rs./HR")
            print("4. VR World Gaming ----------> 500 Rs./HR")
            print("5. Video Games --------------> 400 Rs./HR")
            print("6. Swimming Pool Games ------> 450 Rs./HR")
            print("7. Pool game ----------------> 380 Rs./HR")
            print("8. Squash game---------------> 300 Rs./HR")
            print("9. Chess---------------------> 200 Rs./HR")
            print("10. Exit")
            game=int(input("Enter What Game You Want To Play: "))
            hour=int(input("Enter No Of Hours You Want To Play: "))
            print("\n\n#################################################")
            if game==1:
                print("YOU HAVE SELECTED TO PLAY : Table Tennis")
                gamingbill = hour * 150
            elif game==2:
                print("YOU HAVE SELECTED TO PLAY : Bowling")
                gamingbill = hour * 100
            elif game==3:
                print("YOU HAVE SELECTED TO PLAY : Snooker")
                gamingbill = hour * 250
            elif game==4:
                print("YOU HAVE SELECTED TO PLAY : VR World Gaming")
                gamingbill = hour * 500
            elif game==5:
                print("YOU HAVE SELECTED TO PLAY : Video Games")
                gamingbill = hour * 400
            elif game==6:
                print("YOU HAVE SELECTED TO PLAY : Swimming Pool Games")
                gamingbill = hour * 450
            elif game==7:
                print("YOU HAVE SELECTED TO PLAY : Pool Game")
                gamingbill = hour * 380
            elif game ==8:
                print("YOU HAVE SELECTED TO PLAY : Squash Game")
                gamingbill = hour * 300
            elif game ==9:
                print("YOU HAVE SELECTED TO PLAY : Chess")
                gamingbill = hour * 200
            else:
                print("Sorry, May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                return
            sql= "INSERT INTO GAMING VALUES(%s,%s,%s,%s)"
            values= (cid,game,hour,gamingbill)
            cur.execute(sql,values)
            cur.execute("COMMIT")
            print("Your Total Gaming Bill Is: Rs. ",gamingbill)
            print("FOR : ", hour," HOURS", "\n *** WE HOPE YOU WILL ENJOY YOUR GAME ***")
            print("\n\n#################################################")
            cur.close()
        else:
            print("ERROR ESTABLISHING MYSQL CONNECTION !")
#FN TO GENERATE FASHION STORE
def FashionStore():
    global cid
    customer=searchCustomer()
    if customer:
        global fashionbill
        if con:
            cur=con.cursor()
            createTable ="""CREATE TABLE IF NOT EXISTS FASHION(CID VARCHAR(20),DRESS VARCHAR(30),AMOUNT VARCHAR(30),BILL VARCHAR(30))"""
            cur.execute(createTable)
            f1=open("ReadFashionStore.txt")
            print(f1.read())
            dress=int(input("Enter the your Choice wear: "))
            quantity=int(input("How many you want to buy: "))
            f1.close()
            f=open("FashionStore.txt")
            a=f.read()
            b=a.split()
            c=2*dress-2
            d=2*dress-1
            print("\nYOU HAVE SELECTED A VERY GOOD BRAND: ", b[c])
            fashionbill = quantity * int(b[d])
            f.close()
            sql= "INSERT INTO FASHION VALUES(%s,%s,%s,%s)"
            values= (cid,dress,quantity,fashionbill)
            cur.execute(sql,values)
            cur.execute("COMMIT")
            print("\n\n#################################################")
            print("\nYOU SELECT ITEM NO : ", dress, "\nYOUR QUANTITY IS : ", quantity, " ITEMS","\nTHANK YOU FOR SHOPPING VISIT AGAIN!!!" )
            print("\nYour Total Bill Is : ", fashionbill)
            print("\n\n#################################################")
            cur.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")
#FN TO DISPLAY CUSTOMER DETAILS
def CustomerDetails():
    global cid
    customer=searchCustomer()
    if customer:
        if con:
            cur=con.cursor()
            sql="SELECT * FROM C_DETAILS WHERE CID= %s"
            cur.execute(sql,(cid,))
            x = tuple(cur.fetchall())
            print("########## Details of the customer are provided below: ##########")
            print(" Customer ID: ", x[0][0])
            print(" Customer Name: ", x[0][1])
            print(" Customer Address: ", x[0][2])
            print(" Customer Age: ", x[0][3])
            print(" Customer Country: ", x[0][4])
            print(" Customer Contact : ", x[0][5])
            print(" Customer Email: ", x[0][6])
#FN TO GENERATE TOTAL BILL
def totalAmt():
    global cid
    customer=searchCustomer()
    if customer:
        global grandTotal
        if con :
            cur=con.cursor()
            x = input("Enter CID whose bill need to be generated: ")
            y = (x,)
            print(y)
            p = """select roomrent from room_rent where cid = %s"""
            cur.execute(p,y)
            ROOMRENT = tuple(cur.fetchall())
            a = 0
            for i in range(len(ROOMRENT)):
                a += int(ROOMRENT[i][0])
            q = """select bill from restaurant where cid = %s"""
            cur.execute(q,y)
            RESTAURANTBILL = tuple(cur.fetchall())
            b = 0
            for j in range(len(RESTAURANTBILL)):
                b += int(RESTAURANTBILL[i][0])
            r = """select bill from fashion where cid = %s"""
            cur.execute(r,y)
            FASHIONBILL = tuple(cur.fetchall())
            c = 0
            for k in range(len(FASHIONBILL)):
                c += int(FASHIONBILL[i][0])
            s = """select gaming_bill from gaming where cid = %s"""
            cur.execute(s,y)
            GAMINGBILL = tuple(cur.fetchall())
            d = 0
            for l in range(len(GAMINGBILL)):
                d += int(GAMINGBILL[i][0])
            createTable ="""CREATE TABLE IF NOT EXISTS TOTAL(CID VARCHAR(20),C_NAME VARCHAR(30),ROOMRENT INT, RESTAURANTBILL INT , GAMINGBILL INT, FASHIONBILL INT, TOTALAMOUNT INT)"""
            cur.execute(createTable)
            sql= "INSERT INTO TOTAL VALUES(%s,%s,%s,%s,%s,%s,%s)"
            name = input("Enter Customer Name : ")
            grandTotal = a + b + c + d
            values= (cid, name, a, b, c, d, grandTotal)
            cur.execute(sql,values)
            cur.execute("COMMIT")
            cur.close()
            print("\n **** ADARE MANOR ****")
            print("\n**** CUSTOMER BIILING ****")
            print("\nCUSTOMER NAME: ", name)
            print("\nROOM RENT: ", a, "Rs. ")
            print("\nRESTAURENT BILL: ", b, "Rs. ")
            print("\nFASHION BILL: ", c, "Rs. ")
            print("\nGAMING BILL: ", d, "Rs. ")
            print("----------------------------------------------")
            print("\nTOTAL AMOUNT: ", grandTotal, "Rs. ")
            print("Please visit again!!")
            cur.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")
#FN TO GENERATE OLD BILL
def searchOldBill():
    global cid
    customer=searchCustomer()
    if customer:
        if con:
            cur=con.cursor()
            sql="SELECT * FROM TOTAL WHERE CID= %s"
            cur.execute(sql,(cid,))
            data=cur.fetchall()
            if data :
                print(data)
            else:
                print("Record Not Found Try Again !")
                cur.close()
        else:
            print("\nSomthing Went Wrong ,Please Try Again !")
 
#FN TO SEARCH CUSTOMER
def searchCustomer():
    global cid
    if con:
        cur=con.cursor()
        cid=input("ENTER CUSTOMER ID: ")
        sql="SELECT * FROM C_DETAILS WHERE CID= %s"
        cur.execute(sql,(cid,))
        data=cur.fetchall()
        if data:
            print(data)
            return True
        else:
            print("Record Not Found Try Again !")
            return False
        cur.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")
#FN TO WRITE INTO FILE
def fileAdd():
    print("File for Calculating Restaurant Bill ----> RestaurantMenu.txt")
    print("File for Calculating Fashion Store Bill -> FashionStore.txt")
    fileName=input("Enter File Name: (Plese enter valid file name, e.g. First.txt): ")
    f=open(fileName, "a")
    lim=int(input("No. of items you want to add: "))
    for i in range(lim):
        x=input("Enter item you want to add: ")
        y=input("Enter price of item added: ")
        f.write('\n')
        f.write(x)
        f.write('\t')
        f.write(y)
    print("***** New Element Added!!! *****")
    print('Please add the same in the other related textfile manually... Sorry for the inconvenience....')
    f.close()
#FIRST OUTPUT
print("""
*************** KENDRIYA VIDYALAYA, AIR FORCE STATION, THANE ***************
************************* HOTEL MANAGEMENT SYSTEM **************************
############################### ADARE MANOR ################################
###################### WELCOME TO WORLD'S BEST RESORT ######################
*** **** Designed and Maintained By :" 
******* SHREYA UPADHYAY - XII B – 12221 - [ 2022 - 2023 ]""")
con= MYSQLconnectionCheck()
if con:
    MYSQLconnection()
    while True:
        print("""
        1--->Enter Customer Details
        2--->Booking Record
        3--->Calculate Room Rent
        4--->Calculate Restaurant Bill
        5--->Calculate Gaming Bill
        6--->Calculate Fashion store Bill
        7--->Display Customer Details
        8--->GENERATE TOTAL BILL AMOUNT
        9--->GENERATE OLD BILL
        10-->ADDING NEW ELEMENTS TO FILE
        11-->EXIT""")
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            staydetails()
        elif choice ==2:
            bookingRoom()
        elif choice ==3:
            roomRent()
        elif choice ==4:
            Restaurant()
        elif choice ==5:
            GamingStore()
        elif choice ==6:
            FashionStore()
        elif choice ==7:
            CustomerDetails()
        elif choice ==8:
            totalAmt()
        elif choice ==9:
            searchOldBill()
        elif choice ==10:
            fileAdd()
        elif choice ==11:
            break
        else:
            print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
else:
    print("\nERROR ESTABLISHING MYSQL CONNECTION !")