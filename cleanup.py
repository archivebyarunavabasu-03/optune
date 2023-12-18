import os
import shutil

def clean_up(folders):
    for folder in folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"Deleted '{folder}' folder.")
        else:
            print(f"'{folder}' folder does not exist.")

    print("Cleanup complete.")

if __name__ == "__main__":
    folders_to_clean = ['build', 'dist', 'optune/optune.egg-info']
    clean_up(folders_to_clean)
