# -------------------------------------------------------------------------------
# Name:        Assignment6_withHints.py
# Purpose:     Script for Assignment6
# Author:      Dr. Yoganand Korgaonkar
# Student Name: Siavash Habibi
# -------------------------------------------------------------------------------
#################################################################################
# TODO: Instructions:
#   - You are free to experiment in Python Window if you like.
#   - Your code should still execute error free as a script in this file.
#   - The data can be found in the Assignment6 folder in the zip file provided
#       on D2L
#################################################################################

#################################################################################
# TODO Q1: ArcGIS Project Properties (10 points)
#   a) Open the .../Assignment6/UnitedStates/UnitedStates.aprx project in Python
#       and assign it to a variable. (2 point)
#   b) Save a copy of this project using the name UnitedStates_copy.aprx (2 point)
#   c) Open the UnitedStates_copy.aprx project in Python and assign it to a
#       variable called "aprx". You will use this variable throughout this code
#       to access the project. (2 point)
#   d) Access and print out the following ArcGIS Project properties using the
#       variable aprx from (c). (4 points)
#       - Date Saved
#       - Default Geodatabase
#       - File Path
#       - Home Folder
# Please add comments to explain what you are coding
# Write your code below

# Imports
import arcpy
arcpy.env.overwriteOutput = True

# Open the given UnitedStates.aprx ArcGIS project and assign it to a variable
original_project_path = "C:/Users/siava/Documents/Workspace/gist603/Data/data/Assignment6/UnitedStates/UnitedStates.aprx"  # Replace with the actual path
project = arcpy.mp.ArcGISProject(original_project_path)

# Save a copy of the project as UnitedStates_copy.aprx
copy_project_path = "C:/Users/siava/Documents/Workspace/gist603/Data/data/Assignment6/UnitedStates/UnitedStates_copy.aprx"  # Replace with the actual path
project.saveACopy(copy_project_path)

# Close the project
del project

# Open the copied project and store in variable called aprx
aprx = arcpy.mp.ArcGISProject(copy_project_path)


# Access and print out project properties using the variable aprx
print("Date Saved:", aprx.dateSaved)
print("Default Geodatabase:", aprx.defaultGeodatabase)
print("File Path:", aprx.filePath)
print("Home Folder:", aprx.homeFolder)

# End Q1
#################################################################################
# TODO Q2: Fix Broken Data Sources (10 points)
#   a) Use the variable aprx from Q1 (c) to create a list of all layers with
#       broken data sources. Assign this list to a new variable. (2 points)
#   b) Setup a for loop to loop through this list. (2 points)
#   c) Inside this for loop, access and print the connection properties for each
#       layer with a broken data source. (2 points)
#   d) Inside the for loop, update the geodatabase path using the following
#       correct path and update the connection properties. (4 points)
#       Path = <your computer path>/Assignment6/Assignment6.gdb
# Please add comments to explain what you are coding
# Write your code below


# Create a list of all datasets with broken data sources using the variable aprx
broken_layers = []
for m in aprx.listMaps():
    for layer in m.listLayers():
        if layer.isBroken:
            broken_layers.append(layer)
# Set up a  for loop on the list
for layer in broken_layers:



    # Access the connection properties for each layer
    conn_props = layer.connectionProperties



    # Print the connection properties
    print("Original Connection Properties:", conn_props)



    # Correct path to broken data sources
    correct_path = "C:/Users/siava/Documents/Workspace/gist603/Data/data/Assignment6/Assignment6.gdb"  # Replace with the actual path


    # Update the broken GDB path
    if 'workspace_path' in conn_props:
        conn_props['workspace_path'] = correct_path

    # Update the connection properties
    layer.updateConnectionProperties(layer.connectionProperties, conn_props)


    # Print the connection properties t verify change
    print("Updated Connection Properties:", layer.connectionProperties)


# Save the project
aprx.save()


# End Q2
#################################################################################
# TODO Q3: Map Properties (10 points)
#   a) Access the "USA Map" from the project using the variable aprx and assign
#       the map to a new variable called "usa_map". (2 point)
#   b) Print out the following properties of "USA Map" map using the variable
#       usa_map. (8 points)
#       - Map Name
#       - Map Units
#       - Spatial Reference - Projected Coordinate System
#       - Spatial Reference - Central Meridian
#       - Spatial Reference - Latitude of Origin
#       - Spatial Reference - Standard Parallel 1
#       - Spatial Reference - Standard Parallel 2
#       - Spatial Reference - Linear Unit Name
# Please add comments to explain what you are coding
# Write your code below

# Access the USA Map from the project using the variable aprx, assign to variable usa_map
usa_map = aprx.listMaps("USA Map")[0]


# Print Map properties using the usa_map variable
print("Map Name:", usa_map.name)
print("Map Units:", usa_map.mapUnits)
spatial_ref = usa_map.spatialReference

print("Spatial Reference - Projected Coordinate System:", spatial_ref.name)
print("Spatial Reference - Central Meridian:", spatial_ref.centralMeridian)
print("Spatial Reference - Latitude of Origin:", spatial_ref.latitudeOfOrigin)
print("Spatial Reference - Standard Parallel 1:", spatial_ref.standardParallel1)
print("Spatial Reference - Standard Parallel 2:", spatial_ref.standardParallel2)
print("Spatial Reference - Linear Unit Name:", spatial_ref.linearUnitName)


# End Q3
#################################################################################
# TODO Q4: Layer Properties (25 points)
#   a) Use the variable usa_map from Q3 (a) to create a list of all layers in the
#       map. Assign this list to a new variable. Setup a for loop to loop through
#       this list. (3 points)
#   b) Inside the for loop from (a), use an if condition to check if the layer
#       "supports" the "name" property. Print the name of the layer using the
#       "name" property when the condition is True. (5 points)
#   c) Inside the if statement from (b), use the "name" property and an if
#       statement to check for the "States" layer. Turn on the labels using the
#       "labels" property for the "States" layer. (5 points)
#   d) Inside the if statement from (b), use the "name" property and an if statement
#       to check for the "Cities" layer. Hide the "Cities" layer using the "visible"
#       property. (4 points)
#   e) Inside the for loop from (a), use an if condition to check if the layer
#       "supports" the "brightness" property. Print the brightness of the layer
#       using the "brightness" property when the condition is True. (4 points)
#   f) Inside the for loop from (a), use an if condition to check if the layer
#       "supports" the "transparency" property. Print the transparency of the layer
#       using the "transparency" property when the condition is True. (4 points)
# Please add comments to explain what you are coding
# Write your code below

# Access all layers form the map using the variable usa_map
layers_list = usa_map.listLayers()


# Set up a for loop on the list
for layer in layers_list:


    # Check if the name property is supported by the layer
    if layer.supports("name"):
        # Print the name if the property is supported
        print("Layer Name:", layer.name)


        # Use an if condition to check if the layer name is "States"
        if layer.name == "States":


            # Show labels for the "States" layer using the "labels" property
            if layer.supports("labels"):
                layer.labels.visible = True
                print("Labels for 'States' layer are now visible.")

        # Use an if condition to check if the layer name is "Cities"
        if layer.name == "Cities":


            # Hide the "Cities" layer using the "visible" property
            layer.visible = False
            print("The 'Cities' layer is now hidden.")

    # Check if the brightness property is supported by the layer
    if layer.supports("brightness"):


        # Print the brightness if the property is supported
        print("Layer Brightness:", layer.brightness)


    # Check if the transparency property is supported by the layer
    if layer.supports("transparency"):


        # Print the transparency if the property is supported
        print("Layer Transparency:", layer.transparency)


# Save the project
aprx.save()



# End Q4
#################################################################################
# TODO Q5: Moving Layers (20 points)
#   a) Create two layer objects for the "Interstates" & "Rivers" layers in the
#       map and assign each of them to a variable. (4 points)
#   b) Move the "Interstates" layer to a position after the "Rivers" layer using
#       the variables form (a). (4 points)
#   c) Create two layer objects for the "Counties" & "States" layers in the
#       map and assign each of them to a variable. (4 points)
#   d) Move the "Counties" layer to a position before the "States" layer using
#       the variables form (c). (4 points)
#   e) Create a layer object for the "climatestations" layer in the map and assign to
#       a variable. (2 points)
#   f) Remove the "climatestations" layer from the map using the variable
#       from (e). (2 points)
# Please add comments to explain what you are coding
# Write your code below

# Create a layer object for the "Interstates" layer and assign to a variable
interstates_layer = usa_map.listLayers("Interstates")[0]


# Create a layer object for the "Rivers" layer and assign to a variable
rivers_layer = usa_map.listLayers("Rivers")[0]


# Move the interstates layer after rivers (Write line twice because of bug)
usa_map.moveLayer(rivers_layer, interstates_layer, "AFTER")
usa_map.moveLayer(rivers_layer, interstates_layer, "AFTER")

# Create a layer object for the "Counties" layer and assign to a variable
counties_layer = usa_map.listLayers("Counties")[0]


# Create a layer object for the "States" layer and assign to a variable
states_layer = usa_map.listLayers("States")[0]


# Move the counties layer before states (Write line twice because of bug)
usa_map.moveLayer(states_layer, counties_layer, "BEFORE")
usa_map.moveLayer(states_layer, counties_layer, "BEFORE")

# Create a layer object for the "climatestations" layer and assign to a variable
climatestations_layer = usa_map.listLayers("climatestations")[0]


# Remove the climatestations layer
usa_map.removeLayer(climatestations_layer)


# Save the project
aprx.save()



# End Q5
#################################################################################
# TODO Q6: Working with Symbology (25 points)
#   a) Create a layer objects for the "Counties" layer in the map and assign it
#       to a variable. (2 points)
#   b) Access the symbology of the layer using the variable from (a) and assign
#       the symbology object to a new variable. (2 points)
#   c) Use the variable from (b) and an if condition to to check if the symbology
#       has a "renderer" attribute. (2 points)
#   d) Update the symbology of the "Counties" layer as follows when the condition
#       is True. (3 points)
#       - Renderer: UniqueValueRenderer
#       - Renderer Field: STATE_NAME
#   e) Create a layer objects for the "Rivers" layer in the map and assign it
#       to a variable. (2 points)
#   f) Access the symbology of the layer using the variable from (e) and assign
#       the symbology object to a new variable. (2 points)
#   g) Use the variable from (f) and an if condition to to check if the symbology
#       has a "renderer" attribute. (2 points)
#   h) Update the symbology of the "Rivers" layer as follows when the condition
#       is True. (10 points)
#       - Renderer: GraduatedSymbolsRenderer
#       - Renderer Classification Field: MILES
#       - Renderer Classification Method: QUANTILE
#       - Renderer Break Count: 8
#       - Renderer Minimum Symbol Size: 1
#       - Renderer Maximum Symbol Size: 10
#       - Renderer ColorRamp: <Any of your choice>
# Please add comments to explain what you are coding
# Write your code below

# Create a layer object for the "Counties" layer and assign to a variable
counties_layer = usa_map.listLayers("Counties")[0]


# Access the symbology of the layer and assign to a new variable
counties_symbology = counties_layer.symbology


# Check if the symbology has a renderer attribute
if hasattr(counties_symbology, "renderer"):


    # Update the renderer to UniqueValueRenderer
    counties_symbology.updateRenderer('UniqueValueRenderer')


    # Set the renderer field to STATE_NAME
    counties_symbology.renderer.fields = ["STATE_NAME"]


    # Apply the modified symbology back to the layer
    counties_layer.symbology = counties_symbology


# Create a layer object for the "Rivers" layer and assign to a variable
rivers_layer = usa_map.listLayers("Rivers")[0]


# Access the symbology of the layer and assign to a new variable
rivers_symbology = rivers_layer.symbology


# Check if the symbology has a renderer attribute
if hasattr(rivers_symbology, "renderer"):


    # Update the renderer to GraduatedSymbols
    rivers_symbology.updateRenderer('GraduatedSymbolsRenderer')


    # Set the Classification field to MILES
    rivers_symbology.renderer.classificationField = "MILES"


    # Set the Classification method to QUANTILE
    rivers_symbology.renderer.classificationMethod = "QUANTILE"


    # Set the Break Count to 8
    rivers_symbology.renderer.breakCount = 8


    # Set the Minimum Symbol Size to 1
    rivers_symbology.renderer.minSymbolSize = 1


    # Set the Maximum Symbol Size to 10
    rivers_symbology.renderer.maxSymbolSize = 10


    # Access a color ramp from the project color ramps and assign to a variable
    color_ramp = aprx.listColorRamps()[0]

    # Set the renderer color ramp to the above color ramp
    rivers_symbology.renderer.colorRamp = color_ramp


    # Apply the modified symbology back to the layer
    rivers_layer.symbology = rivers_symbology


# Save the project
aprx.save()



# End Q6
#################################################################################
# End of Assignment 6
#################################################################################
