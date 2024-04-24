from models.comment import Comment
from models.constants.user_role import UserRole
from models.constants.vehicle_type import VehicleType
from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck


class User:
    USERNAME_LEN_MIN = 2
    USERNAME_LEN_MAX = 20
    USERNAME_LEN_ERR = f'Username must be between {USERNAME_LEN_MIN} and {USERNAME_LEN_MAX} characters long!'
    USERNAME_INVALID_SYMBOLS = 'Username contains invalid symbols!'

    PASSWORD_LEN_MIN = 5
    PASSWORD_LEN_MAX = 30
    PASSWORD_LEN_ERR = f'Password must be between {PASSWORD_LEN_MIN} and {PASSWORD_LEN_MAX} characters long!'
    PASSWORD_INVALID_SYMBOLS = 'Password contains invalid symbols!'

    LASTNAME_LEN_MIN = 2
    LASTNAME_LEN_MAX = 20
    LASTNAME_LEN_ERR = f'Lastname must be between {LASTNAME_LEN_MIN} and {LASTNAME_LEN_MAX} characters long!'

    FIRSTNAME_LEN_MIN = 2
    FIRSTNAME_LEN_MAX = 20
    FIRSTNAME_LEN_ERR = f'Firstname must be between {FIRSTNAME_LEN_MIN} and {FIRSTNAME_LEN_MAX} characters long!'

    NORMAL_ROLE_VEHICLE_LIMIT = 5

    NORMAL_USER_LIMIT_REACHED_ERR = f'You are not VIP and cannot add more than {NORMAL_ROLE_VEHICLE_LIMIT} vehicles!'
    ADMIN_CANNOT_ADD_VEHICLES_ERR = 'You are an admin and therefore cannot add vehicles!'
    YOU_ARE_NOT_THE_AUTHOR = 'You are not the author of the comment you are trying to remove!'
    THE_VEHICLE_DOES_NOT_EXIT = 'The vehicle does not exist!'

    def __init__(self, username, firstname, lastname, password, user_role=UserRole.NORMAL):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self._is_admin = False
        self.user_role = user_role
        self._vehicles = []

    @property
    def is_admin(self):
        return self._is_admin

    @property
    def vehicles(self):
        return tuple(self._vehicles)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if len(value) < int(User.USERNAME_LEN_MIN) or len(value) > int(User.USERNAME_LEN_MAX):
            raise ValueError(f'{User.USERNAME_LEN_ERR}')

        allowed_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        for character in value:
            if character not in allowed_characters:
                raise ValueError(f'{User.USERNAME_INVALID_SYMBOLS}')
        self._username = value

    @property
    def firstname(self):
        return self._first_name

    @firstname.setter
    def firstname(self, value):
        if len(value) < int(User.FIRSTNAME_LEN_MIN) or len(value) > int(User.FIRSTNAME_LEN_MAX):
            raise ValueError(f'{User.FIRSTNAME_LEN_ERR}')
        self._first_name = value

    @property
    def lastname(self):
        return self._last_name

    @lastname.setter
    def lastname(self, value):
        if len(value) < int(User.LASTNAME_LEN_MIN) or len(value) > int(User.LASTNAME_LEN_MAX):
            raise ValueError(f'{User.LASTNAME_LEN_ERR}')
        self._last_name = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) < int(User.PASSWORD_LEN_MIN) or len(value) > int(User.PASSWORD_LEN_MAX):
            raise ValueError(f'{User.PASSWORD_LEN_ERR}')

        allowed_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@*-_"

        for character in value:
            if character not in allowed_characters:
                raise ValueError(f'{User.PASSWORD_INVALID_SYMBOLS}')

        self._password = value

    @property
    def user_role(self):
        return self._user_role

    @user_role.setter
    def user_role(self, value):
        role = UserRole.from_string(value)
        if role == UserRole.ADMIN:
            self._is_admin = True
        else:
            self._is_admin = False
        self._user_role = role

    def add_vehicle(self, vehicle):
        if self._is_admin:
            raise ValueError('You are an admin and therefore cannot add vehicles!')
        if self.user_role == UserRole.NORMAL:
            if len(self._vehicles) >= 5:
                raise ValueError('You are not VIP and cannot add more than 5 vehicles!')
        self._vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        if vehicle in self._vehicles:
            self._vehicles.remove(vehicle)

    def get_vehicle(self, index):
        if index < 0 or index >= len(self._vehicles):
            raise ValueError('There is no comment on this index.')
        return self._vehicles[index]

    def add_comment(self, comment: Comment, vehicle):
        new_comment = Comment(comment, self.username)
        vehicle.add_comment(new_comment)

    def remove_comment(self, comment: Comment, vehicle):
        if comment.author != self.username:
            raise ValueError('You are not the author of the comment you are trying to remove!')

        vehicle.remove_comment(comment)

    def print_vehicles(self):
        lines = [f'--USER {self.username}--']
        if len(self._vehicles) == 0:
            lines.append('--NO VEHICLES--')
        else:
            vehicle_index = 1
            for vehicle in self._vehicles:
                lines.append(f'{vehicle_index}. {vehicle}')
                vehicle_index += 1
        return '\n'.join(lines)

    def __str__(self):
        return f'Username: {self.username}, FullName: {self.firstname} {self.lastname}, Role: {self.user_role}'
