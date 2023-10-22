import pytest
from django.contrib.auth.models import User


@pytest.fixture  # (scope='session')
def user_1(db):
    user = User.objects.create_user("test-user")
    print("create-user")
    return user


@pytest.fixture
def new_user_factory():
    def create_app_user(username: str, password: str = None, first_name: str = 'firstname',
                        last_name: str = 'lastname', emai: str = "test@test.com",
                        is_staff: str = False, is_superuser: str = False, is_active: str = True):

        user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                        last_name=last_name, email=emai, is_staff=is_staff,
                                        is_active=is_active, is_superuser=is_superuser)
        return user

    return create_app_user


@pytest.fixture
def new_user1(db, new_user_factory):
    return new_user_factory("Test_user", "password", "My Name")


@pytest.fixture
def new_user2(db, new_user_factory):
    return new_user_factory("Test_user", "password", "My Name", is_staff="True")
