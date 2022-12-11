from pathlib import Path


def get_dirs(directory):
	for i in directory.iterdir():
		if i.is_dir():
			if any(i.iterdir()) is False:
				i.rmdir()
				print(i)
			else:
				get_dirs(i)


your_path = input("Input the folder in which you wish to delete empty subfolders\n")
dir_to_clean = Path(your_path)
print("Removed empty folders:")
get_dirs(dir_to_clean)
