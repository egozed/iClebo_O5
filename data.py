from socket import socket, AF_INET, SOCK_STREAM
from io import BytesIO
from struct import unpack
from time import strftime, localtime
from math import degrees
from abc import abstractmethod  # ABC


class GodOfDData(object):  # @ABC
    ip: str = "lan_is_NOT_connected"
    _sock: socket = None
    port: int = 0
    is_connect: bool = False

    def __init__(self):
        print(f"{self} is BORN!")
        # self._ip = ip

    def __del__(self):
        self.port_disconnect()
        print(f"{self} is DIE!")

    def __repr__(self) -> str:
        return f'RoboData {self.ip}:{self.port}'

    def port_connect(self):
        if not self.is_connect:
            print(f'CONNECT {self}')
            # self._ip = ip
            self._sock = socket(family=AF_INET, type=SOCK_STREAM)
            self._sock.setblocking(True)
            self._sock.connect((self.ip, self.port))
            self.is_connect = True

    def port_disconnect(self):
        if self.is_connect:
            print(f'DISCONNECT {self}')
            if self._sock:
                self._sock.close()
            self.is_connect = False

    def reconnect(self):
        print(f'RECONNECT {self}')
        self.port_disconnect()
        self.port_connect()

    def _get_one_raw_data_block_than_return_it(self) -> tuple:
        """ возвращает tuple(
    сырой_блок_данных_без_размера_и_заголовка,
    размер_блока,
    сырой_заголовок_с_сырым_размером_блока
    )
    получаемые с конкретного сетевого порта """
        raw_data_without_head_and_size: str  # bytes
        size_of_data: int
        heading: int
        raw_head: str  # bytes
        raw_size: str  # bytes
        wrong_head: bool = True

        while wrong_head:
            with self._sock.makefile(mode='b', buffering=True) as rawData:
                raw_head = rawData.read(4)
                (heading,) = unpack('1i', raw_head)
                if heading == 4004:
                    raw_size = rawData.read(16)
                    (size_of_data,) = unpack('1i12x', raw_size)
                    raw_data_without_head_and_size = rawData.read(size_of_data)
                    wrong_head = False
                    # rawData.close()
                    break
                else:
                    print(f'ERROR {self} head = {heading}')
                    self.reconnect()
                    wrong_head = True
                    continue
        return raw_data_without_head_and_size, size_of_data, raw_head + raw_size

    @abstractmethod
    def get_info(self) -> dict:
        pass

    # только для работы как с модулем(как дампер)
    def _save_dump(self, full_file_name: str):
        with open(full_file_name, 'wb') as raw_file_obj:
            raw_file_obj.write(self._get_one_raw_data_block_than_return_it()[0])

    def _save_stream(self, raw_file_obj):
        (
            raw_data_without_head_and_size,
            size_of_data,
            raw_head_plus_raw_size
        ) = self._get_one_raw_data_block_than_return_it()
        raw_file_obj.write(raw_head_plus_raw_size + raw_data_without_head_and_size)

    def start_dump_saving(self):
        global flag_of_ending
        name: str = f'{self.port}/{self.port}'
        file_cnt: int = 0
        while not (flag_of_ending or is_pressed('esc')):
            file_cnt += 1
            full_file_name: str = f'{name}-{file_cnt}.bin'
            self._save_dump(full_file_name)
        print(f"{self.port} Finish!")
        flag_of_ending = True

    def start_stream_saving(self):
        global flag_of_ending
        name: str = f'{self.port}/{self.port}'
        full_file_name: str = f'{name}REC.bin'
        with open(full_file_name, 'ab') as raw_file_obj:
            while not (flag_of_ending or is_pressed('esc')):
                self._save_stream(raw_file_obj)
        print(f"{self.port} Finish!")
        flag_of_ending = True


class DataFrom30001(GodOfDData):
    port: int = 30001

    def get_info(self) -> dict:
        alldata: dict = {}
        sizeOfJPG: int

        raw_data, size_raw_data, raw_head_size = self._get_one_raw_data_block_than_return_it()
        with BytesIO(raw_data) as rawData:
            # print(f"full size = {rawData.getbuffer().nbytes}")
            (
                howMuchDataBlocks,  # 1 int
                fo,  # float
                optX,  # float
                optY,  # float
                ang,  # float
                R,  # float
                cal_dev,  # float
                scale,  # float
                srcX,  # int
                srcY,  # int
                dstX,  # int
                dstY,  # int
                camX,  # float
                camY,  # float
                sizeOfJPG  # 1 int
            ) = unpack('1i7f4i2f1i', rawData.read(4 * 15))
            alldata['sizeOfJPG'] = sizeOfJPG
            alldata['raw_jpg'] = rawData.read(sizeOfJPG)
        return alldata  # = raw_jpg, sizeOfJPG


class DataFrom30002(GodOfDData):
    port: int = 30002

    def get_info(self) -> dict:
        alldata: dict = {}
        fl1: float
        int1: int
        int2: int
        int3: int
        int4: int
        t1: str
        t2: str
        t3: str
        t4: str
        t6: str
        sizeOfText: int

        raw_data, size_raw_data, raw_head_size = self._get_one_raw_data_block_than_return_it()
        with BytesIO(raw_data) as rawData:
            # print(f"full size = {rawData.getbuffer().nbytes}")
            (
                fl1,  # float
                int1,  # int
                int2,  # int
                int3,  # int
                int4,  # int
            ) = unpack('1f4i', rawData.read(4 * 5))
            rawData.seek(-297, 2)
            (sizeOfText,) = unpack('1i', rawData.read(4))
            while sizeOfText > 252 or sizeOfText < 238:
                rawData.seek(-3, 1)
                (sizeOfText,) = unpack('1i', rawData.read(4))
                # print("FUCK!!!!")
            else:
                (Text1,) = unpack(f'{sizeOfText}s', rawData.read(sizeOfText))
                (sizeOf2Text,) = unpack('1i', rawData.read(4))
                (Text2,) = unpack(f'{sizeOf2Text}s', rawData.read(sizeOf2Text))
        alldata['fl1'] = fl1
        txt1 = Text1.decode('ascii')
        alldata['t1'], \
        alldata['t2'], \
        alldata['t3'], \
        alldata['t4'], \
        alldata['t5'] = txt1.split('\n')
        txt2 = Text2.decode('ascii')
        alldata['t6'], \
        alldata['t7'] = txt2.split('\n')
        return alldata  # = fl1, t1, t2, t3, t4, t6


class DataFrom30003(GodOfDData):
    port: int = 30003

    def get_info(self) -> dict:
        alldata: dict = {}
        sizeOfJPG: int = 0
        raw_jpg: bytes
        raw_text: bytes
        text_data: str
        how_much_datablocks_will_be: int
        type_of_data: int
        xf: float
        yf: float
        angf: float
        d1: float
        my_time: str
        f7: float
        f8: float

        raw_data, size_raw_data, raw_head_size = self._get_one_raw_data_block_than_return_it()
        with BytesIO(raw_data) as rawData:
            # size = rawData#.getbuffer().nbytes
            if size_raw_data < 300:  # rawData => text
                (raw_text,) = unpack(f'{size_raw_data - 1}s1x', rawData.read(size_raw_data))
                text_data = raw_text.decode('ascii') + '\n'
                alldata['text'] = text_data
            else:  # rawData => data + jpg
                (how_much_datablocks_will_be,) = unpack('1i', rawData.read(4))
                # CHEAT!!!
                # if how_much_datablocks_will_be > 3:
                #     rawData.seek((how_much_datablocks_will_be-2)*28, 1)
                while how_much_datablocks_will_be:
                    (type_of_data,) = unpack('1i', rawData.read(4))
                    if type_of_data == 1000:
                        (
                            xf1,  # float
                            yf1,  # float
                            angf1,  # float
                            xf2,  # float
                            yf2,  # float
                            angf2,  # float
                         ) = unpack('6f', rawData.read(24))
                        xf = (xf1 + xf2) / 2
                        yf = (yf1 + yf2) / 2
                        angf = (angf1 + angf2) / 2
                        alldata['1000'] = (xf, yf, angf)
                    elif type_of_data == 1004:
                        (
                            d1,  # double
                            f7,  # float
                            f8,  # float
                            i1,  # int
                            h1,  # short
                            h2  # short
                        ) = unpack('1d2f1i2h', rawData.read(24))  #
                        d1 /= 1000
                        my_time = strftime(f"%Y.%m.%d %H:%M:%S.{repr(d1).split('.')[1][:3]}", localtime(d1))
                        alldata['1004'] = (my_time, f7, f8)  #
                    else:
                        with open(f'WTF30003-{type_of_data}.bin', 'wb') as raw_file_obj:
                            rawData.seek(-4, 1)
                            raw_file_obj.write(rawData.read(28))
                        print('WTF!!! 30003 data have new type = ', type_of_data)
                    how_much_datablocks_will_be -= 1
                (sizeOfJPG,) = unpack('1i', rawData.read(4))
                raw_jpg = rawData.read(sizeOfJPG - 12)
                alldata['jpg'] = raw_jpg
        alldata['sizeOfJPG'] = sizeOfJPG - 12
        return alldata  # = data1000, data1004, raw_jpg


class DataFrom5556(GodOfDData):
    port: int = 5556

    def _get_one_raw_data_block_and_type_of_data_than_return_it(self) -> tuple:
        heading: int
        raw_data_without_head_and_size: str  # bytes
        type_of_data: int
        size_of_data: int
        raw_head: str  # bytes
        raw_type_plus_raw_size: str  # bytes
        wrong_head: bool = True

        while wrong_head:
            with self._sock.makefile(mode='b', buffering=True) as rawData:
                raw_head = rawData.read(4)
                (heading,) = unpack('1i', raw_head)
                if heading == -0x55aa55ab:  # a в хекс-редакторе мы видим: "55AA55AA"
                    raw_type_plus_raw_size = rawData.read(12)
                    (
                        type_of_data,  # int
                        size_of_data,  # int
                    ) = unpack('1i4x1i', raw_type_plus_raw_size)
                    raw_data_without_head_and_size = rawData.read(size_of_data)
                    wrong_head = False  #
                    break
                else:
                    print(f'ERROR {self} head = {heading}')
                    self.reconnect()
                    wrong_head = True  #
                    continue
        return raw_data_without_head_and_size, type_of_data, size_of_data, raw_head + raw_type_plus_raw_size

    def get_info(self) -> dict:
        f1: float
        f2: float
        f3: float
        f4: float
        f5: float
        i1: int
        i2: int
        i3: int
        i5: int
        charger_status: int
        bat_volt: int
        datablock_cnt: int
        alldata: dict = {}

        one_raw_data_block, type_of_data, size_of_data, raw_head_plus_raw_type_plus_raw_size = self._get_one_raw_data_block_and_type_of_data_than_return_it()
        with BytesIO(one_raw_data_block) as rawData:
            # size = rawData.getbuffer().nbytes
            alldata['type_of_data'] = type_of_data
            if type_of_data == 1:  # all GET
                (
                    f1,  # float
                    f2,  # float
                    f3,  # float
                    f4,  # float
                    f5,  # float
                ) = unpack('5f', rawData.read(20))  # f1 0.0 f3 0.0 0.0
                alldata['f1'] = f1
                alldata['f2'] = f2
                alldata['f3'] = f3
                alldata['f4'] = f4
                alldata['f5'] = f5
            elif type_of_data == 2:  # NOT ALL
                (
                    i1,  # int
                    i2,  # int
                    i3,  # int
                ) = unpack('3i', rawData.read(12))
                alldata['i1'] = i1
                alldata['i2'] = i2
                alldata['i3'] = i3 / 100
            elif type_of_data == 8:  # NOT ALL
                rawData.seek(4 * 608, 1)
                # rawblk1 = rawData.read(608)
                # rawblk2 = rawData.read(608)
                # rawblk3 = rawData.read(608)
                # rawblk4 = rawData.read(608)
                rawblk5 = rawData.read(608)
                with BytesIO(rawblk5) as raw5556Data8:  # NOT ALL
                    (
                        i1,  # int
                        f2,  # float
                        i3,  # int
                        f4,  # float
                        i5,  # int
                        charger_status,  # int
                        bat_volt,  # int
                    ) = unpack('20x1i16x1f1i4x1f3i', raw5556Data8.read(68))
                alldata['i1'] = i1
                alldata['f2'] = f2
                alldata['i3'] = i3
                alldata['f4'] = f4
                alldata['i5'] = i5
                alldata['charger_status'] = charger_status
                alldata['bat_volt'] = bat_volt
            elif type_of_data == 10:  # all GET
                (
                    f1,  # float
                    f2,  # float
                    f3,  # float
                ) = unpack('3f', rawData.read(12))
                alldata['f1'] = f1 * 1000
                alldata['f2'] = f2 * 1000
                alldata['f3'] = degrees(f3)
            elif type_of_data == 9:  # ???
                datablock_cnt = size_of_data // 20
                while datablock_cnt:
                    # rawData.seek(size_of_data - 20, 1)
                    (
                        f1,  # float
                        f2,  # float
                        f3,  # float
                        f4,  # float
                        f5,  # float
                     ) = unpack('5f', rawData.read(20))
                    datablock_cnt -= 1
                alldata['f1'] = f1
                alldata['f2'] = f2
                alldata['f3'] = f3
                alldata['f4'] = f4
                alldata['f5'] = f5
            else:
                print(f"!NEW datablock 5556! = {type_of_data}  size = {size_of_data}")
                rawData.seek(size_of_data, 1)
        return alldata

    def _save_dump(self, full_file_name: str):
        (
            raw_data_without_head_and_size,
            type_of_data,
            size_of_data,
            raw_head_plus_raw_type_plus_raw_size
        ) = self._get_one_raw_data_block_and_type_of_data_than_return_it()
        full_file_name += f'{type_of_data}.bin'
        with open(full_file_name, 'wb') as raw_file_obj:
            raw_file_obj.write(raw_data_without_head_and_size)

    def _save_stream(self, raw_file_obj):
        (
            raw_data_without_head_and_size,
            type_of_data,
            size_of_data,
            raw_head_plus_raw_type_plus_raw_size
        ) = self._get_one_raw_data_block_and_type_of_data_than_return_it()
        raw_file_obj.write(raw_head_plus_raw_type_plus_raw_size + raw_data_without_head_and_size)

    def start_dump_saving(self):
        global flag_of_ending
        name: str = f'{self.port}/{self.port}'
        file_cnt: int = 0
        while not (flag_of_ending or is_pressed('esc')):
            file_cnt += 1
            full_file_name: str = f'{name}-{file_cnt}-'
            self._save_dump(full_file_name)
        print(f"{self.port} Finish!")
        flag_of_ending = True


if __name__ == '__main__':
    # только для работы как с модулем(как дампер)
    from keyboard import is_pressed

    flag_of_ending: bool = False


    def del_and_make_dirs():
        from os import path, mkdir
        from shutil import rmtree
        from time import sleep

        for port in [5556, 30001, 30002, 30003]:
            try_delete_dirs_count: int = 100
            while path.exists(str(port)) and try_delete_dirs_count:
                rmtree(str(port), ignore_errors=False)
                sleep(0.1)
                try_delete_dirs_count -= 1
            else:
                if path.exists(str(port)):
                    print(f'Delete this directory self: "{port}"')
                    exit(3)
            mkdir(str(port))
        print("WE ARE START!")


    def init_connect_data_package():
        from iCleboIP4finder import get_ip
        global D5556, D30001, D30002, D30003

        my_ip4: str = get_ip()
        setattr(D5556, 'ip', my_ip4)
        D5556.port_connect()
        setattr(D30001, 'ip', my_ip4)
        D30001.port_connect()
        setattr(D30002, 'ip', my_ip4)
        D30002.port_connect()
        setattr(D30003, 'ip', my_ip4)
        D30003.port_connect()
        print("DATA PACKAGE FULL CONNECTED.")


    def start_threads():
        from threading import Thread
        global D5556, D30001, D30002, D30003

        if user_choose_mode == 'd':
            thread1 = Thread(target=D5556.start_dump_saving)  # , args=(user_choose,))
            thread2 = Thread(target=D30001.start_dump_saving)  # , args=(user_choose,))
            thread3 = Thread(target=D30002.start_dump_saving)  # , args=(user_choose,))
            thread4 = Thread(target=D30003.start_dump_saving)  # , args=(user_choose,))
        else:  # user_choose_func == 'r':
            thread1 = Thread(target=D5556.start_stream_saving)  # , args=(user_choose,))
            thread2 = Thread(target=D30001.start_stream_saving)  # , args=(user_choose,))
            thread3 = Thread(target=D30002.start_stream_saving)  # , args=(user_choose,))
            thread4 = Thread(target=D30003.start_stream_saving)  # , args=(user_choose,))
        #   стартуем все потоки одновременно
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        #   дождаться завершения всех потоков
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()


    def start_making_and_saving_dumps():
        del_and_make_dirs()
        init_connect_data_package()
        start_threads()


    print('DUMPS MODE(for research): For make separate files dumps, input "d"')
    print('RECORD MODE(for logging): For make 1 BIG dumpfile, input "r"')
    print('Push "Esc" key for EXIT!')
    user_choose_mode: str = input('d/r: ')
    if user_choose_mode == 'd' or user_choose_mode == 'r':
        # init_data_package
        D5556 = DataFrom5556()
        D30001 = DataFrom30001()
        D30002 = DataFrom30002()
        D30003 = DataFrom30003()
        start_making_and_saving_dumps()
        # kill_data_package
        if D5556:
            del D5556
        if D30001:
            del D30001
        if D30002:
            del D30002
        if D30003:
            del D30003

    print('The End.')
    exit(0)
