from playwright.sync_api import Page


class ScrollHelper:
    def __init__(self, page: Page):
        self.page = page

    def scroll_to_element(self, locator):
        """Scrolls the page until the given element is in view."""
        locator.scroll_into_view_if_needed()

    def scroll_by_pixels(self, pixels: int):
        """Scrolls the page vertically by a given number of pixels."""
        self.page.evaluate(
            f"window.scrollBy(0, {pixels});"
        )

    def scroll_to_top(self):
        """Scrolls to the top of the page."""
        self.page.evaluate(
            "window.scrollTo(0, 0);"
        )

    def scroll_to_bottom(self):
        """Scrolls to the bottom of the page."""
        self.page.evaluate(
            "window.scrollTo(0, document.body.scrollHeight);"
        )