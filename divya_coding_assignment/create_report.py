# Question 3
# Parse this CSV and write a method that takes the data structure and prints out a summary report by crop, indicating the number of fields and total area for each crop. Format it exactly like this:
# 
# Crop Area Summary:
# corn: 3 fields (38.76 ha)
# wheat: 3 fields (131.78 ha)
# barley: 2 fields (33.23 ha)
csv_string = '''
field_name,crop,area_ha
Jones,corn,12.42
Robin,corn,22.12
Chris,wheat,35.34
Fran,barley,10.90
Rick,wheat,77.22
Carl,barley,22.33
Louise,wheat,19.22
Beth,corn,4.22
'''.strip()

def genrate_report_output(csv_string):
    # Recommended to use python3
    final_output_dict = {}
    header, *contents = csv_string.split("\n")
    
    for content in contents:
        _, crop, area_ha = content.split(",")
        if final_output_dict.get(crop):
            pass
            final_output_dict[crop]["field"] += 1
            final_output_dict[crop]["area_ha"] += float(area_ha)

        else:
            final_output_dict[crop] = {
                "field": 1,
                "area_ha": float(area_ha)
            }
    
    print("Crop Area Summary:")

    for crop, crop_data in final_output_dict.items():
        print(f"{crop}: {crop_data['field']} fields ({crop_data['area_ha']} ha)")

genrate_report_output(csv_string)