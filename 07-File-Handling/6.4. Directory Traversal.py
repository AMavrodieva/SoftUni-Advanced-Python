from os.path import sep, isdir, join
from os import listdir


def directory_traversal(file_path, result):
    for el in listdir(file_path):
        if isdir(join(file_path, el)):
            directory_traversal(join(file_path, el), result)
        else:
            extension = el.split('.')[-1]
            if extension not in result:
                result[extension] = []
            result[extension].append(el)


result = {}
path = f'.{sep}'
directory_traversal(path, result)
sorted_result = sorted(result.items(), key=lambda x: (x[0], x[1]))
with open(f'.{sep}result.txt', 'w') as output_file:

    for extension, files in sorted_result:
        output_file.write('.' + extension + '\n')
        for file in files:
            output_file.write(f'- - - {file}\n')

