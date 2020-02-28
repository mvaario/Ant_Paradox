# Ant on rubber rope paradox
# How can ant reach end of the rope, if the rope is extending
# "Increasing the distance by more than his progress"
# Inspired by Vsauce2
# Made by mvaario

import time
import math
from math import e

# Final data
def final():
    print("")
    print("Done, final data")
    print("---------------")
    print("Ant final position", round(game.ant, game.acc), " m")
    print("Rope final length", round(game.rope, game.acc), " m")
    print("Ant moved ", round(game.ant_speed * game.t, game.acc), "m")
    if game.rope_acceleration != 0:
        print("Rope speed", game.rope_speed, "m/s")

    final_times()
    print("---------------")

    return

# Final time
def final_times():
    time = game.t
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
        print("Time", h, "hours", round(min,1), "min")
    elif time > 60:
        min = time / 60
        sec = (min - math.floor(min)) * 60
        min = math.floor(min)
        print("Time", min, "min", round(sec, game.acc), "sec")
    else:
        print("Time", round(time, game.acc), "sec")


class settings:
    def __init__(self):
        #  Accurate, 1, 2, 3, aka 10^acc / sec accurate -- how many decimals
        self.acc = 5

        # Ant's starting position in meters
        self.ant = 0

        # Rope's starting length in meters
        self.rope = 10

        # ant's moving speed m/s      - light speed = 300 000 km/s
        self.ant_speed = 1

        # Rope's extending speed m/s  - universe expanding speed = 73 km/s
        self.rope_speed = 2

        # Rope's acceleration m/s^2
        self.rope_acceleration = 0

        # ant process in %
        self.ant_pro = 0

        # times
        self.t = 0
        # sleep
        self.sleep = 0.5
        # calculated
        self.cal = 0

        # printing secs
        self.print = 1
        self.i = 0
        return

    def start():
        # ant position in meters
        game.ant = game.ant + game.ant_speed / (10 ** game.acc)

        # rope new length
        settings.rub_lenght()

        return

    # Rubber rope length
    def rub_lenght():

        # and process
        game.ant_process()
        # rope new length
        game.rope = game.rope + game.rope_speed / (10 ** game.acc)

        # new ant position
        if game.ant_pro != 0:
            game.ant = (game.rope * game.ant_pro / 100)

        game.rope_speed = game.rope_speed + game.rope_acceleration / (10 ** game.acc)

        return

    # Ant process in percentages
    def ant_process(self):
        # ant process
        game.ant_pro = 100 / game.rope * game.ant

        return

    # Times
    def print():
        i = round(game.t)
        t = round(game.t)
        if game.acc > 4:
            sleep = 0
        elif game.acc != 0:
            sleep = game.sleep / game.acc
        else:
            sleep = game.sleep

        if game.i != t:
            if i < 86400 and game.print == 1:
                if i < 10:
                    time.sleep(sleep)
                    print(t, "sec -", round(game.ant_pro, 2), "%")
                if i % 10 == 0 and i < 60:
                    time.sleep(sleep)
                    print(t, "sec -", round(game.ant_pro, 2), "%")

                if i % 60 == 0 and i < 600:
                    time.sleep(sleep)
                    print(round(t / 60), "min -", round(game.ant_pro, 2), "%")
                elif i % 600 == 0 and i < 3600:
                    time.sleep(sleep)
                    print(round(t / 60), "min -", round(game.ant_pro, 2), "%")

                i = i / 60
                if i % 60 == 0 and i < 600:
                    print(round(t / 3600), "h -", round(game.ant_pro, 2), "%")
                elif i % 600 == 0 and i < 1440:
                    print(round(t / 3600), "h -", round(game.ant_pro, 2), "%")

            else:
                i = i / 60
                if i >= 1440:
                    i = i / 1440
                    settings.print_days(i)
        game.i = t

        return
    # Times days / kk
    def print_days(i):
        if i % 1 == 0 and i < 30:
            print(round(i), "days -", round(game.ant_pro, 2), "%")
        elif i % 30 == 0:
            print(round(i / 30), "kk -", round(game.ant_pro, 2), "%")
        return

    # Calculations
    def cal():
        if game.rope_acceleration == 0:
            print("")
            print("Calculated")
            print("---------------")
            if game.cal == 0:
                v0 = game.rope_speed
                va = game.ant_speed
                x0 = game.rope

                cal = ((e**(v0/va)-1)*x0)/v0
                game.cal = cal

            cal = game.cal
            if cal > 86400:
                day = cal / 86400
                h = round((day - math.floor(day)) * 24)
                day = math.floor(day)
                print("Time", day, "day", h, "hours")
            elif cal > 3600:
                h = cal / 3600
                min = round((h - math.floor(h)) * 60)
                h = math.floor(h)
                print("Time", h, "hours", round(min), "min")
            elif cal > 60:
                min = cal / 60
                sec = (min - math.floor(min)) * 60
                min = math.floor(min)
                print("Time", min, "min", round(sec, game.acc), "sec")
            else:
                print("Time", round(cal, game.acc), "sec")

        return


if __name__ == '__main__':

    game = settings()
    last_time = time.time()
    settings.cal()
    print("Starting")
    print("---------------")
    print("Time - Process")

    while game.ant_pro < 100:
        game.t = game.t + (1 / (10 ** game.acc))
        settings.start()
        settings.print()

    final()
    settings.cal()
