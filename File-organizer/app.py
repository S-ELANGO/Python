import shutil
from pathlib import Path

target_dir = Path("")

cat = {
    'Videos': ['mp4', 'mkv']
}
def organize_files(folder: Path):
    for file in folder.iterdir():
        if file.is_file():
            moved = False

            for category, extensions in cat.items():
                if file.suffix.lower().lstrip('.') in extensions:
                    category_dir = folder / category
                    category_dir.mkdir(exist_ok=True)
                    shutil.move(str(file), category_dir / file.name)
                    moved = True
                    break

            if not moved:
                other_dir = folder / 'Other'
                other_dir.mkdir(exist_ok=True)
                shutil.move(str(file), other_dir / file.name)

if __name__ == '__main__':
    organize_files(target_dir)
    print("File organized successfully ✅")
