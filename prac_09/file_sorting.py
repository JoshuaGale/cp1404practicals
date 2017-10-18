import shutil
import os


def main():
    os.chdir('FilesToSort')
    print(os.listdir('.'))

    for filename in os.listdir('.'):
        extension_name = os.path.splitext(filename)
        directory_name = extension_name[1]
        directory_name = directory_name.replace(".", "")
        print(directory_name)
        if directory_name in
    # os.mkdir()



main()
