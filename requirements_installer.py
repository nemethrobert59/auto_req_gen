import argparse
from pathlib import Path
import os
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--root_path")
parser.add_argument("--overwrite_req", default="False")
args = parser.parse_args()

YOUR_ROOT_PATH = Path(args.root_path)

def get_first_level_subfolders(root_path):
    entries = os.listdir(root_path)
    first_level_subfolders = [entry for entry in entries if os.path.isdir(os.path.join(root_path, entry))]

    return first_level_subfolders

def execute_command(req_file_path):
    command = ['pip install', req_file_path]
    print("Executing command:", command[0] + " " + command[1])
    subprocess.check_call(command)

def main():
    if not YOUR_ROOT_PATH.is_dir():
        print("The root directory doesn't exist")
        raise SystemExit(1)

    first_level_subfolders = get_first_level_subfolders(root_path=YOUR_ROOT_PATH)

    for first_level_subfolder in first_level_subfolders:
        req_file_path = os.path.join(YOUR_ROOT_PATH,first_level_subfolder,'requirements.txt')
        print(req_file_path)
        execute_command(req_file_path)

if __name__ == "__main__":
    main()