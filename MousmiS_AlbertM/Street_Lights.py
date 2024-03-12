import arcpy
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.SelectLayerByLocation(
    in_layer="Street_Lights",
    overlap_type="WITHIN_A_DISTANCE",
    select_features="Road_Centrelines",
    search_distance="0.0002 DecimalDegrees",
    selection_type="NEW_SELECTION",
    invert_spatial_relationship="NOT_INVERT"
)
