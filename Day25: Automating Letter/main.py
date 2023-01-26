
with open(".\Input\\Names\invited_names.txt") as name_file:
    name_list = name_file.readlines()

with open(".\Input\Letters\starting_letter.txt") as letter:
    letter_text = letter.read()
    for i in name_list:
        stripped_i = i.strip()
        with open(f".\Output\ReadyToSend\Letter_To_{stripped_i}.txt", mode="w") as writing_letter:
            letter_fix = letter_text.replace("[name]", stripped_i)
            writing_letter.write(f"{letter_fix}")

