try:
    from _global import *
except:
    from ._global import *


class Port:
    def __init__(self, device, end: str, start=None, baudrate=9600, file_name='', key=None):
        self.device = device
        self.baudrate = baudrate
        self.end = end
        self.key = key
        self.start = start
        self.path = self.path(file_name)

    @staticmethod
    def list_port():
        if sys.platform == 'win32':
            for i in range(256):
                comtest = 'COM' + str(i)
                try:
                    serial.Serial(comtest)
                except:
                    pass
                else:
                    yield comtest
        else:
            raise "This function is only available on win32"

    def read(self):
        inp = ''
        pkg = ''
        while inp != self.end:
            if self.start is not None and inp == self.start:
                pkg = ''
            pkg += inp
            inp = self.device.read().decode('utf-8')
        pkg = pkg.replace('\r', '').replace('\n', '')
        return pkg

    @staticmethod
    def path(file_name):
        if not os.path.exists('Data_log'):
            os.mkdir('Data_log')
        clock = datetime.now().time()
        index = "_".join(list((date.today().strftime("%b-%d-%Y"),
                         str(clock.hour).zfill(2), str(clock.minute).zfill(2))))
        return os.path.join(os.path.abspath(os.getcwd()),
                            'Data_log', f"{file_name}_{index}.csv")

    def reading(self):
        if self.key is not None:
            self.reading_key()
        else:
            self.reading_split()

    def reading_split(self):
        recieved = self.read().split(",")
        if len(recieved) != 0:
            with open(self.path, "at") as file:
                file.write(','.join(recieved))
            return recieved

    def reading_key(self):
        recieved = self.read().split(",")  # recieved from read
        with open(self.path, "at") as file:  # save file
            file.write(','.join(recieved))
        tolist = self.key[recieved[2]]  # map tolist to dict keys set
        if len(tolist) == len(recieved):  # check length
            dic = {tolist[i]: recieved[i] for i in range(len(tolist))}
            return dic
        else:
            raise AttributeError
