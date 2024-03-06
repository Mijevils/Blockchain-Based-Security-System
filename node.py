import subprocess

def connect():
    try:
        # Replace 'your_task_name' with the actual Hardhat task you want to execute
        task_name = 'your_task_name'

        # Run the Hardhat task using subprocess
        result = subprocess.run(['npx', 'hardhat', task_name], capture_output=True, text=True)

        # Print the result
        print(result.stdout)

        # Check for errors
        if result.returncode != 0:
            print(f"Error: {result.stderr}")

    except Exception as e:
        print(f"An error occurred: {e}")

connect()