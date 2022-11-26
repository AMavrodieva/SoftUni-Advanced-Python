from reading import read_until_command
from os import sep, remove
from os.path import exists
command_parts = [str(x).split('-') for x in read_until_command("End")]
# print(command_parts)
for el in command_parts:
    command, file_name = el[0], el[1]
    if command == "Create":
        with open(f'.{sep}{file_name}', 'w') as file:
            pass
    elif command == "Add":
        text = el[2]
        with open(f'.{sep}{file_name}', 'a') as file:
            file.write(text + '\n')
    elif command == "Replace":
        if not exists(f'.{sep}{file_name}'):
            print(f'An error occurred')
            continue
        old_text, new_text = el[2], el[3]
        with open(f'.{sep}{file_name}', 'r+') as file:
            file_content = file.read().replace(old_text, new_text)
            file.seek(0)
            file.truncate()
            file.write(file_content)
    elif command == "Delete":
        if not exists(f'.{sep}{file_name}'):
            print(f'An error occurred')
            continue
        remove(f'.{sep}{file_name}')
