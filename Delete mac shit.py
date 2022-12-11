from pathlib import Path
import shutil


your_path = input("Hello, enter the folder to get rid of mac specific files\n")
dir_to_clean = Path(your_path)

print("Following directories have been deleted:")

mac_dirs = list(dir_to_clean.rglob("__MACOSX"))
for i in mac_dirs:
	print(i)
	shutil.rmtree(i)

dir_del_templates = ["Ableton Project Info", "Backup"]
dirs = []
for i in dir_del_templates:
	dirs.extend(dir_to_clean.rglob(i))

for i in dirs:
	print(i)
	shutil.rmtree(i)

file_del_templates = [".DS_store", "Icon_", "*.als", "*.asd"]
files = []
for i in file_del_templates:
	files.extend(list(dir_to_clean.rglob(i)))

print("Following files have been deleted:")
for i in files:
	print(i)
	i.unlink()


'''
add manual input of file extensions and folder names
add manual submit before deleting
add exception if the list is empty
'''
