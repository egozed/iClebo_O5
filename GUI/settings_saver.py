class SettingsSaver(object):
    filename: str = ''

    def __init__(self, any_filename: str):
        self.filename = any_filename

    def __repr__(self) -> str:
        return f'Save the settings to {self.filename}'

    # -------- pickle ----------------------------------- #
    def get_from_pkl_data(self):
        from pickle import load
        with open(self.filename, 'rb') as fromFile:
            data_loaded = load(fromFile)
        return data_loaded

    def save_data_to_pkl(self, data):
        from pickle import dump
        with open(self.filename, 'wb') as toFile:
            dump(data, toFile, protocol=5)

    def add_data_to_pkl(self, newdata):
        data = self.get_from_pkl_data()

        if isinstance(data, dict):
            data.update(newdata)
        if isinstance(data, list):
            data.append(newdata)
        if isinstance(data, tuple):
            data = *data, newdata

        if data == self.get_from_pkl_data():
            pass
            # print("no changes-no saves")
        else:
            print(self, " Changes: ", newdata)
            self.save_data_to_pkl(data)

    # -------- pickle end -------------------------------- #

    # -------- json -------------------------------------- #
    def get_from_json_data(self):
        from json import load
        from codecs import open
        with open(self.filename, 'r', encoding='utf-8') as fromFile:
            data_loaded = load(fromFile)
        return data_loaded

    def save_data_to_json(self, data):
        from json import dump
        from codecs import open
        with open(self.filename, mode='w', encoding='utf-8') as toFile:
            dump(data, toFile, indent=4)

    def add_data_to_json(self, newdata):
        from json import dumps
        data = self.get_from_json_data()

        if isinstance(data, dict):
            data.update(newdata)
        if isinstance(data, list):
            data.append(newdata)
        # if isinstance(data, tuple):     # json - NOT saves the tuple!
        #     data = *data, newdata

        if dumps(data) == dumps(self.get_from_json_data()):
            pass
            # print("no changes-no saves")
        else:
            print(self, " Changes: ", newdata)
            self.save_data_to_json(data)


# -------- json end ---------------------------------- #


if __name__ == '__main__':
    # только для работы как с модулем(как test-data-дампер)
    data = {
        'ip': '192.168.0.4',
        'winMAINcoord': (320, 240, 640, 480),
        'win5556coord': (320, 240, 640, 480),
        'win30001coord': (320, 240, 640, 480),
        'win30002coord': (320, 240, 640, 480),
        'win30003coord': (320, 240, 640, 480)
    }
    filename = 'mytest-settings.bin'
    ini = SettingsSaver(filename)
    ini.save_data_to_pkl(data)
    ini.add_data_to_pkl({'785': 0.32})
    data_loaded = ini.get_from_pkl_data()
    print(data_loaded)
    del ini

    filename = 'test-settings.json'
    ini = SettingsSaver(filename)
    ini.save_data_to_json(data)
    ini.add_data_to_json({'78': 0.32})
    data_loaded = ini.get_from_json_data()
    print(data_loaded)
    del ini

    exit(0)
