import os

def delete_folder(folder_path):
    try:
 
        for root, dirs, files in os.walk(folder_path, topdown=False):
      
            for file in files:
                os.remove(os.path.join(root, file))

            for dir in dirs:
                os.rmdir(os.path.join(root, dir))

        os.rmdir(folder_path)
        print("Folder and all its contents deleted successfully.")
    except FileNotFoundError:
        print("Folder not found.")
    except PermissionError:
        print("Permission denied. Unable to delete the folder.")
    except Exception as e:
        print(f"An error occurred: {e}")


folder_path = 'TEST'
delete_folder(folder_path)
