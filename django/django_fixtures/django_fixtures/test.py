import pytest
from django.contrib.auth.models import User, Group, Permission





# def create_app_user(
#     username: str,
#     password: Optional[str] = None,
#     first_name: Optional[str] = "first name",
#     last_name: Optional[str] = "last name",
#     email: Optional[str] = "foo@bar.com",
#     is_staff: str = False,
#     is_superuser: str = False,
#     is_active: str = True,
#     groups: List[Group] = [],
# ) -> User:
#     user = User.objects.create_user(
#         username=username,
#         password=password,
#         first_name=first_name,
#         last_name=last_name,
#         email=email,
#         is_staff=is_staff,
#         is_superuser=is_superuser,
#         is_active=is_active,
#     )
#     user.groups.add(*groups)
#     return user






# @pytest.fixture
# def app_user_group(db) -> Group:
#     group = Group.objects.create(name="app_user")
#     change_user_permissions = Permission.objects.filter(
#         codename__in=["change_user", "view_user"],
#     )
#     group.permissions.add(*change_user_permissions)
#     return group

# @pytest.fixture
# def user_A(db, app_user_group: Group) -> User:
#     user = User.objects.create_user("A")
#     user.groups.add(app_user_group)
#     return user

@pytest.fixture
def user_B(db, app_user_group: Group) -> User:
    user = User.objects.create_user("B")
    user.groups.add(app_user_group)
    return user

def test_should_create_two_users(user_A: User, user_B: User) -> None:
    assert user_A.pk != user_B.pk




# @pytest.fixture
# def user_A(db) -> User:
#     group = Group.objects.create(name="app_user")
#     change_user_permissions = Permission.objects.filter(codename__in=["change_user", "view_user"],
#     )
#     group.permissions.add(*change_user_permissions)
#     user = User.objects.create_user("A")
#     user.groups.add(group)
#     return user

# @pytest.fixture
# def user_B(db) -> User:
#     group = Group.objects.create(name="app_user")
#     change_user_permissions = Permission.objects.filter(codename__in=["change_user", "view_user"],
#     )
#     group.permissions.add(*change_user_permissions)
#     user = User.objects.create_user("A")
#     user.groups.add(group)
#     return user

# def test_should_create_two_users(user_A: User, user_B: User) -> None:
#     assert user_A.pk != user_B.pk
#This will cause integrity error as we are making two "app_user" group.


# @pytest.fixture
# def user_A(db) -> Group:
#     group = Group.objects.create(name="app_user")
#     change_user_permissions = Permission.objects.filter(
#         codename__in=["change_user", "view_user"],
#     )
#     group.permissions.add(*change_user_permissions)
#     user = User.objects.create_user("A")
#     user.groups.add(group)
#     return user

# def test_should_create_user(user_A: User) -> None:
#     assert user_A.username == "A"

# def test_user_is_in_app_user_group(user_A: User) -> None:
#     assert user_A.groups.filter(name="app_user").exists()




# @pytest.fixture
# def user_A(db) -> User:
#     return User.objects.create_user("A")

# def test_should_check_password(db, user_A:User) -> None:
#     user_A.set_password("secret")
#     assert user_A.check_password("secret") is True

# def test_should_not_check_unusable_password(db, user_A:User) -> None:
#     user_A.set_password("secret")
#     user_A.set_unusable_password()
#     assert user_A.check_password("secret") is False



# def test_should_create_user_with_username(db) -> None:
#     user = User.objects.create_user("Haki")
#     assert user.username == "Haki"

# def test_should_check_password(db) -> None:
#     user = User.objects.create_user("A")
#     user.set_password("secret")
#     assert user.check_password("secret") is True

# def test_should_not_check_unusable_password(db) -> None:
#     user = User.objects.create_user("A")
#     user.set_password("secret")
#     user.set_unusable_password()
#     assert user.check_password("secret") is False



