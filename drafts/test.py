from structs import *

user_hashmap = UserHashMap(100)

user_hashmap.add_user("1234")
user_hashmap.add_user("5678")

user = user_hashmap.get_user("1234")

user.command_history.add("!help")
user.command_history.add("!ping")
user.command_history.add("!pong")

all_commands = user.command_history.get_all()
print(all_commands)

current_command = user.command_history.current()
print(current_command)
current_command = user.command_history.move_backward()
print(current_command)
current_command = user.command_history.move_backward()
print(current_command)
current_command = user.command_history.move_backward()
print(current_command)
current_command = user.command_history.move_forward()
print(current_command)

user.command_history.save_to_file(f"history_{user.id}.json");
user.command_history.load_from_file(f"history_{user.id}.json")

all_commands = user.command_history.get_all()
print(all_commands)