import arcpy
import os

# Set the workspace
arcpy.env.workspace = "D:\topology\Contours.gdb"
# The name of the data_set containing the topology
data_set = "Contours"
# The name of the topology
topology = "contour_topology"

# Rules for topology
topoRules = ["Add Rule Here", "Add second rule here", "etc"]

# Get the fully qualified name/path of the topology
path_topology = os.path.join(arcpy.env.workspace, data_set, topology)
# Get the feature classes within the specified dataset
feature_classes = arcpy.ListFeatureClasses(feature_dataset = data_set)

# Check to make sure there are some feature classes
if feature_classes is not None:
# for each feature class
for fc in feature_classes:
		# Get the fully qualified path to the feature class
        	path_fc = os.path.join(arcpy.env.workspace, data_set, fc)
        		# Try and add the feature class to the topology
try:
     # add the feature class to the topology
                
arcpy.AddFeatureClassToTopology_management(path_topology, path_fc, 1, 1)
     # Try this here on a small dataset first.  

arcpy.AddRuleToTopology_management(path_topology, “Must not intersect (line)”[0], path_fc)


except Exception as e:
	# print any errors we might get
print(e)
