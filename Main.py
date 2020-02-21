# Ant on rubber rope paradox
# How can ant reach end of the rope, if the rope is extending
# "Increasing the distance by more than his progress"
# Inspired by Vsauce2
# Made by mvaario

import time
import math

class settings:
    def __init__(self):

        # Ant's starting position in meters
        self.ant = 0

        # Rope's starting length in meters
        self.rope = 10

        # ant's moving speed m/s
        self.ant_speed = 1

        # Rope's extending speed m/s
        self.rope_speed = 100

        # Rope's acceleration m/s^2
        self.rope_acceleration = 0



        # ant process in %
        self.ant_pro = 0
        # Times
        self.sec = 0
        self.min = 0
        # Wait time
        self.time = 0

        return

    def start():
        # ant position in meters
        game.ant = game.ant + game.ant_speed

        settings.ant_process()
        ant_pro = game.ant_pro
        if ant_pro < 100:
            settings.rub_leinght()
            game.rope_speed = game.rope_speed + game.rope_acceleration

        return

    def rub_leinght():
        length = game.rope
        speed = game.rope_speed
        game.rope = length + speed

        # new ant position
        if game.ant_pro != 0:
            length = game.rope
            ant_pro = game.ant_pro
            game.ant = (length * ant_pro / 100)

        return

    def ant_process():

        # ant process
        ant = game.ant
        length = game.rope
        game.ant_pro = 100 / length * ant

        return

    # for printing times
    def time(i):
        if i < 60:
            time.sleep(game.time)
        elif i < 1200:
            time.sleep(game.time / 100)

        if i < 60:
            print(i, "s - ", round(game.ant_pro,2) , "%")
            game.sec = i
        else:
            min = i / 60
            sec = (i - (60 * math.floor(min)))/ 10
            sec = math.floor(sec)
            sec = sec * 10
            min = math.floor(min)


            if game.sec != sec or game.min != min:
                print(min, "min", sec, "sec", "- ", round(game.ant_pro, 2), "%")

            game.sec = sec
            game.min = min
        return

if __name__ == '__main__':

    game = settings()
    last_time = time.time()
    i = 0
    F = 0
    print("Starting")
    print("---------------")
    print("Time - Process")

    while F < 100:
        i = i + 1
        settings.start()
        F = game.ant_pro
        settings.time(i)

    # Final results
    time.sleep(0.2)
    print("")
    print("Done, final data")
    print("---------------")
    print("Time", game.min, "min", game.sec, "sec")
    print("Ant final position", round(game.ant, 2), " m")
    print("Rope final length", round(game.rope, 2), " m")


