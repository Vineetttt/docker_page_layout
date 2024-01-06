import sys
import json
import os
from helpers import get_layout_from_single_image, read_config

config = read_config()

layout = get_layout_from_single_image("data")
response = layout.model_dump(mode='json')

with open("data/out.json","w") as f:
    json.dump(response,f)

'''
def main(image_path):
    try:
        layout = get_layout_from_single_image(image_path)
        print("Layout information:")
        print(layout)

        # Create a new directory 'results' if it doesn't exist
        output_directory = "/results"
        os.makedirs(output_directory, exist_ok=True)

        # Save the layout information in a JSON file
        output_path = f"{output_directory}/{os.path.basename(image_path)}.json"
        with open(output_path, 'w') as json_file:
            json.dump(layout, json_file, indent=2)

        print(f"Layout information saved in: {output_path}")
        return layout
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python inference.py <image_path>")
    else:
        image_path = sys.argv[1]
        main(image_path)
'''