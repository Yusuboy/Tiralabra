import os

TEXT_FILE_FOLDER = "src/textfiles"
BINARY_FILE_FOLDER = "src/BinFiles"
DECOMPRESSED_FILE_FOLDER = "src/decompressedFiles"
CLEAN_FOLDERS = ["src/BinFiles", "src/decompressedFiles"]


def is_txt_file(file_path):
    """
    Checks if the given file path corresponds to a text file (.txt).

    Args:
        file_path (str): The path of the file to be checked.

    Returns:
        bool: True if the file is a text file, False otherwise.
    """
    return file_path.lower().endswith(".txt")

def get_file_size(file_path):
    """
    Retrieves the size of a file.

    Args:
        file_path (str): The path of the file for which size is to be retrieved.

    Returns:
        int: The size of the file in bytes.
    """
    return os.path.getsize(file_path)

def list_files(folder, file_type):
    """
    Lists files of a specific type in the given folder.

    Args:
        folder (str): The path of the folder to list files from.
        file_type (str): The type of files to list (e.g., ".txt", ".bin").

    Returns:
        list: A list of filenames with the specified file type in the folder.
    """
    files = [file for file in os.listdir(folder) if file.endswith(file_type)]
    return files


def delete_files_in_folder(folder):
    """
    Deletes all files in the given folder.

    Args:
        folder (str): The path of the folder from which files are to be deleted.
    """
    files = os.listdir(folder)
    for file in files:
        file_path = os.path.join(folder, file)
        os.remove(file_path)
