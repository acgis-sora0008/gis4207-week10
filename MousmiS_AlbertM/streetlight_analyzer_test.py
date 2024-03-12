import arcpy
import streetlight_analyzer as sa

# Set global variables
sa.streetlight_fc = r'C:\acgis\gis4207_prog\data\Ottawa\Street_Lights\Street_Lights.shp'
sa.roads_cl_fc = r'C:\acgis\gis4207_prog\data\Ottawa\Road_Centrelines\Road_Centrelines.shp'
sa.road_name_field = "ROAD_NAME_"

# Test function
def test_get_streetlight_count():


# Perform selection by attribute on road centrelines
 Road_Carling = arcpy.management.SelectLayerByAttribute(sa.roads_cl_fc, where_clause="ROAD_NAME_ LIKE '%CARLING%'")

# Perform selection by location on street lights based on the selected road centrelines
 Street_Light_Selected = arcpy.management.SelectLayerByLocation(sa.streetlight_fc, "WITHIN_A_DISTANCE", Road_Carling, search_distance="0.0002 DecimalDegrees")




# Get the count of selected street lights
 selected_count = arcpy.management.GetCount(Street_Light_Selected).getOutput(0)
 expected_count = 849

# Assertions
 assert int(selected_count) == expected_count, f"Expected count: {expected_count}, Actual count: {selected_count}"





