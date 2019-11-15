import os
import sys
import time
import datetime

os.chdir('HOME_DIR')

paths = ['DIR1', 'DIR2', 'DIR3']
days_count = 5

for path in paths:
    try:
        files = os.listdir(path)
    except FileNotFoundError:
        print("FileNotFoundError: files_deleter.py: Can not find the directory: " + path)
        sys.exit(0)

    current_time = time.time()

    if len(files) > days_count:
        for file in files:
            file_path = path + file
            creation_time = os.path.getmtime(file_path)
            passed_time = current_time - creation_time
            passed_days = passed_time // (3600 * 24)
            current_date = datetime.datetime.today().strftime("%d/%m/%Y(%H:%M)")
            if not os.path.isdir(os.path.join(path, file)):
                if passed_days >= 6:
                    try:
                        os.remove(file_path)
                        with open("cleaner.log", "a+") as log_file:
                            log_file.write(str(current_date) + ": File '" + file_path + "' successfully deleted!\n")
                            log_file.close()
                    except OSError:
                        with open("cleaner.log", "a+") as log_file:
                            log_file.write("Error: " + str(current_date) + ": File '" + file_path + "' can not be deleted!\n")
                            log_file.close()
