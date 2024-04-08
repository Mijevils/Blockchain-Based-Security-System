import hashlib
import os

class Encrypt():
    """
    Class to create the superhash given an array of protected files
    """
    def __init__(self):
        self.superhash = "" # string containing all hashes that will then be converted into a final superhash

    def makeHash(self, path):
        """
        Description: Makes a superhash combining hashes of all files within a given a directory
        Inputs: Self, as well as a string path containing the path of the directory to hash
        Output: The superhash, as a string
        """
        self.superhash = ""

        for file in path:
            sha = hashlib.sha256()  # defines the hashing function (sha256)
            #for filename in os.listdir(file):  # iterate through all files in given directory
            #    f = os.path.join(file, filename)
            #    # checking if it is a file
            #    if os.path.isfile(f):
            #        print(f)  # if file exists, print the name

            #    fullpath = each + '\\' + filename  # determine full path of the file for hash creation
            with open(file, 'rb') as opened_file:
                content = opened_file.read()
                sha.update(content)  # hash computed based on file content
                self.superhash += sha.hexdigest()  # hash for this file added to hashstring
                # print('{}: {}'.format(sha.name, sha.hexdigest()))
                # print()

        return self.makeSuperhash()

    def makeSuperhash(self):
        """
        Description: Auxiliary function to calculate the hash of the hashstring
        Input: self
        Output: String containing the superhash
        """
        sha = hashlib.sha256()
        sha.update(self.superhash.encode('utf-8')) # creation of superhash with hashstring
        # print(self.sha.hexdigest())

        return sha.hexdigest()


#a = Encrypt()
#a.makeHash("")