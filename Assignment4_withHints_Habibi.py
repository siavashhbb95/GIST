# -------------------------------------------------------------------------------
# Name:        Assignment4_withHints.py
# Purpose:     Script for Assignment4
# Author:      Dr. Yoganand Korgaonkar
# Student Name: Siavash Habibi
# -------------------------------------------------------------------------------
#################################################################################
# TODO: Instructions:
#  - The overall goal of this script is to modify the attributes of the
#       Lake Austin watersheds using geoprocessing tools, csv files and cursors.
#  - You will make use of files, strings, lists, dictionaries, conditional
#       statements and looping structures in this assignment.
#  - Hard-coding string literals will be minimum in this script. You will rely
#       heavily on variables to move data across different lines of code.
#  - Note that the output/result from each question carries forward to the
#       next task, so there is a form of continuity to all the code that you
#       will write.
#  - Your script should run error free and as one continuous block of code
#  - To begin, you will use the watersheds feature class from
#       .../ExploringSpatialData/Austin.gdb/Environmental
#  - You will save all your outputs in the "A4_Results" folder. You may create
#       this folder outside of Python.
#  - The LakeAustin_ReachIntegrityScoreQuality.csv file can be found in the
#       Unit5/Assignment module on D2L.
#  - You are encouraged to write code to handle errors and exceptions.
#################################################################################

#################################################################################
# TODO Q1: Create a text file (10 points)
#   a) Open a file in write mode with the name "A4_Question1.txt". Use the "with"
#      statement. (3 points)
#   b) Write the following lines in the file, each on its own new line: (2 points)
#           "My name is <First_Name> <Last_Name>"
#           "What I like about Python:"
#               <List three things you like about Python>
#           "What I do not like about Python:"
#               <List three things you do not like about Python>
#   c) Open this same file in read mode. Use the "with" statement again. (3 points)
#   d) Use a for loop to print out all the lines in the file. (2 points)
# Please add comments to explain what you are coding
# Write your code below
import arcpy
arcpy.env.overwriteOutput = True



# Open the A4_Question1.txt file in write mode using the "with" statement
new_file = open("C:/Users/siava/Documents/Workspace/gist603/Data/data/A4_Results/A4_Question1.txt", "w")
    # Write the given lines, each on its new line
new_file.write("My name is Siavash Habibi\n")
new_file.write("What I like about Python:\n\t")
new_file.write("It is very simple to use, works for almost evey purpose, and it's very fast!\n")
new_file.write("What I do not like about Python:\n\t")
new_file.write("I can say nothing, it's great!\n")
# Open the A4_Question1.txt file in read mode using the "with" statement
with open("C:/Users/siava/Documents/Workspace/gist603/Data/data/A4_Results/A4_Question1.txt", "r") as new_file:
    # Set up a for loop to loop on all lines in the file
    for line in new_file:
    # Print the line
        print(line)
# End Q1
#################################################################################
# TODO Q2: Execute the Select tool (10 points)
#   a) Create three variables to store the inputs for the Select tool. (5 points)
#           in_features: .../ExploringSpatialData/Austin.gdb/Environmental/watersheds
#           out_feature_class: .../A4_results/watersheds.shp
#           where_clause = <select only those features who have RECV_WATER as Lake Austin>
#       Note: Above paths may change based on the location of data on your computer.
#   b) Execute the Select tool using the above variables and assign the output of
#       the Select tool to a variable called "select_result". Use select_result
#       to print out geoprocessing messages. (5 points)
# Please add comments to explain what you are coding
# Write your code below

# Imports
import arcpy

# Environment properties
arcpy.env.workspace = "C:/Users/siava/Documents/Workspace/gist603/Data/data"

# Variables store the inputs for Select tool. Variables to be used in the tool.
in_features = "C:/Users/siava/Documents/Workspace/gist603/Data/data/ExploringSpatialData/Austin.gdb/Environmental/watersheds"
out_feature_class = "C:/Users/siava/Documents/Workspace/gist603/Data/data/A4_results/watersheds.shp"
where_clause = "RECV_WATER = 'Lake Austin'"

# Execute the Select tool and assign the result to the select_result variable
select_result = arcpy.Select_analysis(in_features, out_feature_class, where_clause)


# Print geoprocessing messages using the select_result variable
print(select_result.getMessages())
# End Q2
#################################################################################
# TODO Q3: Execute the DeleteField tool (10 points)
#   a) Create two variables to store the inputs for the DeleteField tool. (5 points)
#           in_table = select_result - from Q1(b)
#           drop_field = OBJECTID_1, OBJECTID, SHAPE_LENG, DCM_CODE, RECV_WAT_1
#   b) Execute the DeleteField tool using the above variables and assign the
#       output of the DeleteField tool to a variable called "delete_field_result".
#       Use delete_field_result to print out geoprocessing messages. (5 points)
# Please add comments to explain what you are coding
# Write your code below

# Variables store the inputs for the DeleteField tool. Variables to be used in the tool.
in_table = select_result # Do not change this line
drop_field = ["OBJECTID_1", "OBJECTID", "SHAPE_LENG", "DCM_CODE", "RECV_WAT_1"]

# Execute the DeleteField tool and assign the result to the delete_field_result variable
delete_field_result = arcpy.DeleteField_management(in_table, drop_field)

# Print geoprocessing messages using the delete_field_result variable
print(delete_field_result.getMessages())
# End Q3
#################################################################################
# TODO Q4: Execute the AddFields tool (10 points)
#   a) Execute the AddFields tool using the following parameters. (5 points)
#           in_table = delete_field_result
#           Field 1 - name = ACRES, type = DOUBLE
#           Field 2 - name = QUALITY, type = TEXT, length = 50
#   b)  Assign the output of the AddFields tool to a variable called
#       "add_fields_result". Use add_fields_result to print out geoprocessing
#       messages. (5 points)
# Please add comments to explain what you are coding
# Write your code below

# Inputs for AddFields tool. Variables to be used in the tool.
in_table = delete_field_result # Do not change this line


# Execute the AddFields tool and assign the result to the add_fields_result variable
fields_to_add = [("ACRES", "DOUBLE"),("QUALITY", "TEXT", "", "", 50)]
add_fields_result = arcpy.management.AddFields(in_table, fields_to_add)

# Print geoprocessing messages using the delete_field_result variable
print(add_fields_result.getMessages())
# End Q4
#################################################################################
# TODO Q5: Update attributes from a CSV file (20 points)
#   In this task, we will update the values in the "QUALITY" column in the
#      attribute table of watersheds.shp using the values in the "QUAL" column of
#      the LakeAustin_ReachIntegrityScoreQuality.csv. This csv file only has a few
#      DCM_NAMEs in it.
#   a) Open the LakeAustin_ReachIntegrityScoreQuality.csv file in read mode. Use
#      the "with" statement. (3 points)
#   b) Create a DictReader object to access its contents and use the for loop to
#      loop through each row of the DictReader object. (5 points)
#   c) Inside the for loop, create two variables csv_name & csv_qual to store the
#      name and quality, respectively, from the iteration. (2 points)
#   d) Inside the for loop, setup an UpdateCursor on the attribute table of
#      watersheds.shp using the following parameters. Use the "with"
#      statement. (5 points)
#           in_table = add_fields_result
#           field_names: "QUALITY"
#           where_clause: DCM_NAME equals csv_name
#   e) Inside the for loop, setup another for loop to iterate over the records
#      returned by the update cursor. (2 points)
#   f) Inside this second for loop, update the values for the field QUALITY in
#      the attribute table using the value stored in the csv_qual variable from
#      Q5(c). Remember to use the .updateRow() method to save changes. (3 points)
#   You may change the order of these tasks as long as you use the "QUAL" values
#       from the csv file to update the "QUALITY" column in the attribute table.
# Please add comments to explain what you are coding
# Write your code below

# Imports
import arcpy
import csv

# Variable stores the path and name of the input CSV file
csv_file_path = "C:/Users/siava/Documents/Workspace/gist603/Data/data/LakeAustin_ReachIntegrityScoreQuality.csv"


# Open the given csv file in read mode using the "with" statement
with open(csv_file_path, mode='r') as csvfile:


    # Create a DictReader object
    csv_reader = csv.DictReader(csvfile)


    # Access each row as a dictionary from the DictReader object using a for loop
    for each_row in csv_reader:

        for row in csv_reader:
            # Making sure the correct column names are used based on the CSV file structure
            try:
                csv_name = row['NAME']
                csv_qual = row['QUAL']
            except KeyError as e:
                print(f"Error: Missing column in CSV file - {e}")
                continue

        # Inputs for the update cursor: in_table, field_names, and where_clause. Variables to set up the cursor
        in_table = add_fields_result # Do not change this line


        # Set up the where_clause as a string filtering DCM_NAMEs from the attribute table to match csv_name
        # Note - single quotes around string - SQL syntax
        where_clause = f"DCM_NAME = '{csv_name}'"

        # Print the where clause to verify if it is correct
        print(f"Where clause: {where_clause}")

        # Setup the Update Cursor to access records using the "with" statement
        with arcpy.da.UpdateCursor(in_table, ["QUALITY"], where_clause) as cursor:

            # Access each record returned by the update cursor using the for loop
            for record in cursor:
                record[0] = csv_qual

                # Update the QUALITY column for this record using the value from csv_qual,
                cursor.updateRow(record)
                # Save Changes
# End Q5
#################################################################################
# TODO Q6: Delete records from the attribute table (10 points)
#    In this task, we want to delete the records with DCM_NAMEs "Bear Creek West"
#       and "Huck's Slough" from the attribute table of watersheds.shp.
#    a) Setup an UpdateCursor on the attribute table of watersheds.shp using the
#       following parameters. Use the "with" statement. (3 points)
#           in_table = add_fields_result
#           field_names: "DCM_NAME"
#    b) Setup a for loop to iterate over the records returned by the update
#       cursor. (2 points)
#    c) Inside the for loop, use an if statement to check if the DCM_NAME is
#       "Bear Creek West" or "Huck's Slough". (3 points)
#    d) Delete the record inside the if statement when the condition is True. (2 points)
# Please add comments to explain what you are coding
# Write your code below

import arcpy
# Inputs for the update cursor: in_table & field_names. Variables to set up the cursor.
in_table = add_fields_result # Do not change this line


# Setup the Update Cursor to access records using the "with" statement
with arcpy.da.UpdateCursor(in_table, ["DCM_NAME"]) as cursor:


    # Access each record returned by the update cursor using the for loop
    for row in cursor:
        # Variable stores the DCM_NAME from the attribute table
        for row in cursor:
        # Variable stores the DCM_NAME from the attribute table for this record
            dcm_name = row[0]

        # if statement to check for "Bear Creek West" or "Huck's Slough"
        if dcm_name in ["Bear Creek West", "Huck's Slough"]:
            cursor.deleteRow()



            # Delete the record if the condition is true



# End Q6
#################################################################################
# TODO Q7: Calculate values using the update cursor (10 points)
#    In this task, we want to calculate values for the ACRES column using the
#       "SHAPE@AREA" field in the attribute table of watersheds.shp. The area in
#       "SHAPE@AREA" is in square feet based on the coordinate system of
#       watersheds.shp.
#       Conversion Factor: 1 Acre = 43560 Sq Ft
#    a) Setup an UpdateCursor on the attribute table of watersheds.shp using the
#       following parameters. Use the "with" statement. (3 points)
#           in_table = add_fields_result
#           field_names: "SHAPE@AREA" and "ACRES"
#    b) Setup a for loop to iterate over the records returned by the update
#       cursor. (2 points)
#    c) Inside the for loop, access the area in sq ft for each record using the
#       "SHAPE@AREA" field, convert it to acres and update the "ACRES" field.
#       Remember to use the .updateRow() method to save changes. (5 points)
# Please add comments to explain what you are coding
# Write your code below

# Inputs for the update cursor: in_table, field_names. Variables to set up the cursor.
in_table = add_fields_result # Do not change this line


# Setup the Update Cursor to access records using the "with" statement
with arcpy.da.UpdateCursor(in_table, ["SHAPE@AREA", "ACRES"]) as cursor:


    # Access each record returned by the update cursor using a for loop
    for row in cursor:

        # Access the area from the "SHAPE@AREA" field
        area_sq_ft = row[0]

        # Calculate area in acres - 1 Acre = 43560 Sq Ft
        area_acres = area_sq_ft / 43560.0

        # Update the ACRES column with the new area
        row[1] = area_acres
        cursor.updateRow(row)


        # Save Changes



# End Q7
#################################################################################
# TODO Q8: Create a CSV file from attributes (20 points)
#   In this task you will create a CSV file with 4 columns: "FID", "DCM_NAME",
#       "ACRES" & "QUALITY". You will populate this file from the attribute table
#       of watersheds.shp.
#    a) Open a csv file in write mode with the following path & name
#       .../A4_Results/LakeAustinWatersheds.csv. Use the "with" statement. (3 points)
#    b) Create a variable called "column_names" to store the following column
#       names as a list: "FID", "DCM_NAME", "ACRES", & "QUALITY" (2 points)
#    c) Setup a DictWriter object to write rows in the CSV file from Q8(a) with
#       column names from Q8(b). Use the .writeHeader() method to write the
#       column names into the file. (3 points)
#    d) Setup a SearchCursor on the attribute table of watersheds.shp using the
#       following parameters. Use the "with" statement. (3 points)
#           in_table = add_fields_result
#           field_names: column_names
#    e) Setup a for loop to iterate over the records returned by the search
#       cursor. (2 points)
#    f) Inside the for loop, create a dictionary to store values from the
#       records returned by the search cursor, using strings "FID", "DCM_NAME",
#       "ACRES" & "QUALITY" as keys. (5 points)
#    g) Inside the for loop, write the above dictionary into the csv file using
#       the DictWriter.writeRow() method. (2 points)
# Please add comments to explain what you are coding
# Write your code below

# Open a CSV file in write mode using the "with" statement
csv_file = "C:/Users/siava/Documents/Workspace/gist603/Data/data/A4_results/LakeAustinWatersheds.csv"
with open(csv_file, 'w', newline ='') as csvfile:

    # Variable column_names stores a list of column names to write to csv file
    column_names = ["FID", "DCM_NAME", "ACRES", "QUALITY"]

    # Setting up the DictWriter object for the csv file and column names
    csv_writer = csv.DictWriter(csvfile, fieldnames=column_names)


    # Write header to CSV file using this list of column names
    csv_writer.writeheader()


    # Inputs for the search cursor: in_table, field_names
    in_table = add_fields_result # Do not change this line
    field_names = column_names # Do not change this line

    # Set up the search cursor to read the attribute table using the "with" statement

    in_table = "C:/Users/siava/Documents/Workspace/gist603/Data/data/A4_results/watersheds.shp"
    with arcpy.da.SearchCursor(in_table, field_names=column_names) as cursor:
        # Access each record returned by the search cursor using a for loop
        for row in cursor:


            # Four variables to access each value in each column of the record
            record = {
                "FID": row[0],
                "DCM_NAME": row[1],
                "ACRES": row[2],
                "QUALITY": row[3]
            }

            # Create a dictionary using the above variables, column names are keys, above variables are values


            # Write the dictionary as a row to the CSV file

            csv_writer.writerow(record)


# End Q8
#################################################################################
# End of Assignment 4
#################################################################################
