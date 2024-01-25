import hashlib
import os

path = r'C:\Windows\System32\WDI\LogFiles\StartupInfo'

for filename in os.listdir(path):
    f = os.path.join(path, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)

    fullpath = path + '\\' + filename
    with open(fullpath, 'rb') as opened_file:
        content = opened_file.read()
        sha256 = hashlib.sha256()

        sha256.update(content)

        print('#############################################')
        print('{}: {}'.format(sha256.name, sha256.hexdigest()))
        print()