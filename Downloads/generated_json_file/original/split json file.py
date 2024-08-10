import json

def split_json_file(input_file, output_prefix, chunk_size=15):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Assuming data is a list of websites
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        output_file = f"{output_prefix}_{i // chunk_size + 1}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(chunk, f, indent=4)
        print(f"Created {output_file}")

# Usage
input_file = 'it_canada.json'
output_prefix = 'output'
split_json_file(input_file, output_prefix)
