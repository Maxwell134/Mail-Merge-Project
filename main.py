PLACEHOLDER = "[name]"
reader = "./input/Names/invited_names.txt"
sender = "./input/Letters/starting_letter.txt"
with open(reader) as source:
    names = source.read().splitlines()

with open(sender, 'r') as destination:
    letter_contents = destination.read()
    for name in names:
        new_text = letter_contents.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for{name}.txt", mode='w') as new:
            new.write(new_text)



