import os
import shutil

# Create folders
os.makedirs("demo/source", exist_ok=True)
os.makedirs("demo/target", exist_ok=True)

# Create one file
with open("demo/source/file1.txt", "w", encoding="utf-8") as f:
    f.write("Hello")

# copy() -> copy file
shutil.copy("demo/source/file1.txt", "demo/target/file1_copy.txt")

# copytree() -> copy full folder
shutil.copytree("demo/source", "demo/source_backup", dirs_exist_ok=True)

# move() -> move file
shutil.move("demo/target/file1_copy.txt", "demo/source/file1_moved.txt")

# rmtree() -> delete folder tree
shutil.rmtree("demo/source_backup")

print("Done: copy, copytree, move, rmtree")
