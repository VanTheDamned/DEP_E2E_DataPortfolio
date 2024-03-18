## My First E2E Data Portfolio

This repository is created as part of the First End to End Data portfolio series of Josh Dev of Data Engineering Pilipinas

## Instructions

1. Clone this repository 
2. Create a virtual environment. `python -m venv env`
3. Activate virtual environment. for powershell `.\env\Scripts\Activate.ps1`
    *** In case you encounter an error when activating the virtual environment, try to run this command `Set-ExecutionPolicy Unrestricted -Scope Process` this sets the execution policy for the current PowerShell session to "Unrestricted".
4. Install the packages. `pip install -r .\requirements.txt`

## Week 1:
Installation of required/needed tech tools.
- Python
- VS Code (optional)
- SQL Server 2022 (Developer)
- Visual Studio
- SQL Server Data Tools (SSDT) for Visual Studio
- PostgreSQL
- PowerBI Desktop
- Git

## Week 2:
Created a local repository with virtual environment and requirements.txt file which includes the packages need for developing the pipeline 

- Used Git commands:
    - git init . #dot for current directory
    - git add . #dot for all changes
    - git commit -m "This is my commit message."
    - git rm your_file_name.ext #used to remove files
    - git push
    - git pull

- Synced alterations from Git local repository to GitHub through push and pull git commands.

## Week 3:
- Configured WSL.
- Configured and customized vsftpd
- Established a Python development environment.
- Established secure connectivity to an FTP server.
- Developed a pipeline for extracting and uploading data.
- Utilized a config.json file to optimize the data extraction process when reading CSV data from the web.
- Uploaded the CSV files to the FTP server and deleted it from the local filesystem afterward.
- Developed a script capable of executing the task either manually or on a scheduled basis.