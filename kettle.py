import KETTLE_CONF as CONF

import threading
import time as cl_time


class ElectricKettle:
    def __init__(self):
        self.water_level = 0
        self.on = False
        self.temperature = 0
        self.status = "Чайник выключен"

    def fill(self, water_level):
        """
        Метод, в ктором задаётся количество воды. В качестве параметра передаётся количество воды.
        :param water_level: float
        :return:
        """
        if water_level < 0:
            self.water_level = 0
        elif water_level > CONF.WATER_LEVEL:
            self.water_level = 0
        else:
            self.water_level = water_level

    def switch_on(self):
        """
        Метод для запуска чайника
        :return:
        """
        if not self.on:
            self.on = True
            self.status = "Чайник включен"
            self._start_boiling()

    def switch_off(self):
        """
        Метод для выключения чайника
        :return:
        """
        if self.on:
            self.on = False

    def _start_boiling(self):
        """
        Метод для запуска процесса кипячения воды
        :return:
        """

        def _boil():
            time = 0
            while time < CONF.TIME_BOILING and self.on and self.temperature <= CONF.TEMPERATURE:
                time += 1
                self.temperature = time * 10
                cl_time.sleep(1)

            if time < CONF.TIME_BOILING:
                self.on = False
                self.temperature = 0
                self.status = "Остановлен"
            else:
                self.on = False
                self.temperature = 0
                self.status = "Вскипел"

        t = threading.Thread(target=_boil)
        t.start()

    def get_status(self):
        if self.on:
            return
        else:
            return
