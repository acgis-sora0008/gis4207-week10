import arcpy
import streetlight_analyzer as sa
import os

# Set global variables
sa.streetlight_fc = r'C:\acgis\gis4207_prog\data\Ottawa\Street_Lights\Street_Lights.shp'
sa.roads_cl_fc = r'C:\acgis\gis4207_prog\data\Ottawa\Road_Centrelines\Road_Centrelines.shp'
sa.road_name_field = "ROAD_NAME_"


def test_get_unique_values():

    fc = r'C:\acgis\gis4207_prog\data\Ottawa\Road_Centrelines\Road_Centrelines.shp'
    field_name="ROAD_NAME_"
    
    unique_values = sa._get_unique_values(fc, field_name)
    
    contains_carling = any("CARLING" in value for value in unique_values)

    assert contains_carling, f"No value containing 'CARLING' found in unique values: {unique_values}"



def test_get_streetlight_count():
    expected_count = 849
    road_name = "CARLING"
    distance = 0.0002  # Distance should be a float value, not a string

    actual_count = int(sa.get_streetlight_count(road_name, distance))
    assert actual_count == expected_count
    
    
def test_save_streetlights():
    # Define test parameters
    road_name = 'CARLING'
    distance = 0.0002
    out_fc = r'C:\acgis\gis4207_prog\data\Ottawa\Street_Lights\Streetlights_within_carling.shp'
    

    # Define paths to mock data
    streetlight_fc = r'C:\acgis\gis4207_prog\data\Ottawa\Street_Lights\Street_Lights.shp'
    roads_cl_fc = r'C:\acgis\gis4207_prog\data\Ottawa\Road_Centrelines\Road_Centrelines.shp'
    road_name_field = "ROAD_NAME_"

    # Create mock feature classes if they don't exist
    if not arcpy.Exists(streetlight_fc):
        arcpy.CreateFeatureclass_management(os.path.dirname(streetlight_fc), os.path.basename(streetlight_fc), "POINT")
    if not arcpy.Exists(roads_cl_fc):
        arcpy.CreateFeatureclass_management(os.path.dirname(roads_cl_fc), os.path.basename(roads_cl_fc), "POLYLINE")

    # Run the function to save streetlights
    sa.save_streetlights(road_name, distance, out_fc, streetlight_fc, roads_cl_fc, road_name_field)

    # Check if the output feature class was created
    assert arcpy.Exists(out_fc), "Output feature class was not created."

    # Clean up - delete the output feature class
    arcpy.Delete_management(out_fc)
    
    
def test_show_road_names():
    # Define test parameters
    pattern = "Main"  # Test pattern to filter road names
    
    # Mock data paths
    roads_cl_fc = r'C:\acgis\gis4207_prog\data\Ottawa\Road_Centrelines\Road_Centrelines.shp'
    road_name_field = "ROAD_NAME_"
    
    # Create mock feature class if it doesn't exist
    if not arcpy.Exists(roads_cl_fc):
        arcpy.CreateFeatureclass_management(os.path.dirname(roads_cl_fc), os.path.basename(roads_cl_fc), "POLYLINE")
    
    # Populate the mock feature class with some test data
    # (This step can vary depending on your specific test scenario)
    
    # Run the function to show road names with the specified pattern
    print("Road Names with pattern '{}'".format(pattern))
    sa.show_road_names(pattern)
    
    # Ensure no errors occurred during execution
    # (This could involve additional checks based on the specific behavior of your function)
    print("Test completed successfully.")

    



   
    