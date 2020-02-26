# Ant on rubber rope paradox
# How can ant reach end of the rope, if the rope is extending
# "Increasing the distance by more than his progress"
# Inspired by Vsauce2
# Made by mvaario

import time
import math


def final_times():
    time = game.time
    if time > 2592000:
        kk = time / 2592000
        day = round((kk - math.floor(kk)) * 24)
        kk = math.floor(kk)
        print("Time", kk, "kk", day, "day")
    elif time > 86400:
        day = time / 86400
        h = round((day - math.floor(day)) * 24)
        day = math.floor(day)
        print("Time", day, "day", h, "hours")
    elif time > 3600:
        h = time / 3600
        min = round((h - math.floor(h)) * 60)
        h = math.floor(h)
        print("Time",h, "hours", min, "min" )
    elif time > 60:
        min = time / 60
        sec = round((min - math.floor(min)) * 60)
        min = math.floor(min)
        print("Time", min, "min", sec, "sec")
    else:

        print("Time", round(time,3), "sec")

def final():
    print("")
    print("Done, final data")
    print("---------------")
    print("Ant final position", round(game.ant, 2), " m")
    print("Rope final length", round(game.rope, 2), " m")
    print("Ant moved ", round(game.ant_speed * game.time), "m")

    final_times()

    return


class settings:
    def __init__(self):
        #  Accurate, 1, 10, 100, aka 1/acc sec accurate
        self.acc = 10000000

        # Ant's starting position in meters
        self.ant = 0

        # Rope's starting length in meters
        self.rope = 10

        # ant's moving speed m/s      - light speed = 300 000 km/s
        self.ant_speed = 1

        # Rope's extending speed m/s  - universe expanding speed = 73 km/s
        self.rope_speed = 1

        # Rope's acceleration m/s^2
        self.rope_acceleration = 0

        # ant process in %
        self.ant_pro = 0

        # times
        self.time = 0

        # printing secs
        self.print = 1
        self.i = 0
        return

    def start():
        # ant position in meters
        game.ant = game.ant + game.ant_speed / game.acc

        # rope new length
        settings.rub_leinght()

        return

    def rub_leinght():

        # and process
        game.ant_process()
        # rope new length
        game.rope = game.rope + game.rope_speed / game.acc

        # new ant position
        if game.ant_pro != 0:
            game.ant = (game.rope * game.ant_pro / 100)

        return

    def ant_process(self):
        # ant process
        game.ant_pro = 100 / game.rope * game.ant

        return

    # Times
    def print():
        i = round(game.time)
        time = round(game.time)

        if game.i != time:
            if i < 86400 and game.print == 1:
                if i < 10:
                    print(time, "sec -", round(game.ant_pro, 2), "%")
                if i % 10 == 0 and i < 60:
                    print(time, "sec -", round(game.ant_pro, 2), "%")

                if i % 60 == 0 and i < 600:
                    print(round(time / 60), "min -", round(game.ant_pro, 2), "%")
                elif i % 600 == 0 and i < 3600:
                    print(round(time / 60), "min -", round(game.ant_pro, 2), "%")

                i = i / 60
                if i % 60 == 0 and i < 600:
                    print(round(time / 3600), "h -", round(game.ant_pro, 2), "%")
                elif i % 600 == 0 and i < 1440:
                    print(round(time / 3600), "h -", round(game.ant_pro, 2), "%")

            else:
                i = i / 60
                if i > 1440:
                    i = i / 1440
                    settings.print_days(i)
        game.i = time

        return

    def print_days(i):
        if i % 1 == 0 and i < 30:
            print(round(i), "days -", round(game.ant_pro, 2), "%")
        elif i % 30 == 0:
            print(round(i / 30), "kk -", round(game.ant_pro, 2), "%")
        return

    # Calculations
    def cal():
        return


if __name__ == '__main__':

    game = settings()
    last_time = time.time()
    print("Starting")
    print("---------------")
    print("Time - Process")

    while game.ant_pro < 100:
        game.time = game.time + (1 / game.acc)
        settings.start()
        settings.print()

    final()
