import arcpy
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="Road_Centrelines",
    selection_type="NEW_SELECTION",
    where_clause="ROAD_NAME_ LIKE '%CARLING%'",
    invert_where_clause=None
)
