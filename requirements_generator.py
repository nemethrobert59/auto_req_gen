import subprocess
import os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--root_path")
parser.add_argument("--overwrite_req", default="False")
args = parser.parse_args()

YOUR_ROOT_PATH = Path(args.root_path)
try:
    OVERWRITE_REQ = eval(args.overwrite_req.lower().capitalize())
except:
    print("The overwrite_req argument does not contain valid value, please use true or false")
    raise SystemExit(1)
def get_first_level_subfolders(root_path):
    entries = os.listdir(root_path)
    first_level_subfolders = [entry for entry in entries if os.path.isdir(os.path.join(root_path, entry))]

    return first_level_subfolders

def execute_command(repo_path, overwrite_req):
    if overwrite_req == True:
        command = ['pipreqs', repo_path, '--force']
        print("Executing command:", command[0] + " " + command[1] + " " + command[2])
    else:
        command = ['pipreqs', repo_path]
        print("Executing command:", command[0] + " " + command[1])
    subprocess.check_call(command)
    print(f"requirements.txt generated successfully in {repo_path}")

def main():
    if not YOUR_ROOT_PATH.is_dir():
        print("The root directory doesn't exist")
        raise SystemExit(1)

    first_level_subfolders = get_first_level_subfolders(root_path=YOUR_ROOT_PATH)

    for first_level_subfolder in first_level_subfolders:
        repo_path = os.path.join(YOUR_ROOT_PATH,first_level_subfolder)
        try:
            execute_command(repo_path, overwrite_req = OVERWRITE_REQ)
        except FileNotFoundError:
            subprocess.check_call("pip install pipreqs")
            print("pipreqs has been installed, hence it was not present on your computer")
            execute_command(repo_path, overwrite_req=OVERWRITE_REQ)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()