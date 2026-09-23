import os
from datetime import datetime

class ScreenshotUtil:
    @staticmethod
    def save_screenshot(page, name_prefix="screenshot"):
        reports_dir = os.path.join(os.path.dirname(__file__), '../reports')
        os.makedirs(reports_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(reports_dir, f"{name_prefix}_{timestamp}.png")
        page.screenshot(path=file_path)
        return file_path
