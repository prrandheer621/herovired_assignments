# Q4. In DevOps, performing regular backups of important files is crucial:
# ●       Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.
# ●       The script should copy all files from the source directory to the destination directory.
# ●       Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.
# ●       Handle errors gracefully, such as when the source directory or destination directory does not exist.
# Sample Command:
# python backup.py /path/to/source /path/to/destination
# By running the script with the appropriate source and destination directories, it should create backups of the files in the source directory, ensuring unique file names in the destination directory.

import sys, os, shutil
from datetime import datetime

def copy_files_of_current_directory(source_folder, destination_folder):
  try:
    for file_name in os.listdir(source_folder):
      source_path = source_folder + '\\' + file_name
      destination_path = destination_folder + '\\' + file_name

      if os.path.isfile(source_path):
        if os.path.isfile(destination_path):
          filename_split = file_name.split('.')
          destination_path = destination_folder + '\\' + '.'.join(filename_split[0: -1]) + '_' + datetime.now().strftime('%d-%m %H-%M-%S') + '.' + filename_split[-1]

        shutil.copy(source_path, destination_path)
      else:
        if not os.path.exists(destination_path):
          os.makedirs(destination_path)
        copy_files_of_current_directory(source_path, destination_path)
        # shutil.copytree(source_folder + '\\' + file_name, destination_folder + '\\' + file_name, dirs_exist_ok=True)

  except FileNotFoundError as e:
    print('FileNotFoundError: ', e)

  except NotADirectoryError as e:
    print('NotADirectoryError: ', e)

try:
  source_folder = sys.argv[1]
  destination_folder = sys.argv[2]
  copy_files_of_current_directory(source_folder, destination_folder)

except IndexError:
  print('IndexError: ', 'Expected script: python backup.py /path/to/source /path/to/destination')
