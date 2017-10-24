import shutil
import os


def main():
    os.chdir('FilesToSort')
    print(os.listdir('.'))
    file_extensions = []

    for filename in os.listdir('.'):
        extension_name = filename.split(".")[1]
        if extension_name not in file_extensions:
            file_extensions.append(extension_name)
            os.mkdir(extension_name)
        shutil.move(filename, extension_name)

main()
