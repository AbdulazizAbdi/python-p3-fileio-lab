def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode = 'w', encoding = 'utf-8') as written_file:
        written_file.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode = 'a', encoding = 'utf-8') as appended_file:
        appended_file.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt', mode = 'r', encoding = 'utf-8') as readin_file:
        return readin_file.read()
