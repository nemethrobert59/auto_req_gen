# Python Multi-Repository Requirements Management Tools

This repository hosts two powerful Python scripts that are crafted to streamline dependency management across multiple GitHub repositories. The `requirements_generator.py` script is adept at traversing through several repositories, automatically generating a `requirements.txt` file for each. Meanwhile, the `requirements_installer.py` script efficiently installs dependencies from these `requirements.txt` files across all specified repositories. This toolset is ideal for managing dependencies in complex projects involving multiple repositories, ensuring consistency and ease of setup.

## Scripts

### 1. requirements_generator.py

This script automatically scans a Python projects and generates a `requirements.txt` file. It identifies all the external libraries used in the project and lists them with their corresponding versions.

#### Usage

```bash
python requirements_generator.py --root_path <path_to_python_project>
```

### 2. requirements_installer.py
This script reads a requirements.txt files and installs all the listed Python packages. It's a convenient way to ensure that all necessary dependencies are installed for a project.

#### Usage

```bash
python requirements_installer.py --root_path <path_to_python_project>
```
## Installation
No additional installation is required for these scripts, as they are standalone Python scripts. However, they do assume that Python is already installed on your system.

