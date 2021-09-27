try:
    from _global import *
except:
    from ._global import *


class RTC:
    def __init__(self):
        self.start_time = time.time()

    @staticmethod
    def time_format(time):
        time_list = [str(time.hour).zfill(2), str(time.minute).zfill(
            2), str(time.second).zfill(2), str(time.microsecond)[0:3]]
        timen = ' '.join(
            time_list) if time.second % 2 == 0 else ':'.join(time_list)
        return timen

    @staticmethod
    def time_pc():
        time = datetime.now().time()
        return RTC.time_format(time)

    @staticmethod
    def time_UTC():
        time = datetime.utcnow().time()
        return RTC.time_format(time)

    def time_elapsed(self):
        delta = time.time() - self.start_time
        second = round(delta % 60)
        microsecond = str(datetime.now().time().microsecond)[:2]
        minute = delta // 60
        minute = minute % 60
        hour = minute // 60
        time_list = [str(round(hour)), str(round(minute)),
                     str(round(second)), microsecond]
        timestp = ' '.join(
            time_list) if second % 2 == 0 else ':'.join(time_list)
        return timestp


if __name__ == '__main__':
    clock = RTC()
    while True:
        print(f'elspsed {clock.time_elapsed()}')
        print(f'pc {clock.time_pc()}')
        time.sleep(0.01)
