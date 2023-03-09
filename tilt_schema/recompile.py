def reconstruct():
    import os
    import json
    import glob 

    """
    func:   Constructs the tilt-schema out of a number of constituent parts.
    """

    
    properties_sections = sorted(glob.glob('properties/*.json'))

    
    print(properties_sections)
    
    # Update the properties file with the underlying values 
    # Note: presupposes that all changes to the properties have been made in the properties-folder
    data_props = []
    for subfile in properties_sections:

        with open(subfile, 'r') as sf:
            data_props.append(json.load(sf))
            
    combo_props = {}
    for item in data_props:
        combo_props.update(item)
        
    # Write the combined data to a the properties file
    with open('06_properties.json', 'w') as f:
        json.dump({'properties':combo_props}, f)
    
    meta_sections = sorted(glob.glob("*.json"))
    print(meta_sections)


    # Create an empty list to hold the data from each file
    data = []

    # Iterate over each JSON file and load its contents into the data list
    for file in meta_sections:
        with open(file, 'r') as f:
            data.append(json.load(f))

    # Combine all the data into a single dictionary
    combined_data = {}
    for item in data:
        combined_data.update(item)

    
    # Write the combined data to a new JSON file
    with open('../combined.json', 'w') as f:
        json.dump(combined_data, f)
        print('successfully created new json')

    os.remove("06_properties.json")

    return

if __name__== "__main__":
    reconstruct()