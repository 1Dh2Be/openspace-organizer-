from src.table import Table
import pandas as pd 

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
    ______
     """
    def __init__(self, number_of_tables:int=6):
        self.opspaces = {k+1: Table() for k in range(number_of_tables)}

    def organize(self, file):
        """
        Assigns each name in the provided excel file to a free chair in the open space.
        The assignment stops once all names have been assigned or there are no more free spots.
        ///Be cautious since the parameters inside variable 'df' and 'names' are case sensitive, 
        be sure to write the corresponding sheet and column name to your excel file!///
        """
        
        excel_file = pd.ExcelFile(file)

        df = excel_file.parse('Sheet_names')
        names = df['Names'].tolist()
        number_people  = len(names)

        for name in names:
            for table_number, table in self.opspaces.items():
                if table.has_free_spot():
                    table.assign_seat(name)
                    break
        counter = 0
        for table_number, table in self.opspaces.items():
            for seat in table.seats.values():
                if seat.free:
                    counter += 1 
                
        max_seats = 24
        last = []
        if number_people > max_seats:
            result = names[max_seats:]
            last = [name for name in result]
            

        print(f"\nThe room capacity is {max_seats}.")
        print(f"\nThere are {number_people} persons in the room and {counter} free seats left.\n")
        print(f"{last} hasn't been asigned a chair\n")
        
        

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