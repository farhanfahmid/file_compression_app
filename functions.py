import zipfile
import pathlib

def make_archive(filepaths, destination):
    dest_path = pathlib.Path(destination, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath) #to make sure that extracting the zip file gives the compressed files directly instead of giving them in a bunch of subdirectories
            archive.write(filepath, arcname=filepath.name)

def extract_archive(filepaths, destination):
    with zipfile.ZipFile(filepaths, 'r') as file:
        file.extractall(destination)

