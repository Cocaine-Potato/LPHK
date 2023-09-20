import os
import json

target_directory = "E:\\FILES\\GitHub\\LPHK\\user_layouts\\Huge_layout"  # Replace with your directory path

# Define the target content to replace within the JSON structure
target_content = "@LOAD_LAYOUT E:\\FILES\\GitHub\\LPHK\\user_layouts\\Huge_layout\\huge_1\\smol_1\\smolmain.lpl"
replacement_content = "@LOAD_LAYOUT E:\\FILES\\GitHub\\LPHK\\user_layouts\\Huge_layout\\huge_1\\smol_1\\smolmain.lpl"

def replace_content_in_json_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                
                # Assuming "buttons" is the key containing your list of lists
                if 'buttons' in data and isinstance(data['buttons'], list):
                    # Check if the last line of the JSON structure contains the target content
                    last_line = data['buttons'][-1]
                    if isinstance(last_line, list) and len(last_line) > 0:
                        last_item = last_line[-1]
                        if isinstance(last_item, dict) and 'text' in last_item and last_item['text'] == target_content:
                            # Modify the JSON data with the replacement content
                            last_item['text'] = replacement_content

                            # Write back the modified JSON
                            with open(file_path, 'w') as f:
                                json.dump(data, f, indent=2)
                            print(f'{file} changed in {file_path}')
            
            except Exception as e:
                print(f"Error processing {file_path}: {str(e)}")

replace_content_in_json_files(target_directory)
