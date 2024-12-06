def read_and_write_file(input_file, output_file):
    try:
        # Read the contents of the input file
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File has been modified and saved as '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError as e:
        print(f"An error occurred while reading or writing files: {e}")

# Usage example
read_and_write_file('input.txt', 'output.txt')
