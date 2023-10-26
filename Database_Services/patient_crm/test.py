import time, logging as log
import subprocess

log.basicConfig(level=log.INFO)
# Function to run the external script
def run_external_script():
    subprocess.run(["python", "main.py"])

# Run the external script every 2 seconds
count = 0
while True:
    run_external_script()
    count += 1
    log.info(f"{count} Batch script executed successfully")
    time.sleep(2)