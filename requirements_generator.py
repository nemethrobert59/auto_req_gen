import subprocess
import os

with open('my_path.txt','r') as file:
    YOUR_ROOT_PATH = file.read()

def get_first_level_subfolders(root_path):
    entries = os.listdir(root_path)
    first_level_subfolders = [entry for entry in entries if os.path.isdir(os.path.join(root_path, entry))]

    return first_level_subfolders

def main():
    YOUR_ROOT_PATH

    first_level_subfolders = get_first_level_subfolders(root_path=YOUR_ROOT_PATH)

    for first_level_subfolder in first_level_subfolders:
        repo_path = os.path.join(YOUR_ROOT_PATH,first_level_subfolder)
        try:
            command = ['pipreqs', repo_path, '--force']
            print("Executing command:", command[0] + " " + command[1] + " " + command[2])
            subprocess.check_call(command)
            print(f"requirements.txt generated successfully in {repo_path}")
        except FileNotFoundError:
            subprocess.check_call("pip install pipreqs")
            print("pipreqs has been installed, hence it was not present on your computer")
            command = ['pipreqs', repo_path, '--force']
            print("Executing command:", command[0] + " " + command[1] + " " + command[2])
            subprocess.check_call(command)
            print(f"requirements.txt generated successfully in {repo_path}")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()