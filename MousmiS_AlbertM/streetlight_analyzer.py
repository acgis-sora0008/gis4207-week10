# Global variables
import arcpy

streetlight_fc = r'C:\acgis\gis4207_prog\data\Ottawa\Street_Lights\Street_Lights.shp'
roads_cl_fc = r'C:\acgis\gis4207_prog\data\Ottawa\Road_Centrelines\Road_Centrelines.shp'
road_name_field = "ROAD_NAME_"

# Functions
def _get_unique_values(fc, field_name):
    
    unique_values = set()
    with arcpy.da.SearchCursor(fc, [field_name]) as cursor:
        for row in cursor:
            unique_values.add(row[0])
    return unique_values

def get_streetlight_count(road_name, distance):

    count = 0
    query = "{} = '{}'".format(arcpy.AddFieldDelimiters(roads_cl_fc, road_name_field), road_name)
    with arcpy.da.SearchCursor(roads_cl_fc, ["SHAPE@"], where_clause=query) as cursor:
        for row in cursor:
            for part in row[0]:
                for pnt in part:
                    for streetlight in arcpy.da.SearchCursor(streetlight_fc, ["SHAPE@"], spatial_reference=row[0].spatialReference):
                        if streetlight[0].distanceTo(pnt) <= distance:
                            count += 1
    return count

def save_streetlights(road_name, distance, out_fc):

    query = "{} = '{}'".format(arcpy.AddFieldDelimiters(roads_cl_fc, road_name_field), road_name)
    arcpy.SelectLayerByAttribute_management(roads_cl_fc, "NEW_SELECTION", query)
    arcpy.SelectLayerByLocation_management(streetlight_fc, "WITHIN_A_DISTANCE", roads_cl_fc, distance)
    arcpy.CopyFeatures_management(streetlight_fc, out_fc)

def show_road_names(pattern=None):

    if pattern:
        pattern = pattern.upper()
        query = "{} LIKE '%{}%'".format(arcpy.AddFieldDelimiters(roads_cl_fc, road_name_field), pattern)
    else:
        query = None
    with arcpy.da.SearchCursor(roads_cl_fc, [road_name_field], where_clause=query) as cursor:
        for row in cursor:
            print(row[0])




