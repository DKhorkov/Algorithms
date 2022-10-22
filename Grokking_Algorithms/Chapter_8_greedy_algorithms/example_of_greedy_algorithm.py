"""Найти минимальное количество радиостанций, чтобы охватить все страны СНГ"""


class Greedy:

    def __init__(self):
        self.countries = {'Russia', 'Ukraine', 'Armenia', 'Azerbaijan', 'Belarus',
                          'Kazakhstan', 'Kyrgyzstan', 'Moldova', 'Tajikistan', 'Uzbekistan'}
        self.radio_stations = {1: {'Russia', 'Kyrgyzstan', 'Armenia', 'Belarus', 'Moldova'},
                               2: {'Azerbaijan', 'Moldova', 'Kazakhstan', 'Belarus'},
                               3: {'Tajikistan', 'Kyrgyzstan', 'Kazakhstan', 'Uzbekistan', 'Ukraine', 'Moldova'},
                               4: {'Belarus', 'Kyrgyzstan', 'Moldova', 'Tajikistan'},
                               5: {'Azerbaijan', 'Ukraine', 'Armenia'}}
        self.chosen_stations = set()

    def check_best_station(self):
        countries_covered = set()
        best_station = None
        for station, countries in self.radio_stations.items():
            covered_countries = self.countries & countries
            if len(covered_countries) > len(countries_covered):
                countries_covered = covered_countries
                best_station = station
        return best_station

    def main(self):
        while len(self.countries) > 0:
            radio = self.radio_stations[self.check_best_station()]
            self.chosen_stations.add(self.check_best_station())
            self.radio_stations.pop(self.check_best_station())
            for country in radio:
                if country in self.countries:
                    self.countries.remove(country)
        print(f'Чтобы охватить все страны СНГ, были выбраны радиостанции номер '
              f'{[station for station in self.chosen_stations]}!')


if __name__ == '__main__':
    alr = Greedy()
    alr.main()
