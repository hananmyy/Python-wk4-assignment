def handle_file_errors():
    while True:
        filename = input("Enter the filename to read: ")
        
        try:
            # Try to open and read the file
            with open(filename, 'r') as file:
                content = file.read()
                print("File content:")
                print(content)
            break  # Exit loop if file is successfully read
        
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist. Please try again.")
        except IOError as e:
            print(f"An error occurred while accessing the file: {e}.")
            break  # Exit on non-recoverable errors

# Usage example
handle_file_errors()
