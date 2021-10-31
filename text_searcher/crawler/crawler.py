from pathlib import Path

def get_files(basepath,verbose=False):
    '''
    Get all files existing in the path. 
    Args:
        basepath = string, root directory path 

    Return: 
        files_in_path = generator, contains list of all files in the basepath
    Next:
        support nested directories
    '''
    basepath = Path(basepath)
    files_in_path = (entry for entry in basepath.iterdir() if entry.is_file())
    if verbose:
        for item in files_in_path:
            print(item.name)
    return files_in_path


if __name__ == "__main__":
    ls = list(get_files("."))
    print([str(file) for file in ls])
    