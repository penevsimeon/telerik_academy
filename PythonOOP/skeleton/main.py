from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine

app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start()

# from show_users_test.py one test failed, I don't know why,
# when I import the sample input in the console, I receive the expected output 1:1
