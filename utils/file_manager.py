import os
from typing import List, Tuple


class FileManager:
    def __init__(self, base_dir: str) -> None:
        self.base_dir: str = base_dir

    def check_directory(self, dir_path: str) -> bool:
        is_dir: bool = os.path.isdir(dir_path)
        print(f"{dir_path} is {'a valid' if is_dir else 'not a valid'} directory!\n")
        return is_dir

    def get_image_files(
        self, directory: str, extensions: Tuple[str, ...] = ("jpg", "png", "jpeg")
    ) -> List[str]:
        return [
            os.path.join(directory, file)
            for file in os.listdir(directory)
            if file.lower().endswith(extensions)
        ]

    def create_directory(self, dir_name: str) -> None:
        os.makedirs(dir_name, exist_ok=True)
        print(
            f"Directory {dir_name} {'exists' if os.path.exists(dir_name) else 'created'}."
        )
