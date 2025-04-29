from dataclasses import dataclass


@dataclass
class MainPageTestData:
    expected_price = "1 item(s) - $602.00"
    currency_data = [
        ("pound_sterling", "£ currency"),
        ("dollar", "$ currency"),
        ("euro", "€ currency")
    ]
    expected_page_title = "Search - MacBook"
    expected_names = [
        "desktops", "laptops & notebooks", "components", "tablets", "software", "phones & pdas", "cameras",
        "mp3 players"
    ]
    macbook_link = "macbook"
    expected_message = "you must login or create an account to save macbook to your wish list!"
