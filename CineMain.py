from datetime import date

class Seat:
    def _init_(self,number,row,price):
        self._number=number
        self._row=row
        self._isReserved=False
        self._price=0.0

    @property
    def number(self):
        return self._number
    
    @property
    def row(self):
        return self._row
    
    @property
    def isReserved(self):
        return self._isReserved
    
    @property
    def isReserved(self,status):
        self._isReserved=status
        return self._isReserved
    
    @property
    def price(self,pricePass):
        self._price=pricePass
        return self._price

class SalaCine:
    def __init__(self,base_price):
        self.base_price=base_price
        self._seat=[]

        #Adding a new Seat
    def add_Seat(self, number, row):

            addSeat=True
            for seat in self._seat:
                if seat.number == number and seat.row == row:
                    addSeat=False
                    print(f"The seat: {number} in the row: {row} already exists.")
                    break
            if addSeat==True:
                new_Seat=Seat(number,row)
                self._seat.append(new_Seat)

        #search a new Seat
    def search_seat(self, number, row):
            for seat in self.__seat:
                if seat.number == number and seat.row == row:
                    return seat
            raise ValueError(f"Entry {number} was not found in row: {row}.")

        #reserve or cancelReserve
    def reserve_or_Cancel_Seat(self,number,row):
            try:
                seat=self.search_seat(number,row)

                if seat.isReserved:
                    seat.isReserved=False
                    
                else:
                    seat.isReserved=True
            except:
                print("The Seat dont exist")
            
        #Show_Asientos
    def show_seat(self):
            for seat in self._seat:
                print("Seat number:",seat.number," row:",seat.row,"is reserved:",seat.isReserved," price: ",seat.price)
        #CalculatePrice
    def calculate_price(self,age):

        #Validation for Age
            try:
                age=int(age)
                price =self.base_price
                today=date.today()
                weekday=today.weekday #return a number of the week 0-Monday, 1-Thuesday, 2-wednesday...

            #30% Discount 
                if age>65:
                    price=price*0.7

            #20% Discount 
                if weekday==2:
                    price=price*0.8
                
                return price
            except:
                print("Error age its not a integer")
            return None
       
    #Get age of the client
    def get_age(year_of_birthday,month_of_birthdday,day_of_birthday):
            try:
                year_of_birthday=int(year_of_birthday)
                month_of_birthdday=int(month_of_birthdday)
                day_of_birthday=int(day_of_birthday)
                today=date.today()
                age=today.year-year_of_birthday
                if(month_of_birthdday<today.month):
                    if(day_of_birthday<=today.day):
                        age=age+1
            
                return age
            except:
                print("Error input its not a integer")
                return None
