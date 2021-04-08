"""
File: how_much_mulch.py
------------------
This program calculates the amount of mulch needed for garden beds.
"""

MULCH_DEPTH = 2
INCHES_IN_FEET = 12
CUFEET_IN_CUYARD = 27

def main():
    """
    User is prompted to give length and width of all garden beds on property.
    The program then calculates how much mulch will be needed to cover all
    garden beds at a constant depth.
    """

    # tell the user what this program does.
    print("This program calculates the amount of mulch you will need for your garden beds.")

    bed_num = 0

    # count the garden bed numbers (this is last, before the while loop continues for the next bed.)
    bed_num += 1

    # loop calculate area for all beds entered by user
    while input != 0:
        # ask user to input length of garden bed (in feet).
        length_ft = float(input("Enter the length of garden bed number " + str(bed_num) + " in feet: "))
        # ask user to input width of garden bed (in feet).
        width_ft = float(input("Enter the width of garden bed number " + str(bed_num) + " in feet: "))

        # calculate_area of bed in square feet
        area_bed_sqft = length_ft * width_ft

        # calculate_volume of mulch needed for a bed
        volume_bed_cuft = area_bed_sqft * (MULCH_DEPTH / INCHES_IN_FEET)
        volume_bed_cuyd = area_bed_sqft * (MULCH_DEPTH / INCHES_IN_FEET) / CUFEET_IN_CUYARD

        # output to user in cubic feet
        print("The cubic feet of mulch needed for garden bed number " + str(bed_num) + " is: " + str(volume_bed_cuft))

        # output to user in cubic yards
        print("The cubic yards of mulch needed for garden bed number " + str(bed_num) + " is: " + str(volume_bed_cuyd))

        # add all volume_bed_cuft together







    # This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
