import time
from datetime import datetime
from utils.scroll_helper import ScrollHelper
from playwright.sync_api import expect
from pages.communities import Communities
from pages.loginpage import LoginPage
from utils.logger import get_logger
from utils.user_data_loader import get_valid_user


logger = get_logger("CommunityPostsTest")


def test_communities_all_page(page, base_url):
    communities = Communities(page)
    scroll = ScrollHelper(page)
    logger.info("Started test for communities-all page")
    post_cards = page.locator(communities.COMMUNITY_POST_CARD)
    page.goto(base_url + "/import-export-communities")
    logger.info("Successfully redirected to import-export communities page")

    # Verify at least one community post is available
    first_post = communities.get_community_post_cards(0)
    expect(first_post).to_be_visible()

    logger.info("All communities posts are visible")

    # Scroll to bottom to trigger load more functionality
    scroll.scroll_to_bottom()
    # Wait for the 20 post cards to appear
    expect(post_cards).to_have_count(20)

    logger.info("Scrolled to bottom for checking load more functionality")

    # Check number of posts
    card_length = page.locator(communities.COMMUNITY_POST_CARD).count()

    assert card_length == 20, (
        f"Scroll in communities all post is not working. GET {card_length}"
    )

    logger.info(
        f"Checking if 20 posts count available after load more. GET {card_length}"
    )


def test_communities_posts(page, base_url):
    communities = Communities(page)

    logger.info("Started test for communities posts in each communities")

    page.goto(base_url + "/import-export-communities")
    # expect(page).to_have_url(base_url + "/import-export-communities")

    logger.info("Successfully redirected to the import-export communities")

    community_count = page.locator(communities.COMMUNITY_LISTS).count()

    logger.info(f"Total communities available: {community_count}")

    for i in range(min(10, community_count)):
        communities.navigate_to_communities_and_test_posts(i)

        logger.info(f"Redirected to the community post no {i + 1}")

        # Verify at least one post exists
        first_post = communities.get_community_post_cards(0)

        expect(
            first_post
        ).to_be_visible(
            timeout=30000
        )

        logger.info(
            f"Community post card is visible in community post no {i + 1}"
        )


def test_communities_post_time(page, base_url):
    communities = Communities(page)

    logger.info("Test for checking community posts posted today")

    page.goto(base_url + "/import-export-communities")

    logger.info(
        "Successfully redirected to import-export communities page"
    )

    today = datetime.now().strftime("%d %b %Y")

    logger.info(
        f"Fetching current date-time for checking today's posts. GET : {today}"
    )

    for i in range(1):
        post_time = communities.get_community_post_time(i).lower()

        is_today = (
            today.lower() in post_time
            or "today" in post_time
            or "hour" in post_time
            or "minute" in post_time
            or "second" in post_time
        )

        assert is_today, (
            f"The post {i + 1} in the feed is not posted today. "
            f"GET {post_time}"
        )

        logger.info(
            f"Tested the post no. {i + 1} if it is posted today or not. "
            f"Get {post_time}"
        )


def test_my_post(page, base_url):
    communities = Communities(page)
    login_page = LoginPage(page)

    user = get_valid_user()

    logger.info("Started the test for checking my posts page")

    communities.navigate_to_my_post(base_url)

    logger.info("Redirected to login page by clicking my post from a guest user")

    login_page.login(user["email"],user["password"])

    expect(login_page.PROFILE_DROPDOWN).to_contain_text(user["email"])
    assert f"{user['email']}" in page.content(), "Some Error Occurred : User is not able to login "