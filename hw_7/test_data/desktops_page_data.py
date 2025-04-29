from dataclasses import dataclass


@dataclass
class DesktopsPageTestData:
    expected_title = "Desktops"
    expected_breadcrumb_name = "desktops"
    expected_link_names = [
        'desktops (13)', '- pc (0)', '- mac (1)', 'laptops & notebooks (5)', 'components (2)', 'tablets (1)',
        'software (0)', 'phones & pdas (3)', 'cameras (2)', 'mp3 players (4)'
    ]
    expected_product_name = "imac"
