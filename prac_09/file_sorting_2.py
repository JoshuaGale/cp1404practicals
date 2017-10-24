import shutil
import os


def main():
    os.chdir('FilesToSort')
    print(os.listdir('.'))
    file_categorise = {}

    for filename in os.listdir('.'):
        extension_name = filename.split(".")[1]
        if extension_name not in file_categorise.keys():
            category = input("What category would you like to sort {} files into? ".format(extension_name))
            if category not in file_categorise.values():
                os.mkdir(category)
            file_categorise[extension_name] = category
        shutil.move(filename, file_categorise[extension_name])

main()
