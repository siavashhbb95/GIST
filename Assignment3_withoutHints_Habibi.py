# -------------------------------------------------------------------------------
# Name:        Assignment3_withoutHints.py
# Purpose:     Script for Assignment3
# Author:      Dr. Yoganand Korgaonkar
# Student Name: Siavash Habibi
# -------------------------------------------------------------------------------
#################################################################################
# TODO: Instructions:
#  - The overall goal of this script is to copy existing polygon feature
#       classes into a new feature dataset in a new geodatabase, extract and store
#       fields from the copied feature classes in a dictionary and print out the
#       contents of the dictionary.
#  - Each goal is split into a specific task in each question given below.
#  - Note that the output/result from each task carries forward to the next task,
#       so there is a form of continuity to all the code that you will write.
#  - Your script should run error free and as one continuous block of code from
#       start to end.
#  - Remember to use a print statement to indicate what step is currently
#       executing in the code.
#  - Data required to test the script can be found on D2L.
#################################################################################

#################################################################################
# TODO Q1: Create a geodatabase (15 points)
#   a) Create a new variable "gdb_path" to store only the path for a new
#      geodatabase on your computer. (2 points)
#      For example: gdb_path = "c:\workspace\gist\"
#      Your path may be different based on your folder structure.
#   b) Using the arcpy.Exists() function, check if "Assignment3.gdb" exists in
#      gdb_path. If it exists, the code should print the message (5 points):
#           "Assignment3.gdb already exists."
#   c) If "Assignment3.gdb" does not exist in gdb_path, use the
#      CreateFileGDB tool with the following parameters: (5 points)
#       out_folder_path: gdb_path
#       out_name: "Assignment3"
#   d) Print out appropriate messages from CreateFileGDB tool execution. (3 points)
# Please add comments to explain what you are coding
# Write your code below
# Imports and workspace
import arcpy
arcpy.env.workspace = "C:/Users/siava/Documents/Workspace/gist603/Data/data"
arcpy.env.overwriteOutput = True
# Creating a new variable for storing the new geo database
gdb_path = "C:/Users/siava/Documents/Workspace/gist603\Data/data/Assignment3"

# Creating a new variable for the name of geo database
Assignment3 = "Assignment3.gdb"

# Checking the existence of the geo database and creating a new one if it does not exist
if arcpy.Exists(Assignment3):
    print(f"{Assignment3} already exists")
else:
    arcpy.management.CreateFileGDB(gdb_path, Assignment3)
    print(f"{Assignment3} was created" )
# End Q1
#################################################################################
# TODO Q2: Create a feature dataset (10 points)
#   a) Create a new variable "dataset_path" to store only the path for the new
#      feature dataset in gdb_path from Q1(a) (2 points)
#      For example: dataset_path = "c:/workspace/gist/Assignment3.gdb"
#      Your path may be different based on your folder structure.
#   b) Use the CreateFeatureDataset tool with the following parameters: (5 points)
#           out_dataset_path: dataset_path
#           out_name: polygon_fcs
#           spatial_ref: use North America Equidistant Conic (3 points)
#      HINT: You must create a spatial reference object to send to the tool
#            before setting up the CreateFeatureDataset tool.
#   c) Print out appropriate messages from tool execution.
# Please add comments to explain what you are coding
# Write your code below
# Creating a new variable to store the path for the geo database from question 1
dataset_path = "C:/Users/siava/Documents/Workspace/gist603\Data/data/Assignment3/Assignment3.gdb"
# Creating a new variable to store the name for the new geo database
polygon_fcs = "polygon_fcs"
# Creating a spatial reference object for "North America Equidistant Conic"
sr = arcpy.SpatialReference(102010)
# Using the CreateFeatureDataset tool to create a new object
arcpy.management.CreateFeatureDataset(dataset_path, polygon_fcs, spatial_reference = sr)
# Printing the messages to see the results
print(f"{polygon_fcs} has been created")
# End Q2
#################################################################################
# TODO Q3: List all polygon feature classes in Austin.gdb/Environmental (5 points)
#   a) Use an ArcPy List functions to create a list of all polygon feature classes
#      in the Environmental feature dataset in Austin.gdb. Store the list in a new
#      variable called list_of_fcs. Print the contents of the list. (3 points)
#   HINT: There should only be three feature classes in your list
#   b) Using the variable list_of_fcs and correct indices, use three print
#      functions to print the following lines exactly as they appear. (2 points)
#               Feature Class 1: geology
#               Feature Class 2: watersheds
#               Feature Class 3: soils
# Please add comments to explain what you are coding
# Write your code below
# Setting up the workspace for Austin.gdb
arcpy.env.workspace = "C:/Users/siava/Documents/Workspace/gist603/Data\data/ExploringSpatialData/Austin.gdb/Environmental"
# Creating a list for the feature classes
list_of_fcs = arcpy.ListFeatureClasses(feature_type = "Polygon")
# Printing the content of the list
print(list_of_fcs)
# Printing the item in the list with the correct indices
i=0
for each_fcs in list_of_fcs:
    i+=1
    print(f"Feature Class {i}: {each_fcs}")
# End Q3
#################################################################################
# TODO Q4: Copy feature classes to empty geodatabase (10 points)
#   a) Using a for loop, loop through the list from Q3. (3 points)
#   b) In the loop, check for the "watersheds" polygon feature class and skip
#      the iteration of the loop for it. (2 points)
#   c) In the loop, create a new variable called out_fc and concatenate the
#      path to the polygon_fcs feature dataset with the name of the feature
#      class stored in the variable of the for loop. (1 point)
#   d) In the loop, use the CopyFeatures tool to copy the remaining feature
#      classes to the empty feature dataset created in Q2. Print out appropriate
#      messages from tool execution. (4 points)
#          Input Feature: use variable from for loop
#          Output Feature: use variable out_fc from (c)
#   HINT: There should only be two feature classes in the new geodatabase
# Please add comments to explain what you are coding
# Write your code below
# Setting up the workspace
arcpy.env.workspace = "C:/Users/siava/Documents/Workspace/gist603/Data/data/ExploringSpatialData/Austin.gdb/Environmental"

# Looping over the list
for each_item in list_of_fcs:

    # Skipping the "watersheds" item
    if each_item == 'watersheds':
        continue
    out_fc = f"{dataset_path}/{each_item}"

    # Copying the  content of the feature class to a new one
    arcpy.management.CopyFeatures(each_item, out_fc)
    print(each_item)
# End Q4
#################################################################################
# TODO Q5: List feature classes in Assignment3.gdb/polygon_fcs (5 points)
#   a) Use an ArcPy List functions to create a list of both the polygon feature
#       classes in the polygon_fcs feature dataset in Assignment3.gdb. (2 points)
#   b) Use a for loop to print the contents of this list. (3 points)
# Please add comments to explain what you are coding
# Write your code below
# Setting up the new workspace
arcpy.env.workspace = "C:/Users/siava/Documents/Workspace/gist603/Data/data/Assignment3/Assignment3.gdb"

# Using the ListFeatureClasses to create a new list from feature classes
feature_classes = arcpy.ListFeatureClasses()

# Using a for loop to print the content of the list
for each_Poly_fc in feature_classes:
    print(each_Poly_fc)
# End Q5
#################################################################################
# TODO Q6: Access fields from the soils feature class (10 points)
#   a) Use an ArcPy List function to access all "Single" fields from the "soils"
#       feature class. (3 points)
#   b) Create an empty list that will be used later in the code to store field
#       names. Use the variable "soils_field_names" to store this empty list. (1 points)
#   c) Setup a for loop to loop through the list of "Single" fields. (1 points)
#   d) In this loop, access the name of each field and append it to the
#       "soils_field_names" list from Q6(c). (2 points)
#   e) In the same loop, print the name and length of each field as follows (3 points):
#         Field Name = <name_of_field> | Length = <length_of_field>
# Please add comments to explain what you are coding
# Write your code below
# Setting up the path for the soils feature class in a variable
soils_path = "C:/Users/siava/Documents/Workspace/gist603/Data/data/Assignment3/Assignment3.gdb/polygon_fcs/soils"

# Using ListField tool to create a new list from soils with only single fields in it
arcpy.ListFields(feature_classes[1], field_type="Single")

# Creating an empty list
soils_field_names = []

# Creating a for lopp
for item in arcpy.ListFields(feature_classes[1], field_type="Single"):
    soils_field_names.append(item.name)
    print(f"Field Name = {item.name} | Length = {item.length}")

print(soils_field_names)

# End Q6
#################################################################################
# TODO Q7: Access fields from the geology feature class (10 points)
#   a) Use an ArcPy List function to access all "String" fields from the "geology"
#       feature class. (3 points)
#   b) Create an empty list that will be used later in the code to store field
#       names. Use the variable "geology_field_names" to store this empty list. (1 points)
#   c) Setup a for loop to loop through the list of "String" fields. (1 points)
#   d) In this loop, access the name of each field and append it to the
#       "geology_field_names" list from Q6(c). (2 points)
#   e) In the same loop, print the name and length of each field as follows (3 points):
#         Field Name = <name_of_field> | Length = <length_of_field>
# Please add comments to explain what you are coding
# Write your code below
# Setting up the path for the soils feature class in a variable
geology_path = "C:/Users/siava/Documents/Workspace/gist603/Data/data/Assignment3/Assignment3.gdb/polygon_fcs/geology"

# Using ListField tool to create a new list from soils with only single fields in it
arcpy.ListFields(feature_classes[0], field_type="String")

# Creating an empty list
geology_field_names = []

# Creating a for lopp
for item in arcpy.ListFields(feature_classes[1], field_type="Single"):
    geology_field_names.append(item.name)
    print(f"Field Name = {item.name} | Length = {item.length}")
print(geology_field_names)
# End Q7
#################################################################################
# TODO Q8: Add lists to a dictionary (10 points)
#   a) Create an empty dictionary that will be used later in the code to store
#       the soils_fields and geology_fields list from above. Use the variable
#       "poly_dict" to store this empty dictionary. (2 points)
#   b) Store the "soils_field_names" list in this dictionary with key "soils". (4 points)
#   c) Store the "geology_field_names" list in the same dictionary with key
#       "geology". (4 points)
# Please add comments to explain what you are coding
# Write your code below
# Creating an empty dictionary
poly_dict = {}

# Adding soils as key and it's items as values
poly_dict['soils'] = soils_field_names

# Adding geology as key and it's items as values
poly_dict['geology'] = geology_field_names

# End Q8
#################################################################################
# TODO Q9: Print contents of dictionary (5 points)
#   a) Setup a for loop to loop through the "poly_dict" dictionary from Q8 (2 points)
#   b) Print out the keys and values from the dictionary in the following
#       format: (3 points)
#       Feature Class = <fc1_name>
#           Fields = <list_of field_names>
# Please add comments to explain what you are coding
# Write your code below
# Setting up a for loop for the dictionary
for key in poly_dict:
    print(f"Feature Class = {key}\n\t Fields = {poly_dict[key]}")

# End Q9
#################################################################################
# TODO Q10: Dictionaries (10 points)
#  Given the following list of dictionaries, this task requires you to print three
#  columns populated by the values in the dictionaries.
#   a) Print the following lines exactly as it appears. (3 points)
#          ID |     WATERSHED     | RECEIVING WATERSHED
#        ---- | ----------------- | -------------------
#      IMPORTANT: Note the formatting on these three columns
#         Column 1: ID - right aligned, width = 5 characters
#         Column 2: WATERSHED - center aligned, width = 19 characters
#         Column 3: RECEIVING WATERSHED - left justified, width = 21 characters
#   b) Set up a for loop to loop on the given list of dictionaries. (2 points)
#   c) Use the for loop and a single print function to print the following
#      exactly as it appears. You may create variables to facilitate the
#      formatting of the print function. (5 points)
#           88 |       RINARD      | ONION CREEK
#           58 |  HARPER'S BRANCH  | TOWN LAKE
#           75 |        MAHA       | CEDAR CREEK
#           74 |      LOCKWOOD     | WILBARGER
#           47 |        ELM        | GILLELAND CREEK
#      IMPORTANT: The alignment and column widths should be the same as in (a).
#                 All strings must be uppercase.
#                 Do not hardcode any of these strings. Use variables and keys.
# Please add comments to explain what you are coding
# Write your code below

# The following list stores 5 dictionaries.
# Each dictionary stores 5 records from the attribute table of the watersheds
# feature class in the Austin.gdb/Environmental dataset
# The keys in these dictionaries are the column names
# The values correspond to the attributes in the respective columns
list_of_dicts = [
    {"DISPLAY" : "Rinard" , "RECV_WATER" : "Onion Creek" , "WATERSHED_" : 88},
    {"DISPLAY" : "Harper's Branch" , "RECV_WATER" : "Town Lake", "WATERSHED_" : 58},
    {"DISPLAY" : "Maha" , "RECV_WATER" : "Cedar Creek", "WATERSHED_" : 75},
    {"DISPLAY" : "Lockwood" , "RECV_WATER" : "Wilbarger", "WATERSHED_" : 74},
    {"DISPLAY" : "Elm" , "RECV_WATER" : "Gilleland Creek", "WATERSHED_" : 47}
]
print("ID".rjust(5) + "WATERSHED".center(19) + "RECEIVING WATERSHED".ljust(21))
for items in list_of_dicts:
    id_str = str(items["WATERSHED_"]).rjust(5)
    watershed_str = items["DISPLAY"].upper().center(19)
    recv_watershed_str = items["RECV_WATER"].upper().ljust(21)
    print(f"{id_str} | {watershed_str} | {recv_watershed_str}")



# # End Q10
# #################################################################################
# # TODO Q11: Errors (10 points)
# #  Identify and fix all errors in the code below.
# #  Only fix errors by modifying the lines of code, do not add your own lines.
# #  Please add comments to identify the type of error, i.e. Syntax, Exception or Logical.
# #  Please add comments to explain what you fixed
# #  Please add comments to explain why you fixed that error
# # Fix all the errors in the code below
#
# imports
# Arcpy should be written as arcpy (lower case)
import arcpy

# Setting environment properties
# Workspace should be written as workspace (lower case)
arcpy.env.workspace = "c:/workspace/gist/data/ExploringSpatialData/Austin.gdb/Environmental"

# List all line feature classes in the workspace
# list name is for lines, but in the tool Point is specified as feature type
list_of_line_fcs = arcpy.ListFeatureClasses("", "Polyline", "")

# Access and print the name of the first feature class in the list
# Indexing in wrong, first item should be 0
first_line_fc = list_of_line_fcs[0]

# f-string in used incorrectly
print(f"\nFirst feature class in the list is {first_line_fc})

# Empty dictionary to use later
# For creating dictionaries {} should be used instead of []
line_dictionary = {}

# Loop through all feature classes one-by-one
# for and in should be replaced which each other
for line_fc  in list_of_line_fcs:
    print("\nFull path of feature class:")
    # Concatenate the full path of the feature class
    # Concatenation should be corrected
    line_path = f"{arcpy.env.workspace}/{line_fc}"
    # Print the path
    print(line_path)
    # Save the path to the dictionary using the name as the key
    line_dictionary[line_fc] = line_path

# Print all the keys from the dictionary
# keys should be replaced with key
print("\nKeys: ")
for key in line_dictionary.keys():
    print(key)

# Print all the values from the dictionary
# line_dictionary.values should be changed
print("\nValues: ")
for value in line_dictionary.values:
    print(value)

# End Q11
#################################################################################
# End of Assignment 3
#################################################################################