from models.user import User


class ApplicationData:
    def __init__(self):
        self._users = []
        self._logged_user = None

    @property
    def users(self):
        return tuple(self._users)

    def create_user(self, username, firstname, lastname, password, user_role) -> User:
        if len([u for u in self._users if u.username == username]) > 0:
            raise ValueError(
                f'User {username} already exist. Choose a different username!')

        user = User(username, firstname, lastname, password, user_role)
        self._users.append(user)

        return user

    def find_user_by_username(self, username: str) -> User:
        filtered = [user for user in self._users if user.username == username]
        if filtered == []:
            raise ValueError(f'There is no user with username {username}!')

        return filtered[0]

    @property
    def logged_in_user(self):
        if self.has_logged_in_user:
            return self._logged_user
        else:
            raise ValueError('There is no logged in user.')

    @property
    def has_logged_in_user(self):
        return self._logged_user is not None

    def login(self, user: User):
        self._logged_user = user

    def logout(self):
        self._logged_user = None

    def show_users(self):
        lines = ['--USERS--']
        user_index = 1
        for user in self._users:
            lines.append(f'{user_index}. {user}')
            user_index += 1
        return '\n'.join(lines)
