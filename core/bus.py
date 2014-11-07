# -*- coding: utf-8 -*-

from pyquery import PyQuery
import static


class Bus:
    url = None
    bus_page = None
    station_page = None

    def __init__(self, number):
        self.url = static.BUS_URL.format(str(number))

    def query(self):
        self.bus_page = PyQuery(self.url, headers=static.UA_HEADER)
        # print(self.bus_page)
        deli = ['.headinfo', '.leftspan01', '.rightspan01', '.leftspan02']
        [bus_number, bus_start_station, bus_end_station, bus_time] = map(self.map_bus, deli)
        bus_number = bus_number.split(' ')[1]
        bus_start_time, bus_stop_time = bus_time.split('~')
        print bus_number, bus_start_station, bus_end_station, bus_start_time, bus_stop_time

        station_list = self.bus_page('.buslineinfo > ul')
        for station in station_list:
            self.station_page = PyQuery(station)
            deli = ['.li_01', '.yuanicon', 'p']
            [station, station_number, station_gps] = map(self.map_station, deli)
            print station, station_number, station_gps

    def map_bus(self, delimiter):
        return self.bus_page(delimiter).text()

    def map_station(self, delimiter):
        return self.station_page(delimiter).text()

if __name__ == '__main__':
    bus = Bus(1)
    bus.query()