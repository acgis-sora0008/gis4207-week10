import arcpy
import streetlight_analyzer as sa

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






