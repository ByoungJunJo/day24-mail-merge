# day24-mail-merge
## Summary
- Create a letter using starting_letter.txt for each name in invited_names.txt.
- Replace the [name] placeholder with the actual name.
- Save the letters in the folder "ReadyToSend".
- Create a letter with each name
```
# Write a message with the actual_name and save it to 'Output/ReadyToSend/letter_to_actual_name'
  for actual_name in clean_name_list:
      new = old.replace("[name]", actual_name)
      with open(f"Output/ReadyToSend/letter_to_{actual_name}.txt", mode="w+") as output_message:
          output_message.write(new)
```
- Read and write from text files
```
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
```
##Lessons
- Don't worry too much about how clean or fancy your code is. If it does what it's supposed to do and you understand your own code, that's good.
- I should start reading [The Art of Computer Programming by Donald Knuth](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming)
- Avoid the premature optimization. It's okay your code and your instructor code are different. We all think differently so the code should look different. (But if it does what it's supposed to do, that's fine.)
