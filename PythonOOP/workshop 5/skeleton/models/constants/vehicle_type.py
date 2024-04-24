class VehicleType:
    MOTORCYCLE = 'Motorcycle'
    CAR = 'Car'
    TRUCK = 'Truck'

    @classmethod
    def from_string(cls, value) -> str:
        if value not in [cls.MOTORCYCLE, cls.CAR, cls.TRUCK]:
            raise ValueError(
                f'None of the possible VehicleType values matches the value {value}.')

        return value
