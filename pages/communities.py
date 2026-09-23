from playwright.sync_api import Page

class Communities:

    COMMUNITY_POST_CARD = "//div[@class='panel panel-default']"
    COMMUNITY_POST_TIME = "//div[@class='created-at']"
    CREATE_YOUR_POST_TEXT = "//div[@class='panel-body']//div[@class='text-center']"
    ADD_POST_TITLE = "//input[@id='communitybundle_newpost_title']"
    ADD_POST_DESCRIPTION = "//textarea[@id='communitybundle_newpost_description']"
    ADD_POST_SELECT_COMMUNITY = "//select[@id='communitybundle_newpost_community']"
    ADD_POST_UPLOAD_IMAGE = "//input[@id='communitybundle_newpost_image']"
    ADD_POST_SUBMIT_BUTTON = "//button[@type='submit' and contains(text(), 'Submit')]"
    COMMUNITY_LISTS = "//div[@id='sidebar-left']//img[@class='img-icon']"
    LOADER = "//input[@name='loadPostUrl']"
    POST_MENUS = "//i[@class='fa fa-ellipsis-v']"
    DELETE_POST = "//a[@id='delete-post-link']"
    ARE_YOU_SURE_DELETE_BUTTON = "//button[@data-bb-handler='confirm']"
    OK_SUCCESS_DELETE_BUTTON = "//button[@data-bb-handler='ok']"

    def __init__(self, page: Page):
        self.page = page

    def get_community_post_cards(self, i: int):
        """
        Return the community post card at the given index.
        """
        community_post_cards = self.page.locator(self.COMMUNITY_POST_CARD)
        return community_post_cards.nth(i)

    def get_community_post_time(self, i: int):
        """
        Return the text of the community post time at the given index.
        """
        community_post_times = self.page.locator(self.COMMUNITY_POST_TIME)
        return community_post_times.nth(i).inner_text()

    def navigate_to_my_post(self, base_url):
        self.page.goto(base_url + "/import-export-communities/my-posts")

    def navigate_to_add_post(self, base_url):
        self.page.goto(base_url + "/import-export-communities/add-post")

    def filling_the_add_post_form(
        self,
        title,
        description,
        community
    ):
        self.page.locator(self.ADD_POST_TITLE).fill(title)
        self.page.locator(self.ADD_POST_DESCRIPTION).fill(description)
        self.page.locator(self.ADD_POST_SELECT_COMMUNITY).select_option(label=community)
        self.page.locator(self.ADD_POST_SUBMIT_BUTTON).click()

    def navigate_to_communities_and_test_posts(self, i: int):
        """
        Click a community from the community list using its index.
        """
        community_list_elements = self.page.locator(self.COMMUNITY_LISTS)
        community_list_elements.nth(i).click()

    def delete_communities_test_post(self, base_url):
        """
        Navigate to My Posts and delete the first post.
        """
        self.navigate_to_my_post(base_url)

        post_menus = self.page.locator(self.POST_MENUS)
        post_menus.first.click()
        self.page.locator(self.DELETE_POST).click()
        self.page.locator(self.ARE_YOU_SURE_DELETE_BUTTON).click()
        self.page.locator(self.OK_SUCCESS_DELETE_BUTTON).click()