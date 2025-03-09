PLACEHOLDER = "[name]"

with open("C:/Users/ascom/Desktop/Python_Challenge/Day_21/Input/Names/invited_names.txt") as name_file:
    invited_people = name_file.readlines()

with open ("C:/Users/ascom/Desktop/Python_Challenge/Day_21/Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in invited_people:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"C:/Users/ascom/Desktop/Python_Challenge/Day_21/Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as send_file:
            send_file.write(new_letter)

