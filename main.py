#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


# Get the invited names
with open("Input/Names/invited_names.txt") as invited_names:
    # Read names from "invited_names.txt"
    dirty_name_list = invited_names.readlines()
    print(f"Dirty Name List: {dirty_name_list}")

    # Clean these names from "invited_names.txt" i.e get rid of the '\n'.
    clean_name_list = []
    for actual_name in dirty_name_list:
        clean_name = actual_name.strip("\n")
        clean_name_list.append(clean_name)
    print(f"Clean Name List: {clean_name_list}\n")

# Replace the [name] placeholder with the clean (i.e. actual) name.
with open("Input/Letters/starting_letter.txt") as starting_letter:
    old = starting_letter.read() # Read everything in the file

    # Write a message with the actual_name and save it to 'Output/ReadyToSend/letter_to_actual_name'
    for actual_name in clean_name_list:
        new = old.replace("[name]", actual_name)
        with open(f"Output/ReadyToSend/letter_to_{actual_name}.txt", mode="w+") as output_message:
            output_message.write(new)