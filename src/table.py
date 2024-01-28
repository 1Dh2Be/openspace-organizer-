

class Seat():
    """
    ----

    A class used to represent a Seat.


    Attributes
    ----------
    * free : bool
         a boolean indicating if the seat is free (default is True)
    * occupant : str
         a string for the occupant's name (default is an empty string)

    Methods
    ----------
    /// See documentation for methods using .__doc__ after method name. ///

    * set_occupant()
    
    * reomve_occupant()

    ----
    """

    def __init__(self, free:bool=True, occupant:str=""):
        self.free = free
        self.occupant = occupant

    def set_occupant(self, name):
        """
        Assigns an occupant to the seat if it's free. If the seat is already occupied, it prints a message indicating that 
        the seat is already occupied by the current occupant.
        """

        if self.free:
            self.occupant = name
            self.free = False
            # print(f"{name} has been asigned the chair. ")
        else:
            print(f"The chair is already occupied by {self.occupant} ")
            
    def remove_occupant(self):
        """
        Removes the occupant from the seat if it's occupied. If the seat is already free, it prints a message indicating
        that nobody is sitting on the chair.
        """

        if not self.free:
            self.free = True
            print("The chair is now free!")
        else: 
            print("Nobody is sitting on chair.")

class Table():
    """
    A class used to represent a Table.

    ---

    Attributes
    ----------
     * seats : dict
         A dictionary where keys are seat numbers and values are Seat objects.
    
    Methods
    ----------
    /// See documentation for methods with .__doc__ after method name. ///

    * has_free_spot
    
    * assign_seat
    
    * capacity_left

    ---
    """

    
    def __init__(self, n_seats:int = 4):
        self.seats = {k+1: Seat() for k in range(n_seats)}

    def has_free_spot(self):
        """
        Checks if there's a free spot at the table. Returns a boolean.
        """

        return any(seat.free for key, seat in self.seats.items())
    
    def assign_seat(self, name):
        """
        Assigns a seat to a person if a free spot is available. 
        If there are no free spots, it prints a message indicating that there are 
        no free seats available.
        """
        sorted_seats = sorted(self.seats.keys())
        for seat_number in sorted_seats:
            if self.seats[seat_number].free:
                seat_to_assign = self.seats[seat_number]
                seat_to_assign.set_occupant(name)
                break
            
    def capacity_left(self):
        """
        Calculates the number of free spots left at the table. Returns an integer.
        """

        return sum(seat.free for seat in self.seats.values())