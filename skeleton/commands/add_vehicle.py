from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from models.car import Car
from models.motorcycle import Motorcycle
from models.constants.vehicle_type import VehicleType
from models.truck import Truck


class AddVehicleCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)

        logged_user = self._app_data.logged_in_user
        vehicle = self._create_vehicle(params)
        logged_user.add_vehicle(vehicle)

        return f'{logged_user.username} added vehicle successfully!'

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 5

    def _create_vehicle(self, params) -> VehicleType:
        type, make, model, price, *rest = params
        price = self._try_parse_float(
            price, 'Invalid value for price. Should be a number.')
        type = VehicleType.from_string(type)

        if type == VehicleType.CAR:
            seats = self._try_parse_int(
                rest[0], 'Invalid seats. Expected a number.')
            return Car(make, model, price, seats)

        if type == VehicleType.MOTORCYCLE:
            category = rest[0]
            return Motorcycle(make, model, price, category)

        if type == VehicleType.TRUCK:
            weight_capacity = self._try_parse_int(
                rest[0], 'Invalid weight capacity. Expected a number.')
            return Truck(make, model, price, weight_capacity)

        raise ValueError('Cannot create this type of vehicle.')
