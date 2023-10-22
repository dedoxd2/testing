import pytest


# @pytest.fixture() # arrange data  , arrange phase
# def user_1(db):
#     return User.objects.create_user("test-user")


# @pytest.mark.django_db
# def test_set_check_password(user_1):
#     user_1.set_password("new-password") # act phase
#     assert user_1.check_password("new-passwords") is True # assert


# @pytest.mark.django_db
# def test_set_check_password1(user_1):
#     print('check-user1')
#     assert user_1.username == "test-user"


# def test_set_check_password2(user_1):
#     print('check-user2')
#     assert user_1.username == "test-user"


def test_new_user(new_user1):
    print(new_user1)
    assert new_user1.first_name == "My Name"


def test_new_user2(new_user2):
    print(new_user2.is_staff)
    assert new_user2.is_staff  # == True X  # "True"
