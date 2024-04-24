from commands.add_to_category import AddToCategoryCommand
from commands.add_to_shopping_cart import AddToShoppingCartCommand
from commands.create_category import CreateCategoryCommand
from commands.create_product import CreateProductCommand
from commands.remove_from_category import RemoveFromCategoryCommand
from commands.remove_from_shopping_cart import RemoveFromShoppingCartCommand
from commands.show_category import ShowCategoryCommand
from commands.total_price import TotalPriceCommand


class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "createcategory":
            return CreateCategoryCommand(params, self._app_data)
        if cmd.lower() == "createproduct":
            return CreateProductCommand(params, self._app_data)
        if cmd.lower() == "showcategory":
            return ShowCategoryCommand(params, self._app_data)
        if cmd.lower() == "addtocategory":
            return AddToCategoryCommand(params, self._app_data)
        if cmd.lower() == "removefromcategory":
            return RemoveFromCategoryCommand(params, self._app_data)
        if cmd.lower() == "addtoshoppingcart":
            return AddToShoppingCartCommand(params, self._app_data)
        if cmd.lower() == "removefromshoppingcart":
            return RemoveFromShoppingCartCommand(params, self._app_data)
        if cmd.lower() == "totalprice":
            return TotalPriceCommand(self._app_data)

        raise ValueError(f'Invalid command name: {cmd}!')
