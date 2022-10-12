systemMenu = {"Sandwich-Ham": 35, "ไข่เจียวหมูสับ": 45, "เป็ดย่าง": 55, "น้ำเปล่า": 20}
menuList = []

def showBill():
    total = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        total += int(menuList[number][1])
        print("Total :", total, "THB.")

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])


print(menuList)

showBill()

