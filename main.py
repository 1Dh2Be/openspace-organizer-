from src.openspace import OpenSpace



if __name__ == "__main__":


    # Create an open space with 6 tables.
    room = OpenSpace(6)

    # Organize the open space by assigning seats to the people in the names list.
    room.organize('/Users/MimounB/Desktop/VScode/openspace-organizer-/colleagues.xlsx')

    # Display the seating arrangement.
    room.display()

    # Stores the displayed seating arrangement in an excel file. 
    room.store("sorted_places.xlsx") 