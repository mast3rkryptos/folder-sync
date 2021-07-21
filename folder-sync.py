import os
import shutil

from datetime import datetime

sourcePath = "C:\\project_files"
sourceExcludedPaths = ["C:\\project_files\\cds\\T2080",
                       "C:\\project_files\\criis_piu_release_tags",
                       "C:\\project_files\\git",
                       "C:\\project_files\\svn"]
destinationPath = "U:\\folder-sync-backups"
numBackups = 2

startTime = datetime.now()

# Prepare the destination directory
for i in range(numBackups, 0, -1):
    if i == numBackups and os.path.exists(os.path.join(destinationPath, str(i))):
        print("Removing oldest backup: " + os.path.join(destinationPath, str(i)))
        shutil.rmtree(os.path.join(destinationPath, str(i)))
    elif os.path.exists(os.path.join(destinationPath, str(i))):
        print(f"Moving backup: {os.path.join(destinationPath, str(i))} -> {os.path.join(destinationPath, str(i+1))}" )
        os.rename(os.path.join(destinationPath, str(i)), os.path.join(destinationPath, str(i+1)))
print("Creating backup destination: " + os.path.join(destinationPath, str(1)))
os.mkdir(os.path.join(destinationPath, str(1)))

# Create backup to destination directory
print("Creating backup")
for root, dirs, files in os.walk(sourcePath):
    skip = False
    for sourceExcludedPath in sourceExcludedPaths:
        if sourceExcludedPath in root:
            skip = True
    if not skip and not os.path.exists(os.path.join(destinationPath, "1", root.replace(sourcePath + "\\", ""))):
        os.mkdir(os.path.join(destinationPath, "1", root.replace(sourcePath + "\\", "")))
        for file in files:
            if not file.startswith("~$"):
                shutil.copyfile(os.path.join(root, file), os.path.join(destinationPath, "1", root.replace(sourcePath + "\\", ""), file))

# Print out script runtime
print("\nRuntime:", datetime.now() - startTime)
