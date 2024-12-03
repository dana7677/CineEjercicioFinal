from datetime import datetime

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
    
                    raise ValueError(f"The seat: {number} in the row: {row} already exists.")
                    addSeat=False
                    break
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
            seat=self.search_seat(number,row)

            if seat.isReserved:
                 seat.isReserved=False
                 raise  ValueError(f"The Seat {numero} in the row {fila} already is reserved.")
            else:
                seat.isReserved=True
            
        #Show_Asientos
    def show_seat(self):
         for seat in self._seat:
              print("Seat number:",seat.number," row:",seat.row,"is reserved:",seat.isReserved," price: ",seat.price)
        #CalculatePrice
    def calculate_price(self,age,day):
        price =self.base_price

        #30% Discount 
        if age>65:
              price=price*0.7

        #20% Discount 
        if day.lower()=="wednesday" or day.lower()=="miércoles":
             price=price*0.8

        return price
    def __str__(self):
         return