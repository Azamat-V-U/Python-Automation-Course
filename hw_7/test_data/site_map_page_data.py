from dataclasses import dataclass


@dataclass
class SiteMapTestData:
    sitemap_page_header = "site map"
    base_links = [
        "desktops", "laptops & notebooks", "components", "tablets",
        "software", "phones & pdas", "cameras", "mp3 players",
        "special offers", "my account", "shopping cart", "checkout", "search"
    ]
    my_account_links = [
        "account information", "password", "address book", "order history", "downloads"
    ]
    information_links = [
        "terms & conditions", "delivery information", "about us", "privacy policy", "contact us"
    ]
