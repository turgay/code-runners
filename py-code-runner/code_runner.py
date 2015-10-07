import subprocess
import time
import platform
import tempfile
import shutil
import os

if platform.system() == 'Windows':
    RUN_LOCATION = "\\tmp\\"
else:
    RUN_LOCATION = "/tmp/"

TIME_OUT = 1

class CodeRunner:

    def __init__(self):
        pass

    def run_with_timeout(self, cmd, timeout):
        process = subprocess.Popen(cmd, bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        poll_seconds = .250
        deadline = time.time()+timeout
        while time.time() < deadline and process.poll() == None:
            time.sleep(poll_seconds)

        if process.poll() is None:
            process.terminate() # after 2.6
            time.sleep(0.1)
            return "", "timeout", 0

        std_out, std_err = process.communicate()
        return std_out, std_err, process.returncode

    def run(self, code, timeout=TIME_OUT):

        current_location = os.getcwd()

        if not os.path.exists(RUN_LOCATION):
            os.makedirs(RUN_LOCATION)

        working_dir = tempfile.mkdtemp(prefix="run_", dir=RUN_LOCATION)

        os.chdir(working_dir)
        main_code_file_name = "main.py"
        code_file = open(main_code_file_name, "w")
        code_file.write(code)
        code_file.close()

        std_out, std_err, result = self.run_with_timeout('python ' + main_code_file_name, timeout=1)

        os.chdir(current_location)
        shutil.rmtree(working_dir)

        return std_err, std_out
