import os
import shutil
import getpass

user = getpass.getuser()  # gets automatically the system user name
directory = "C:\\Users\\{}\\Downloads".format(user)
# changes the directory to what is inside the directory variable
dir = os.chdir("{}".format(directory))

EXTENSIONS = {}
EXTENSIONS['Audio'] = ['.wav', '.mp3', '.raw', '.wma']
EXTENSIONS['Videos'] = ['.mp4', '.m4a', 'm4v',
                        'f4v', 'f4a', 'm4b', 'm4r', 'f4b', 'mov']
EXTENSIONS['Documents'] = ['.txt', '.pdf',
                           '.doc', '.docx', '.odt', '.html', '.csv', '.arff', '.xls', '.xlsx']
EXTENSIONS['Images'] = ['.jpeg', '.png', '.sgv', '.gif', '.bmp']
EXTENSIONS['Books'] = ['.epub']
EXTENSIONS['Programas'] = ['.exe']
EXTENSIONS['Compact'] = ['.zip', '.rar']


files = os.listdir()
for i in EXTENSIONS.keys():
    fold = './' + i
    if not os.path.isdir(fold):
        os.mkdir(fold)
        print('Created the {} directory'.format(i))
    for file in files:
        name, extension = os.path.splitext(file)
        if extension == '.py':
            continue
        if extension in EXTENSIONS[i]:
            shutil.move(file, './{}/{}'.format(i, file))
            print('File {} moved to {}'.format(file, i))
        elif extension == '.pem' or extension == '.ppk':
            os.remove(file)
            print('File {} removed!'.format(file))
