class UserRole:
    NORMAL = 'Normal'
    ADMIN = 'Admin'
    VIP = 'VIP'

    @classmethod
    def from_string(cls, value) -> str:
        if value not in [cls.NORMAL, cls.ADMIN, cls.VIP]:
            raise ValueError(
                f'None of the possible UserRole values matches the value {value}.')

        return value
