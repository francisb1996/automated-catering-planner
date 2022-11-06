# Automated Catering Planner
This script is designed to process a catering order PDF and export a detailed plan for catering staff.

## Python setup for windows
1. Download the Python installer here: https://www.python.org/downloads/
2. Run installer, making sure to select "Add python.exe to PATH"
3. After install completes, run `python --version` and `pip --version` to make sure the install was successful
    * If commands fail, try restarting your computer

## VSCode setup for Python
1. Download the `Python` Extension 
2. Create `.vscode/settings.json` and the following. Be sure to add your own Windows user and change python version if necessary. (Assuming defualt install path of Python 3.11):
```
{
    "python.pythonPath": "C:\\Users\\<Insert User Here>\\AppData\\Local\\Programs\\Python\\Python311\\python.exe"
}
```


## Run script
`python process.py <input file path>`

## Debugging
A VSCode configuration is included in this project. Place breakpoints and run the `Process` configuration in the `Run and Debug` tab. This will process the Test PDF in the project.

## Output
Output files are written to the `output/` directory