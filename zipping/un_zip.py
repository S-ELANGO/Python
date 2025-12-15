import zipfile

with zipfile.ZipFile('documents.zip','r')as zipf:
    zipf.extractall()

print("Files extracted successfully")
