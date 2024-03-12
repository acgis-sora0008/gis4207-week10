import arcpy
import streetlight_analyzer

streetlight_analyzer.streetlight_fc = r'C:\acgis\gis4207_prog\data\Ottawa\Street_Lights\Street_Lights.shp'
streetlight_analyzer.roads_cl_fc = r'C:\acgis\gis4207_prog\data\Ottawa\Road_Centrelines\Road_Centrelines.shp'

def test_get_streetlight_count():

    road_name = "ExampleRoad"
    distance = 0.0002


    actual_streetlight_count = streetlight_analyzer.get_streetlight_count(road_name, distance)


    expected_streetlight_count = 39  
    assert actual_streetlight_count == expected_streetlight_count

test_get_streetlight_count()