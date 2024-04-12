from Roomtype import HotelRoomType

class Room():
    """Python class to implement a basic version of a hotel room.

    This Python class implements the basic functionalities of a hotel room in a 
    simple hotel management system.

    Syntax
    ------
    obj = Room(room_type, room_number, room_state, room_price)

    Parameters
    ----------
    [in] room_type : Roomtype
        Valid values are "Individual", "Doble", "Suite".
    [in] room_number : int
        Unique number of the room.
    [in] room_state : str
        Occupancy state of the room. Expected values are "Ocupada" or "Desocupada".
    [in] room_price : float
        Price per night for the room.

    Returns
    -------
    obj : Room
        Python object output parameter that represents an instance of the class Room.

    Attributes
    ----------
    """

    #Here you start your code.

    #constructor
    def __init__(self, room_type, room_number, room_state, room_price):
        
        #verifica el tipo de habitacion 
        if room_type not in ["Individual", "Doble", "Suite"]:
            raise ValueError("Tipo de habitación no válido.")
        self.room_type = room_type
        
        #verifica que el numero de la habitacion es un entero
        if not isinstance(room_number, int) or room_number <= 0:
            raise ValueError("El número de habitación debe ser un entero positivo.")
        self.room_number = room_number
        
        #verifica que el estado es boleano 
        if not isinstance(room_state, bool):
            raise TypeError("El estado de la habitación debe ser un booleano.")
        self._room_state = room_state

        #verifica que el precio es un entero positivo
        if not isinstance(room_price, float) or room_price <= 0:
            raise ValueError("El precio de la habitación debe ser un número positivo.")
        self.room_price = room_price

    #getters y setters
    def get_room_type(self):
        if isinstance(self.room_type, str):
            return self.get_room_type
        else:
            raise TypeError("El tipo tiene que ser una cadena de texto")
        
    def set_room_type(self, room_type):
        if isinstance(room_type, str):
            self._room_type = room_type
        else:
            raise TypeError("El tipo tiene que ser una cadena de texto")


    def get_room_number(self):
        return self._room_number
    
    def set_room_number(self, room_number):
        self._room_number = room_number
    

    def get_room_state(self):
        if isinstance(self._room_state, bool):
            return self.get_room_state
        else:
            raise TypeError("El estado tiene que ser un booleano")
        
    def set_room_state(self, room_state):
        if isinstance(self._room_state, bool):
            self._room_state = room_state
        else:
            raise TypeError("El estado tiene que ser un booleano")


    def get_room_price(self):
        if isinstance(self.room_price, float):
            return self.get_room_price
        else:
            raise TypeError("El precio tiene que ser un numero")
        
    def set_room_price(self, room_price):
        if isinstance(room_price, float):
            self._room_price = room_price
        else:
            raise TypeError("El precio tiene que ser un número")


    #
    def is_occupied(self):
        return self.room_state == "Ocupada"
    
    def check_in(self, guest_name):
        if not self._room_state:  # Si la habitación no está ocupada
            self._room_state = True
            self._guest_name = guest_name
            print(f"Se ha realizado el check-in en la habitación {self._room_number} a nombre de {guest_name}.")
        else:
            print(f"La habitación {self._room_number} ya está ocupada.")

    # Método para realizar el check-out de la habitación
    def check_out(self):
        if self._room_state:  # Si la habitación está ocupada
            self._room_state = False
            guest_name = self._guest_name
            self._guest_name = None
            print(f"Se ha realizado el check-out de la habitación {self._room_number} a nombre de {guest_name}.")
        else:
            print(f"La habitación {self._room_number} no está ocupada.")
        







def main():
    #TESTING
    print("=================================================================")
    print("Test Case 1: Create a Room.")
    print("=================================================================")
    room1 = Room(HotelRoomType.DOBLE, 101, "Desocupada", 150)

    if room1.get_room_type() == "Doble":
        print("Test PASS. The parameter room_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.get_room_number() == 101:
        print("Test PASS. The parameter room_number has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.get_room_state() == "Desocupada":
        print("Test PASS. The parameter room_state has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.get_room_price() == 150:
        print("Test PASS. The parameter room_price has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================")
    print("Test Case 2: Check-in a Room.")
    print("=================================================================")
    room2 = Room(HotelRoomType.SUITE, 102, "Desocupada", 300)
    check_in_result = room2.check_in()

    if check_in_result == "Check-in realizado con éxito." and room2.is_occupied():
        print("Test PASS. Check-in functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_in().")


    print("=================================================================")
    print("Test Case 3: Check-out a Room.")
    print("=================================================================")
    # Assuming room2 was checked in from the previous test
    check_out_result = room2.check_out()

    if check_out_result == "Check-out realizado con éxito." and not room2.is_occupied():
        print("Test PASS. Check-out functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_out().")


    print("=================================================================")
    print("Test Case 4: Attempt Check-in on an Occupied Room.")
    print("=================================================================")
    room3 = Room(HotelRoomType.INDIVIDUAL, 103, "Ocupada", 100)
    check_in_result = room3.check_in()

    if check_in_result == "La habitación ya está ocupada.":
        print("Test PASS. Attempted check-in on an occupied room handled correctly.")
    else:
        print("Test FAIL. Check the method check_in() for occupied rooms.")


    print("=================================================================")
    print("Test Case 5: Attempt Check-out on a Vacant Room.")
    print("=================================================================")
    # Assuming room3 was made vacant from the previous operation or is initially vacant
    room4 = Room("Doble", 104, "Desocupada", 200)
    check_out_result = room4.check_out()

    if check_out_result == "La habitación ya está desocupada.":
        print("Test PASS. Attempted check-out on a vacant room handled correctly.")
    else:
        print("Test FAIL. Check the method check_out() for vacant rooms.")

if __name__ == "__main__":
    main()