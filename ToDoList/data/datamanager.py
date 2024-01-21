import json


class ManageData:
    def __init__(self):
        self.data = self.__read_file()

    def __read_file(self) -> dict:
        with open("data.json", "r+") as  f:
            try:
                return json.loads(f.read())
            except Exception as E:
                return E

    def __write_file(self, data):
        with open("data.json", "w+") as f:
            json.dump(data, f, indent=4)

    def save(self, data):
        self.__write_file(data)

    def delete_task(self, data):
        self.__write_file(data)



