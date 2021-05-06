import json
import discord
class db():
  def __init__(self):
    try:
      with open("users.db", "r") as file:
        self._user_database = json.loads(file.read())
    except:
      with open("users.db", "x") as file:
        file.write(json.dumps({"":""}))
  def db_load(self):
    with open("users.db") as file:
      self._user_database = json.loads(file.read())
  def db_write(self, data):
    try:
      with open("users.db", "w") as file:
        file.write(json.dumps(data))
    except OSError:
      print(f"OSError encountered in db_write with data: {data}")
    except BaseException as error:
      print(f"error: {error}")

  def add_money(self, user_id, money: int):
    self.db_load()
    user_id = format(user_id, "d")
    self._user_database[str(user_id)]["money"] += money

    self.db_write(self._user_database)
  def remove_money(self, user_id, money: int):
    self.db_load()
    user_id = format(user_id, "d")
    self._user_database[str(user_id)]["money"] -= money
    self.db_write(self._user_database)


  def reset_money(self, user_id):
    self.db_load()
    user_id = format(user_id, "d")
    self._user_database[str(user_id)]["money"] = 1000
    self.db_write(self._user_database)


  def get_money(self, user_id) -> int:
    self.db_load()
    user_id = format(user_id, "d")
    try:
      result = self._user_database[str(user_id)]["money"] 
      return result
    except:
      return "err"
  def reg_user(self, user_id):
    self.db_load()
    try:
      self._user_database[str(user_id)] = {"money":1000}
      self.db_write(self._user_database)
    except BaseException as error:
      print(f"error in reg_user: {error}")
  def get_user(self, user_id):
    return self._user_database[str(user_id)]