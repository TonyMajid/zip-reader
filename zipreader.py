import os
import getpass
import glob
import zipfile

def find_logged_in_user():
    return getpass.getuser()

def find_most_recent_zip(downloads_folder):
    zip_files = glob.glob(os.path.join(downloads_folder, '*.zip'))
    if not zip_files:
        return None
    most_recent_zip = max(zip_files, key=os.path.getctime)
    return most_recent_zip

def find_file_in_zip(zip_path, target_file_name):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            if file_name.endswith(target_file_name):
                with zip_ref.open(file_name) as target_file:
                    lines = target_file.readlines()
                    if len(lines) > 1:
                        return lines[1].decode('utf-8').strip()
    return None

def main():
    user = find_logged_in_user()
    downloads_folder = os.path.join("C:\\Users", user, "Downloads")
    zip_path = find_most_recent_zip(downloads_folder)

    if not zip_path:
        print("No zip files found in the Downloads folder.")
        return

    second_line = find_file_in_zip(zip_path, "part-0000")

    if second_line is None:
        print("The file 'part-0000' was not found in the most recent zip file or it does not have a second line.")
    else:
        print("The second line of the file 'part-0000' is:")
        print(second_line)

if __name__ == "__main__":
    main()
