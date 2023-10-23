import pytest
from pytest_factoryboy import register
from tests.factories import UserFactory, ProductFactory, CategoryFactory
from selenium import webdriver


register(UserFactory)  # u gonna access it by -> user_factory
register(ProductFactory)
register(CategoryFactory)


@pytest.fixture
def new_user1(db, user_factory):
    user = user_factory.create()
    return user


@pytest.fixture(scope="class")
def chrome_driver_init(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Chrome(options=options)
    if request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Firefox(options=options)
    request.cls.driver = web_driver
    yield
    web_driver.close


# No Factory boy
# @pytest.fixture  # (scope='session')
# def user_1(db):
#     user = User.objects.create_user("test-user")
#     print("create-user")
#     return user


# @pytest.fixture
# def new_user_factory():
#     def create_app_user(username: str, password: str = None, first_name: str = 'firstname',
#                         last_name: str = 'lastname', emai: str = "test@test.com",
#                         is_staff: str = False, is_superuser: str = False, is_active: str = True):

#         user = User.objects.create_user(username=username, password=password, first_name=first_name,
#                                         last_name=last_name, email=emai, is_staff=is_staff,
#                                         is_active=is_active, is_superuser=is_superuser)
#         return user

#     return create_app_user


# @pytest.fixture
# def new_user1(db, new_user_factory):
#     return new_user_factory("Test_user", "password", "My Name")


# @pytest.fixture
# def new_user2(db, new_user_factory):
#     return new_user_factory("Test_user", "password", "My Name", is_staff="True")
