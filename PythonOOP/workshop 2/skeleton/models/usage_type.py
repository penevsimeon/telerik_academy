class UsageType:
    EVERY_DAY = 'Every_Day'
    MEDICAL = 'Medical'

    @classmethod
    def from_string(cls, usage_type_string):
        if usage_type_string not in [cls.MEDICAL, cls.EVERY_DAY]:
            raise ValueError(
                f'None of the possible UsageType values matches the value {usage_type_string}.')

        return usage_type_string
