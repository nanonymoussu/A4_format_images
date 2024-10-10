from typing import List, Tuple

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas


class PDFGenerator:
    def __init__(self, page_size: Tuple[float, float] = A4) -> None:
        self.page_size: Tuple[float, float] = page_size

        self.image_width: float = 2.5 * cm
        self.image_height: float = 3.5 * cm

        self.images_per_row: int = 6
        self.rows_per_page: int = 7

    def create_pdf(self, output_filename: str, image_paths: List[str]) -> None:
        width, height = self.page_size
        _canvas = canvas.Canvas(filename=output_filename, pagesize=self.page_size)

        horizontal_spacing: float = (width - self.images_per_row * self.image_width) / (
            self.images_per_row + 1
        )
        vertical_spacing: float = (height - self.rows_per_page * self.image_height) / (
            self.rows_per_page + 1
        )

        for person_index in range(min(self.rows_per_page, len(image_paths))):
            for col in range(self.images_per_row):
                image_index: int = person_index
                if image_index < len(image_paths):
                    x_position: float = horizontal_spacing + col * (
                        self.image_width + horizontal_spacing
                    )
                    y_position: float = height - (
                        vertical_spacing
                        + (person_index + 1) * self.image_height
                        + person_index * vertical_spacing
                    )
                    _canvas.drawImage(
                        image=image_paths[image_index],
                        x=x_position,
                        y=y_position,
                        width=self.image_width,
                        height=self.image_height,
                    )

        _canvas.save()
