# -------------------------------------------------------------------------------
# Name:        Assignment5_withHints.py
# Purpose:     Script for Assignment5
# Author:      Dr. Yoganand Korgaonkar
# Student Name: Siavash Habibi
# -------------------------------------------------------------------------------

#################################################################################
# TODO: Instructions:
#   - The overall goal of this part is to create a feature class using
#       coordinates from a csv file and then use this feature class to create
#       watersheds from an elevation raster.
#   - Hard-coding string literals will be minimum in this script. You will rely
#       heavily on variables to move data across different lines of code.
#   - Note that the output/result from each question carries forward to the
#       next task, so there is a form of continuity to all the code that you
#       will write.
#   - Your script should run error free and as one continuous block of code.
#   - You will use the elevation raster from
#       .../ExploringSpatialData/Sturgis.gdb/topo30m
#   - You will save all your outputs in the "A5_Results" folder. You may create
#       this folder outside of Python.
#   - The pourpoints.csv file can be found in the Unit6/Assignment module on D2L.
#   - You are encouraged to write code to handle errors and exceptions.
#################################################################################

# Imports - include all imports at the very beginning of the script.
import arcpy
from arcpy import env
import csv
arcpy.env.overwriteOutput = True

# Environment Properties
# TODO IMP: Change this path to the "A5_results" folder on your computer
arcpy.env.workspace = "C:/Users/siava/Documents/Workspace/gist603/Data/data/A5_Results"


#################################################################################
# TODO Q1: Execute the CreateFeatureclass tool (10 points)
#   a) Create four variables to store the inputs for the CreateFeatureclass
#       tool. (5 points)
#       out_path: .../A5_Results
#       out_name: sturgis_points.shp
#       geometry_type: POINT
#       spatial_reference: NAD 1983 UTM Zone 13N (WKID = 26913)
#   b) Execute the CreateFeatureclass tool using the above variables and assign the
#       output of the CreateFeatureclass tool to a variable called "sturgis_pts".
#       Use sturgis_pts to print out geoprocessing messages. (5 points)
# Please add comments to explain what you are coding
# Write your code below

# Variables store the inputs for the CreateFeatureclass tool. Variables to be used in the tool
out_path = "C:/Users/siava/Documents/Workspace/gist603/Data/data/A5_Results"
out_name = "sturgis_points.shp"
geometry_type = "POINT"
spatial_reference = arcpy.SpatialReference(26913)

# Execute the CreateFeatureclass tool and assign the result to the sturgis_pts variable
sturgis_pts = arcpy.management.CreateFeatureclass(out_path, out_name, geometry_type, spatial_reference=spatial_reference)


# Print geoprocessing messages using the sturgis_pts variable
print(arcpy.GetMessages())


# End Q1
#################################################################################
# TODO Q2: Execute the AddField tool (10 points)
#   a) Execute the AddField tool using the following parameters. (5 points)
#           in_table = sturgis_pts
#           Field - name = WSHED, type = TEXT
#   b)  Assign the output of the AddField tool to a variable called
#       "add_field_result". Use add_field_result to print out geoprocessing
#       messages. (5 points)
# Please add comments to explain what you are coding
# Write your code below

# Variables store the inputs for the AddField tool. Variables to be used in the tool
in_table = sturgis_pts # Do not change this line
field_name = "WSHED"
field_type = "TEXT"

# Execute the AddField tool and assign the result to the add_field_result variable
add_field_result = arcpy.management.AddField(in_table, field_name, field_type)

# Print geoprocessing messages using the add_field_result variable

print(arcpy.GetMessages())

# End Q2
#################################################################################
# TODO Q3: Add features to the empty feature class. (30 points)
#   In this task, we will create point objects from coordinates that are given
#       in the pourpoints.csv file. The CSV file contains 4 columns - W_ID,
#       X_COORD, Y_COORD, NAME. We will insert these point objects, along with
#       their ID & NAME into our empty feature class from above.
#   a) Open the pourpoints.csv file in read mode. Use the "with" statement. (3 points)
#   b) Create a DictReader object to access its contents and use the for loop to
#       loop through each row of the DictReader object. (5 points)
#   c) Inside the for loop, create four variables id, wshed, x_coord & y_coord
#       to store the W_ID, NAME, X_COORD & Y_COORD, respectively, from the
#       iteration. Note that the X & Y coordinates are stored as strings in the
#       dictionary. You will have to use the float() function to convert the
#       X & Y coordinates to floats while assigning to the variables. (5 points)
#   d) Inside the for loop, create an arcpy.Point object using
#       the variables x_coord & y_coord from (c) and assign it to a variable
#       called "pt_obj". (3 points)
#   e) Inside the for loop, create an arcpy.PointGeometry object using the
#       variable pt_obj from (d) and assign this object to a variable called
#       "pt_geom" (3 points)
#   f) Inside the for loop, setup an InsertCursor on the attribute table of
#      sturgis_points.shp using the following parameters. Use the "with"
#      statement. (5 points)
#           in_table = sturgis_pts ... from Q2 (a)
#           field_names: "SHAPE@", "ID", & "WSHED" (Note: this order matters)
#   g) Inside the for loop, create a list that stores three variables as items and
#       assign this list to a variable called "in_row" in the given order. (3 points)
#           Item 1: pt_geom ... from (d)
#           Item 2: id ... from (c)
#           Item 3: wshed ... from (c)
#   h) Inside the for loop, use the .insertRow() method with in_row from (e) to
#       insert the record into the attribute table. (3 points)
# Please add comments to explain what you are coding
# Write your code below


# Open the given csv file in read mode using the "with" statement
csv_file_path = "C:/Users/siava/Documents/Workspace/gist603/Assignments/Module_5/pourpoints.csv"  # Replace with the actual path to the CSV file

with open(csv_file_path, 'r') as csvfile:

    # Create a DictReader object
    csv_reader = csv.DictReader(csvfile)


    # Access each row as a dictionary from the DictReader object using a for loop
    for row in csv_reader:


        # Using column names to access each item from the dictionary, Column names are keys in the dictionary
        # Variable stores the value in first column of CSV file, i.e. W_ID
        id = row['W_ID']


        # Variable stores the Value in second column of CSV file, i.e. NAME
        wshed = row['NAME']


        # Variable stores the value in third column of CSV file, i.e. X_COORD - convert to float
        x_coord = float(row['X_COORD'])


        # Variable stores the Value in fourth column of CSV file, i.e. Y_COORD - convert to float
        y_coord = float(row['Y_COORD'])


        # Print the variables id, wshed,  x_coord & y_coord, to verify their contents
        print(f"ID: {id}, WSHED: {wshed}, X_COORD: {x_coord}, Y_COORD: {y_coord}")


        # Create a Point object using the Point class and variables x_coord & y_coord
        pt_obj = arcpy.Point(x_coord, y_coord)


        # Create a Point Geometry object using the variables pt_obj
        pt_geom = arcpy.PointGeometry(pt_obj)


        # Inputs for the insert cursor: in_table & field_names. Variables to set up the cursor
        in_table = sturgis_pts # Do not change this line
        field_names = ["SHAPE@", "ID", "WSHED"]

        # Setup the Insert Cursor to access records using the "with" statement
        with arcpy.da.InsertCursor(in_table, field_names) as cursor:

            # Create a list of three items - pt_geom, id & wshed
            in_row = [pt_geom, id, wshed]


            # Insert the list using the .insertRow() method and the cursor
            cursor.insertRow(in_row)

# End Q3
#################################################################################
# TODO Q4: Create watersheds. (25 points)
#   You are given a variable "in_dem" that stores the path and name of the
#   topo30m raster available in ../ExploringSpatialData/Sturgis.gdb. You will
#   create watersheds using this dem and points from the previous question.
#   a) Execute the Fill tool using the following parameters, and assign the output
#       raster of the Fill tool to a variable called "dem_fill". Save the output
#       raster object permanently on disk in the A5_results folder using the name
#       "topo_f". Print geoprocessing messages using arcpy.GetMessages(). (5 points)
#           in_surface_raster = in_dem
#   b) Execute the FlowDirection tool using the following parameters, and assign
#       the output raster of the FlowDirection tool to a variable called "flow_dir".
#       Save the output raster object permanently on disk in the A5_results folder
#       using the name "topo_fd". Print geoprocessing messages using
#       arcpy.GetMessages(). (5 points)
#           in_surface_raster = dem_fill ... from (a)
#   c) Execute the FlowAccumulation tool using the following parameters, and assign
#       the output raster of the FlowAccumulation tool to a variable called
#       "flow_acc". Save the output raster object permanently on disk in the
#       A5_results folder using the name "topo_fa". Print geoprocessing messages
#       using arcpy.GetMessages(). (5 points)
#           in_flow_direction_raster = flow_dir ... from (b)
#   d) Execute the SnapPourPoint tool using the following parameters, and assign
#       the output raster of the SnapPourPoint tool to a variable called
#       "snap_pts". Save the output raster object permanently on disk in the
#       A5_results folder using the name "topo_pts". Print geoprocessing messages
#       using arcpy.GetMessages().(5 points)
#           in_pour_point_data = stur_pts ... from Q3(a)
#           in_accumulation_raster = flow_acc ... from (c)
#           snap_distance = 50
#   e) Execute the Watershed tool using the following parameters, and assign the
#       output raster of the Watershed tool to a variable called "watershed".
#       Save the output raster object permanently on disk in the A5_results folder
#       using the name "sheds". Print geoprocessing messages using
#       arcpy.GetMessages().(5 points)
#           in_flow_direction_raster = flow_dir ... from (b)
#           in_pour_point_data = snap_pts ... from (d)
# Please add comments to explain what you are coding
# Write your code below

# Variable stores the path and name of the input dem raster.
# TODO IMP: Change this path to the "../ExploringSpatialData/Sturgis.gdb/topo30m"
#  folder on your computer
in_dem = "C:/Users/siava/Documents/Workspace/gist603/Data/data/ExploringSpatialData/Sturgis.gdb/topo30m"

# Execute the Fill tool using the in_dem variable as input
dem_fill = arcpy.sa.Fill(in_dem)


# Save the raster output to disk as "topo_f"
dem_fill.save("C:/Users/siava/Documents/Workspace/gist603/Data/data/A5_Results/topo_f")


# Print geoprocessing messages using arcpy.GetMessages()
print(arcpy.GetMessages())


# Execute the FlowDirection tool using the dem_fill variable
flow_dir = arcpy.sa.FlowDirection(dem_fill)


# Save the raster output to disk as "topo_fd"
flow_dir.save("C:/Users/siava/Documents/Workspace/gist603/Data/data/A5_Results/topo_fd")


# Print geoprocessing messages using arcpy.GetMessages()
print(arcpy.GetMessages())


# Execute the FlowAccumulation tool using the variable flow_dir
flow_acc = arcpy.sa.FlowAccumulation(flow_dir)


# Save the raster output to disk as "topo_fa"
flow_acc.save("C:/Users/siava/Documents/Workspace/gist603/Data/data/A5_Results/topo_fa")


# Print geoprocessing messages using arcpy.GetMessages()
print(arcpy.GetMessages())


# Execute the SnapPourPoint tool using the variables stur_pts, flow_acc and a snap_distance of 50
snap_pts = arcpy.sa.SnapPourPoint(sturgis_pts, flow_acc, 50)


# Save the raster output to disk as "topo_pts"
snap_pts.save("C:/Users/siava/Documents/Workspace/gist603/Data/data/A5_Results/topo_pts")


# Print geoprocessing messages using arcpy.GetMessages()
print(arcpy.GetMessages())


# Execute the Watershed tool using the variables flow_dir and snap_pts
watershed = arcpy.sa.Watershed(flow_dir, snap_pts)


# Save the raster output to disk as "sheds"
watershed.save("C:/Users/siava/Documents/Workspace/gist603/Data/data/A5_Results/sheds")


# Print geoprocessing messages using arcpy.GetMessages()
print(arcpy.GetMessages())


# End Q4
#################################################################################
# TODO Q5: Reclassify the watersheds. (10 points)
#   In this task, you will reclassify the 9 watersheds to only 6 watersheds.
#   Watersheds with values 2, 3, 6 & 8 will be combined into a single watershed.
#   a) Use the sa.RemapValue class to create a RemapValue object to reflect the
#       following reclassification. Assign the RemapValue object to a variable
#       called "remap_value". (6 points)
#       Old Value --> New Value
#               1 --> 1
#               2 --> 2
#               3 --> 2
#               4 --> 3
#               5 --> 4
#               6 --> 2
#               7 --> 5
#               8 --> 2
#               9 --> 6
#   b) Execute the Reclassify tool using the following parameters, and assign
#       the output raster of the Reclassify tool to a variable called "r_ws".
#       Save the output raster object permanently on disk in the A5_results
#       folder using the name "r_sheds". (4 points)
#           in_raster = watershed ... from Q (e)
#           reclass_field: "VALUE"
#           remap = remap_value ... from (a)
# Please add comments to explain what you are coding
# Write your code below
from arcpy.sa import RemapValue, Reclassify

# Create a remap_value object based on the given reclassification
remap_value = RemapValue([[1, 1], [2, 2], [3, 2], [4, 3], [5, 4], [6, 2], [7, 5], [8, 2], [9, 6]])


# Execute the Reclassify tool using the variables watershed, remap_value.
r_ws = Reclassify(watershed, "VALUE", remap_value)


# Save the raster output to disk as "r_sheds"
r_ws.save("C:/Users/siava/Documents/Workspace/gist603/Data/data/A5_Results/r_sheds")


# Print geoprocessing messages using arcpy.GetMessages()
print(arcpy.GetMessages())


# End Q5
#################################################################################
# TODO Q6: List rasters and their properties (15 points)
#   a) Use an ArcPy List functions to create a list of all rasters in the
#       A5_results folder (2 points)
#   b) Setup a for loop to loop through this list. (2 points)
#   c) Inside this for loop, create a raster object for each raster in the
#       iteration. Assign the raster object to a variable called "ras". (3 points)
#   d) Inside the for loop, using the variable ras, print out the following
#       properties of the raster. (8 points)
#           1) Name
#           2) Coordinate System Name
#           3) Coordinate System Type
#           4) Coordinate System Linear Unit Name
#           5) Mean Cell Height
#           6) Mean Cell Width
#           7) Height
#           8) Width
# Please add comments to explain what you are coding
# Write your code below

# Create a list of rasters located in A5_results using an arcpy List function
rasters_list = arcpy.ListRasters("*", "ALL")


# Set up a for loop on the list
for raster in rasters_list:

    # Create a raster object for the raster in this iteration
    ras = arcpy.Raster(raster)


    #Print out raster properties using the variable ras
    print("Name:", ras.name)
    print("Coordinate System Name:", ras.spatialReference.name)
    print("Coordinate System Type:", ras.spatialReference.type)
    print("Coordinate System Linear Unit Name:", ras.spatialReference.linearUnitName)
    print("Mean Cell Height:", ras.meanCellHeight)
    print("Mean Cell Width:", ras.meanCellWidth)
    print("Height:", ras.height)
    print("Width:", ras.width)
    print("-----------------------------")

# End Q6
#################################################################################
# End of Assignment 5
#################################################################################
