import os

username = "admin:admin123"

local = "http://localhost:8081"

repo = "/repository/repository-name"

def run_fast_scandir(dir, ext):    # dir: str, ext: list
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)


    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)
    return subfolders, files


def run_cmd_command(files,folder_location):
    for file in files:
        # print(file)
        folder= file.split('\\',folder_location)
        # print(x[1])
        command = "curl -v --user \"{}\" --upload-file \"{}\" {}{}/{}".format(username,file,local,repo,folder[folder_location])
        # print(command)
        print(os.popen(command))


subfolders, files = run_fast_scandir("D:\\UpdateSiteExport", [".jar"])
run_cmd_command(files,1)

