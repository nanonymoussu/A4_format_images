import os
from typing import List

from utils.file_manager import FileManager
from utils.pdf_generator import PDFGenerator


def process_images(base_dir: str) -> None:
    file_manager = FileManager(base_dir=base_dir)
    pdf_generator = PDFGenerator()

    orgs: List[str] = [
        org
        for org in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, org))
    ]
    for org_name in orgs:
        print(f"Processing org: {org_name}")
        org_dir: str = os.path.join(base_dir, org_name)

        image_paths: List[str] = file_manager.get_image_files(directory=org_dir)
        if not image_paths:
            print(f"No images found for {org_name}. Skipping...")
            continue

        output_dir: str = os.path.join(os.getcwd(), "output", org_name)
        file_manager.create_directory(dir_name=output_dir)

        # Group images into chunks and generate PDFs
        for i, group in enumerate(iterable=chunk_list(lst=image_paths, chunk_size=7)):
            output_pdf: str = os.path.join(output_dir, f"{org_name}_{i + 1}.pdf")
            pdf_generator.create_pdf(output_filename=output_pdf, image_paths=group)
            print(f"PDF created: {output_pdf}")

        print()


def chunk_list(lst: List[str], chunk_size: int) -> List[List[str]]:
    """Splits a list into smaller chunks."""
    return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]


if __name__ == "__main__":
    image_dir: str = os.path.join(os.getcwd(), "images")
    file_manager = FileManager(base_dir=image_dir)
    if file_manager.check_directory(dir_path=image_dir):
        process_images(base_dir=image_dir)
