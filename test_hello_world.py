#!/Library/installapplications/Python.framework/Versions/Current/bin/python3

import os

def main():
    """Simple test script that creates a hello world file on user's desktop"""
    
    # Get the current user's desktop directory
    desktop_dir = os.path.expanduser("~/Desktop")
    
    # Create the hello world file path
    hello_file = os.path.join(desktop_dir, "hello_world.txt")
    
    # Write hello world content
    with open(hello_file, 'w') as f:
        f.write("Hello World!\nThis is a test file created by InstallApplications test script.\n")
    
    print(f"Successfully created hello world file at: {hello_file}")
    
    # Verify the file was created
    if os.path.exists(hello_file):
        print("Test script completed successfully!")
        return 0
    else:
        print("Error: Failed to create test file")
        return 1

if __name__ == "__main__":
    exit(main())