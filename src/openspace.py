from src.table import Table
import pandas as pd 
from random import shuffle 

class OpenSpace():
    """
    ______
    A class used to represent an OpenSpace with multiple tables.

    ____

    Attributes
    ___________
    * opspaces : dict
         a dictionary where keys are table numbers and values are Table objects.
    ____

    Methods
    __________
    /// See documentation for methods using .__doc__ after method name. ///

    * organize()

    * display()

    * store()

    * add_new_person()
    ______
     """
    def __init__(self, number_of_tables:int=6):
        self.opspaces = {k+1: Table() for k in range(number_of_tables)}

    def organize(self, file):
        """
       This method shuffles the names and selects one randomly.
       Each name from the provided Excel file is then assigned to an available seat in the open space. 
       The assignment process continues until all names have been assigned or there are no more available seats.
       
       ///Please note that the parameters within the 'df' and 'names' variables are case sensitive.
       Ensure to match the sheet and column names exactly with those in your Excel file.///
        """
        
        excel_file = pd.ExcelFile(file)

        df = excel_file.parse('Sheet_names')
        names = df['Names'].tolist()
        shuffle(names)
        number_of_people = 0

        for name in names:
            for table in self.opspaces.values():
                if table.has_free_spot():
                    table.assign_seat(name)
                    break
        counter = 0
        total_seats = 0
        for table in self.opspaces.values():
            for seat in table.seats.values():
                total_seats += 1
                if not seat.free:
                    number_of_people += 1
                if seat.free:
                    counter += 1 

        last = []
        print(f"\nThe room capacity is {total_seats}.")
        # Fix the list output. You want it to output names, but not in list format
        if number_of_people > total_seats:
            result = names[total_seats:]
            last = [name for name in result]
            print(f"\nThere are {number_of_people} persons in the room, "
                  f"{counter} seats are unoccupied.\n")
            print(f"{last} hasn't been asigned a chair\n")
        elif number_of_people == total_seats - 1:
            print(f"\nThere are {number_of_people} persons in the room, "
                  f"{counter} seat remains free.\n")
        else:
            print(f"\nThere are {number_of_people} persons in the room, "
                  f"{counter} seats are unoccupied.\n")      

    def add_new_person(self, name:str):
        seat_assigned = False
        for table in self.opspaces.values():
            if seat_assigned == False:
                for seat in table.seats.values():
                    if seat.free:
                        seat.set_occupant(name)
                        seat_assigned = True
                        print(f"{name} has been assigned a chair. ")
                        break
        counter = 0
        for table in self.opspaces.values():
            for seat in table.seats.values():
                if not seat.free:
                    counter += 1 
        print(f"There are now {counter} persons in the room.\n") 
        
    def display(self):
        """
        Prints the current state of the open space, 
        showing which seats are occupied and by whom.
        """

        for table_number, table in self.opspaces.items():
            print(f"Table {table_number} \n")
            for seat_number, seat in table.seats.items():
                if not seat.free:
                    print(f"Seat {seat_number} is assigned to {seat.occupant}")
                else:
                    print(f"Seat {seat_number} is free")
            print("\n")

    def store(self, filename):
        """
        Stores the current state of the open space in an Excel file.
        The fille will contain a table with columns for table number, seat and occupant name.
        """

        data = []

        for table_number, table in self.opspaces.items():
            for seat_number, seat in table.seats.items():
                if not seat.free:
                    data.append([table_number, seat_number, seat.occupant])
                else:
                    data.append([table_number, seat_number, 'free'])
            df = pd.DataFrame(data, columns = ["table", "seat", "occupant"])
            df.to_excel(filename, index = False)