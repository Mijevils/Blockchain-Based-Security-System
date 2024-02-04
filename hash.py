import hashlib
import os

path = r'C:\Windows\System32\WDI\LogFiles\StartupInfo'
superhash = "" # hashstring containing all file hashes
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
        superhash += sha256.hexdigest() # hash for this file added to hashstring
        print('#############################################')
        print('{}: {}'.format(sha256.name, sha256.hexdigest()))
        print()

sha256 = hashlib.sha256()
sha256.update(superhash.encode('utf-8')) # creation of superhash with hashstring
print(sha256.hexdigest())