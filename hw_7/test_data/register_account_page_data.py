from dataclasses import dataclass
from faker import Faker


fake = Faker()


@dataclass
class RegisterAccountPageTestData:
    expected_header = "register account"
    expected_title = "Account Login"
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = fake.password()
    valid_credentials = [
        (fake.first_name_male(), fake.last_name_male(), fake.email(), fake.password()),
        (fake.first_name_female(), fake.last_name_female(), fake.email(), fake.password()),
        (fake.first_name(), fake.last_name(), fake.email(), fake.password()),
    ]
    expected_page_title = "Your Account Has Been Created!"
    expected_message = "first name must be between 1 and 32 characters!"
    error_message = "warning: you must agree to the privacy policy!"
