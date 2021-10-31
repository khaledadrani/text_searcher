import sys
import os
from pathlib import Path

if __name__ == "__main__":
    print(sys.argv)
    path = str(sys.argv[1])
    #print(os.listdir(path))

    # with os.scandir(path) as entries:
    #     for entry in entries:
    #         print(entry.name)

    # entries = Path(path)
    # print(entries, entries.resolve())
    # for entry in entries.iterdir():
    #     print(entry.name, entry.parent, entry.stem, entry.suffix, entry.anchor)

    # List all files in a directory using os.listdir
    basepath = path
    # for entry in os.listdir(basepath):
    #     if os.path.isfile(os.path.join(basepath, entry)):
    #         print(entry)
    basepath = Path(path)
    #files_in_basepath = basepath.iterdir()
    # for item in files_in_basepath:
    #     if item.is_file():
    #         print(item.name)

    files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
    for item in files_in_basepath:
        print(item.name)