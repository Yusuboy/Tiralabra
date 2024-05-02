import os

TEXT_FILE_FOLDER = "src/textfiles"
BINARY_FILE_FOLDER = "src/BinFiles"
DECOMPRESSED_FILE_FOLDER = "src/decompressedFiles"
CLEAN_FOLDERS = ["src/BinFiles", "src/decompressedFiles"]


def is_txt_file(file_path):
    return file_path.lower().endswith(".txt")

def get_file_size(file_path):
    return os.path.getsize(file_path)

def list_files(folder, file_type):
    files = [file for file in os.listdir(folder) if file.endswith(file_type)]
    return files


def delete_files_in_folder(folder):
    files = os.listdir(folder)
    for file in files:
        file_path = os.path.join(folder, file)
        os.remove(file_path)
