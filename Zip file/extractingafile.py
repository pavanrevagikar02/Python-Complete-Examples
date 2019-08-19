from  zipfile import *
 # Create a ZipFile Object and load sample.zip in it
with ZipFile('myfile.zip', 'r') as zipObj:

# Extract all the contents of zip file in different directory
    zipObj.extractall('temporaryfile')


# Extracting a zip file
# # Create a ZipFile Object and load sample.zip in it
# with ZipFile('files.zip', 'r') as zipObj:

# Extract all the contents of zip file in different directory
#     zipObj.extractall('temp')