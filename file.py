filename = "demofile.txt"  

while True:  # Loop until user chooses to exit
    print("\nChoose an option:")
    print("1: Read")
    print("2: Write")
    print("3: Search")
    print("4: Append")
    print("5: Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        try:   
            with open(filename, "r") as f:   # Open file in read mode
                print("\n--- File Content ---")
                print(f.read())        # Read and print file content
        except FileNotFoundError:     # Handle file not found error
            print("\nFile not found.")

    elif choice == "2":
        text = input("Enter text to write: ")
        with open(filename, "w") as f:     # Open file in write mode
            f.write(text)          # Write user input to file
        print("\nFile written successfully.")

    elif choice == "3":
        word = input("Enter word to search: ")
        try:
            with open(filename, "r") as f:    # Open file in read mode
                content = f.read()
                if word in content:
                    print(f"\n'{word}' found in file.")
                else:
                    print(f"\n'{word}' not found.")
        except FileNotFoundError:  # Handle file not found error
            print("\nFile not found.")

    elif choice == "4":
        text = input("Enter text to append: ")
        with open(filename, "a") as f:   # Open file in append mode
            f.write("\n" + text)        # Append user input to file
        print("\nText appended successfully.")

    elif choice == "5":
        print("\nExiting program...")
        break

    else:
        print("\nInvalid choice! Please try again.")
