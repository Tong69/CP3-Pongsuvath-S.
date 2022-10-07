usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput=="tong" and passwordInput=="1234":
    print("Login Success")
    print("Tool Room")
    print("My i help you")
    print("---------------------------------------------------------")
    print("1.Wrench")
    print("2.อาหารอีสาน")
    print("3.ตามสั่งไม่ตามหา")
    print("4.เครื่องดื่ม")
    print("---------------------------------------------------------")
    userselected = int(input("Choose in item list :"))
    print("---------------------------------------------------------")
    if userselected == 1:
        print("Wrench")
        print("1.1 1/16 400 $")
        print("2.1 1/8 545 $")
        print("3.1 13/16 430 $")
        print("4.1 300 $")
        print("---------------------------------------------------------")
        userselecte = int(input("Tool in your Order :"))
        if userselecte == 1:
           N1 = int(input("How many would you like ? :"))
           price1 = 400*N1
           print("Total = ",price1,"$")
        elif userselecte == 2:
             N2 = int(input("How many would you like ? :"))
             price2 = 545*N2
             print("Total = ",price2,"$")
        elif userselecte == 3:
             N3 = int(input("How many would you like ? :"))
             price3 = 430*N3
             print("ราคารวมทั้งหมด = ",price3)
        elif userselecte == 4:
             N4 = int(input("How many would you like ? :"))
             price4 =300*N4
             print("Total : ",price4,"$")
    elif userselected == 2:
         print("อาหารอีสาน")
         print("1.ก้อยขมวากิว 200 บาท")
         print("2.คอหมูย่างทรัฟเฟิล 250 บาท")
         print("3.ตำกุ้งมังกร 500 บาท")
         print("---------------------------------------------------------")
         userselecte2 = int(input("รายการที่ต้องการเลือก :"))
         if userselecte2 == 1:
            N5 = int(input("เอาเท่าไหร่ว่ามา :"))
            price5 = 200*N5
            print("ราคารวมทั้งหมด :",price5,"บาท")
         elif userselecte2 == 2:
            N6 = int(input("เอาเท่าไหร่ว่ามา ? :"))
            price6 = 250*N6
            print("ราคารวมทั้งหมด :",price6,"บาท")
         elif userselecte2 == 3:
             N7 = int(input("เอาเท่าไหร่ว่ามา ? :"))
             price7 = 500*N7
             print("ราคารวมทั้งหมด :",price7,"บาท")
    elif userselected == 3:
         print("ตามสั่งไม่ตามหา")
         print("1.ต้มไก่")
         print("2.หมูเทียม")
         print("3.หมี่เหลือง")
         print("---------------------------------------------------------")
         userselecte3 = int(input("รายการที่ท่านต้องการเลือก :"))
         if userselectedbook3 == 1:
             N7 = int(input("How many would you like ? :"))
             price7 = 100 * N7
             print("ราคารวมทั้งหมด :", price7, "บาท")
         elif userselecte3 == 2:
             N8 = int(input("How many would you like ? :"))
             price8 = 104 * N8
             print("ราคารวมทั้งหมด :", price8, "บาท")
         elif userselecte3 == 3:
             N9 = int(input("How many would you like ? :"))
             price9 = 120 * N9
             print("ราคารวมทั้งหมด :", price9, "บาท")
    elif userselected == 4:
         print("ดิ่มไปให้ลืมติ๋ม")
         print("1.037 125 บาท")
         print("2.wine 400 บาท")
         print("3.scoth 250 บาท")
         print("---------------------------------------------------------")
         userselecte4 = int(input("รายการที่ท่านต้องการเลือก :"))
         if userselecte4 == 1:
             N10 = int(input("How many would you like ? :"))
             price10 = 125 * N10
             print("ราคารวมทั้งหมด :", price10, "บาท")
         elif userselecte4 == 2:
             N11 = int(input("How many would you like ? :"))
             price11 = 400 * N11
             print("ราคารวมทั้งหมด :", price11, "บาท")
         elif userselecte4 == 3:
             N12 = int(input("How many would you like ? :"))
             price12 = 250 * N12
             print("ราคารวมทั้งหมด :", price12, "บาท")
    print("---------------------------------------------------------")
    print("------------------------THANK YOU------------------------")
else:
    print("Login Failed!! (T_T)")
    print("Try again.")



