class Customer:
      name = ""
      position = ""
      ID = ""

      def addCart(self):
          print("Add tool to",self.name,self.position,self.ID)

customer1 = Customer()
customer1.name = "tong"
customer1.position = "mech"
customer1.ID = "36998"
customer1.addCart()

customer2 = Customer()
customer2.name = "Golf"
customer2.position = "mech"
customer2.ID = "48995"
customer2.addCart()

customer3 = Customer()
customer3.name = "too"
customer3.position = "mech"
customer3.ID = "89745"
customer3.addCart()

customer4 = Customer()
customer4.name = "tui"
customer4.position = "mech"
customer4.ID = "33214"
customer4.addCart()
