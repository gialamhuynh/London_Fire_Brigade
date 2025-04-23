import os
import subprocess
from datetime import datetime
import time

# Custom wait time in seconds
WAIT_TIME = 5  # Wait time of 60 seconds (can be adjusted)

# Wait before starting the test
print(f"Waiting for {WAIT_TIME} seconds before starting the test...")
time.sleep(WAIT_TIME)
print("Waiting time expired. Starting the test...")

# Get the directory path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
print('script_dir:',script_dir)
# Navigate to the project directory (two parent directories up from the script directory)
project_dir = os.path.dirname(script_dir)
print('project_dir:',project_dir)

# Set the path to the module
module_path = os.path.join(project_dir, "src", "features", "jr_preprocessing.py")
print('module_path:',module_path)

# Set the path to the log.txt file in the tests directory
log_file_path = os.path.join(project_dir, "tests", "log.txt")
print('log_file_path:',log_file_path)

# Check if log.txt exists in the tests directory, if not, create it
if not os.path.exists(log_file_path):
    open(log_file_path, "w").close()
    

# Get the current date and time
date_time = datetime.now()

# Format the date and time with two decimal places for seconds
formatted_date_time = date_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-4]

# Write the start time to the log file
with open(log_file_path, "a") as log_file:
    log_file.write("\n====================================\n")
    log_file.write(f"Start test on 'jr_preprocessing.py': \n{formatted_date_time}\n")
    log_file.write("====================================\n")
    



# Test whether the script executes successfully
def test_script_execution():
    # Get the absolute path to the script
    script_path = os.path.join(project_dir, "src/features/jr_preprocessing.py")
    print('script_path:', script_path)
    # Define the command to execute the script
    command = f"python {script_path}"
    # Execute the command and check if it runs successfully
    try:
        process = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        # Print the process output
        print("Process output:", process.stdout)
        # Get the current datetime from the program
        current_datetime = os.environ.get('CURRENT_DATETIME')
        # Write the test result to log.txt in the tests directory
        with open(log_file_path, "a") as log_file:
            log_file.write("====================================\n")
            log_file.write("pytest: \"jr_preprocessing.py\"\n")
            log_file.write("Time of execution: {}\n".format(current_datetime))
            log_file.write("test_script_execution(): Success\n")
            log_file.write("====================================\n")
    except subprocess.CalledProcessError as e:
        # Write the error information to log.txt
        with open(log_file_path, "a") as log_file:
            log_file.write("====================================\n")
            log_file.write("pytest: \"jr_preprocessing.py\"\n")
            log_file.write("test_script_execution(): Failure\n")
            log_file.write(f"Reason: The script execution failed\n{e.stderr}\n")
            log_file.write("====================================\n")

# Test whether the output file is created
def test_output_file_creation():
    # Construct the path to the output file relative to the project directory
    output_file_path = os.path.join(project_dir, "data/processed/df_mi5_5.csv")
    print('\noutput_file_path:', output_file_path)
    if os.path.exists(output_file_path):
        result = "Success"
    else:
        result = "Failure"
    # Write the test result to log.txt in the tests directory
    with open(log_file_path, "a") as log_file:
        log_file.write("====================================\n")
        log_file.write("pytest: \"jr_preprocessing.py\"\n")
        log_file.write("test_output_file_creation(): ")
        log_file.write(result + "\n")
        log_file.write("====================================\n")








