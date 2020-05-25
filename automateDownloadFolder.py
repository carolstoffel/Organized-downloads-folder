import os, shutil

print(os.getcwd()) # prints the actual folder
print(os.listdir()) # prints the files in actual folder
directory = "C:\\Users\\carol\\Downloads" # change here to your Downloads folder
dir = os.chdir("{}".format(directory)) #changes the directory to what is inside the directory variable

print('Currently directory: {}'.format(dir))

EXTENSIONS = {}
EXTENSIONS['EXT_AUDIO'] = ['.wav', '.mp3', '.raw', '.wma']
EXTENSIONS['EXT_VIDEO'] = ['.mp4', '.m4a', 'm4v', 'f4v', 'f4a', 'm4b', 'm4r', 'f4b', 'mov']
EXTENSIONS['EXT_DOCUMENTS'] = ['.txt', '.pdf', '.doc', '.docx', '.odt', '.html', '.csv', '.arff']
EXTENSIONS['EXT_IMAGE'] = ['.jpeg', '.png', '.sgv', '.gif', '.bmp' ]
EXTENSIONS['EXT_BOOKS'] = ['.epub']
EXTENSIONS['EXT_PROGRAMAS'] = ['.exe']
EXTENSIONS['EXT_COMPACT'] = ['.zip', '.rar']
EXTENSIONS['EXT_SCRIPT'] = ['.py']
DIRS = ['Audio', 'Videos', 'Documents', 'Images', 'Folders', 'Others', 'Books', 'Programas', 'Compact']

if not os.path.isdir('./Audio'):
    for d in DIRS:
        os.mkdir('./{}'.format(d))
        print('Created the {} directory'.format(d))


files = os.listdir()
for file in files:
    name, extension = os.path.splitext(file)
    if extension in EXTENSIONS['EXT_AUDIO']:
        shutil.move(file, './Audio/{}'.format(file))
    elif extension in EXTENSIONS['EXT_DOCUMENTS']:
        shutil.move(file, './Documents/{}'.format(file))
    elif extension in EXTENSIONS['EXT_VIDEO']:
        shutil.move(file, './Video/{}'.format(file))
    elif extension in EXTENSIONS['EXT_IMAGE']:
        shutil.move(file, './Images/{}'.format(file))
    elif extension in EXTENSIONS['EXT_BOOKS']:
        shutil.move(file, './Books/{}'.format(file))
    elif extension in EXTENSIONS['EXT_COMPACT']:
        shutil.move(file, './Compact/{}'.format(file))
    elif os.path.isdir(file) and file not in DIRS:
        shutil.move(file, './Folders/{}'.format(file))
    elif extension == '.pem' or extension == '.ppk':
        os.remove(file)
        print('File {} removed!'.format(file))
    elif extension in EXTENSIONS['EXT_PROGRAMAS']:
        shutil.move(file, './Programas/{}'.format(file))
    elif file not in DIRS and extension not in EXTENSIONS['EXT_SCRIPT']:
        shutil.move(file, './Others/{}'.format(file))
