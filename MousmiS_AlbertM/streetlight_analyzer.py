import arcpy

# Global variables
streetlight_fc = None
roads_cl_fc = None
road_name_field = None

# Functions
def _get_unique_values(fc, field_name):
    """
    Returns a set containing all unique values in the feature class (fc) from the provided field_name.
    This function is used by get_streetlight_count to check if the provided road_name is valid or not.
    """
    values = set()
    with arcpy.da.SearchCursor(fc, [field_name]) as cursor:
        for row in cursor:
            values.add(row[0])
    return values

def get_streetlight_count(road_name, distance):
    """
    Returns an integer with the count of all street lights within “distance” of line segment(s) where road_name_field = road_name.
    """
    if streetlight_fc is None or roads_cl_fc is None or road_name_field is None:
        raise ValueError("Global variables not set. Please set streetlight_fc, roads_cl_fc, and road_name_field.")

    # Use a SQL expression to select road segments with the given road name
    where_clause = f"{road_name_field} = '{road_name}'"
    arcpy.MakeFeatureLayer_management(roads_cl_fc, "selected_roads", where_clause)
    
    # Select streetlights within the specified distance of the selected road segments
    arcpy.SelectLayerByLocation_management(streetlight_fc, "WITHIN_A_DISTANCE", "selected_roads", distance)
    
    # Get the count of selected streetlights
    count = int(arcpy.GetCount_management(streetlight_fc).getOutput(0))
    
    # Clear selection
    arcpy.SelectLayerByAttribute_management(streetlight_fc, "CLEAR_SELECTION")
    arcpy.Delete_management("selected_roads")

    return count

def save_streetlights(road_name, distance, out_fc):
    """
    Saves the selected streetlights to a feature class (out_fc).
    The selected streetlights are within “distance” of the line segments where road_name_field = road_name.
    """
    if streetlight_fc is None or roads_cl_fc is None or road_name_field is None:
        raise ValueError("Global variables not set. Please set streetlight_fc, roads_cl_fc, and road_name_field.")

    # Use a SQL expression to select road segments with the given road name
    where_clause = f"{road_name_field} = '{road_name}'"
    arcpy.MakeFeatureLayer_management(roads_cl_fc, "selected_roads", where_clause)
    
    # Select streetlights within the specified distance of the selected road segments
    arcpy.SelectLayerByLocation_management(streetlight_fc, "WITHIN_A_DISTANCE", "selected_roads", distance)
    
    # Copy selected streetlights to the output feature class
    arcpy.CopyFeatures_management(streetlight_fc, out_fc)
    
    # Clear selection
    arcpy.SelectLayerByAttribute_management(streetlight_fc, "CLEAR_SELECTION")
    arcpy.Delete_management("selected_roads")

def show_road_names(pattern=None):
    """
    Prints the road_names to the console.
    The pattern argument can be lower, mixed, or upper case.
    If no pattern is specified, all road names will be printed.
    If a pattern is specified, then a LIKE %pattern% where clause will be used.
    This will help the user pass an appropriate road_name to get_streetlight_count.
    Since the ROAD_NAME_ field contains upper case values, if provided, the pattern should be converted to upper case.
    """
    if roads_cl_fc is None or road_name_field is None:
        raise ValueError("Global variables not set. Please set roads_cl_fc and road_name_field.")

    # Construct SQL where clause based on the pattern
    if pattern is None:
        where_clause = None
    else:
        pattern = pattern.upper()  # Convert pattern to upper case
        where_clause = f"{road_name_field} LIKE '%{pattern}%'"
    
    # Use a search cursor to iterate over road names
    with arcpy.da.SearchCursor(roads_cl_fc, [road_name_field], where_clause) as cursor:
        for row in cursor:
            print(row[0])