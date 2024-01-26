# Program description

This project is about managing seating arrangements in an open space with multiple tables. It provides a way to assign randomly seats to people from a list, display the current seating arrangement, and store the seating arrangement in an Excel file.

# Installations

This project requires Python and the pandas library. If you don’t have Python installed, you can download it from the official website. Once Python is installed, you can install pandas using pip:

``` pip install pandas ```

pip install pandas 
``` pip install pandas ```


# Usage

To use this script, you need to create an instance of the OpenSpace class and call its methods. Here’s an example:

### Step 1
- Create an open space with 6 tables.
### Step 2
- Organize method will organize the open space by assigning seats to the people in the excel sheet.
/// Be sure that your excel file has for the first column name "Names" and sheet name "Sheet_names" otherwise it won't work properly ///
### Step 3
- Display the seating arrangement.
### Step 4
- Stores the displayed seating arrangement in an excel file. 


``` pip install pandas ```

from src.openspace import OpenSpace

1. open_space = OpenSpace(number_of_tables=6)
2. open_space.organize('YOUR_EXCEL_FILE.xlsx')
3. open_space.display()
4. open_space.store('NAME_OF_EXCEL_FILE.xlsx')
``` pip install pandas ```
