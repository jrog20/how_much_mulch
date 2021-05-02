"""
File: how_much_mulch.py
------------------
This program calculates the amount of mulch needed for garden beds.
The user is prompted to give length and width of all garden beds.
The program then calculates how much mulch will be needed to cover all
garden beds at a constant depth.
"""

MULCH_DEPTH = 2
INCHES_IN_FEET = 12
CUFEET_IN_CUYARD = 27

def main():

    bed_num = 0
    total_beds_volume_cuft = 0
    total_beds_volume_cuyd = 0

    print("This program calculates the amount of mulch you will need for your garden beds.")

    while input != 0:
        bed_num += 1
        length_ft = float(input("Enter the length of garden bed number " + str(bed_num) + " in feet: "))
        width_ft = float(input("Enter the width of garden bed number " + str(bed_num) + " in feet: "))

        area_bed_sqft = length_ft * width_ft

        volume_bed_cuft = area_bed_sqft * (MULCH_DEPTH / INCHES_IN_FEET)
        volume_bed_cuyd = area_bed_sqft * (MULCH_DEPTH / INCHES_IN_FEET) / CUFEET_IN_CUYARD

        total_beds_volume_cuft += volume_bed_cuft
        total_beds_volume_cuyd += volume_bed_cuyd

        print("The cubic feet of mulch needed for garden bed number", bed_num, "is:", volume_bed_cuft)
        print("The cubic yards of mulch needed for garden bed number", bed_num, "is:", volume_bed_cuyd)

        print("Total mulch needed for all garden beds is:", total_beds_volume_cuft, "cubic feet, or", total_beds_volume_cuyd, "cubic yards.")


if __name__ == '__main__':
    main()
