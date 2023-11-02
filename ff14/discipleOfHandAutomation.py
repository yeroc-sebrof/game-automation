#!/usr/bin/env python

from pyautogui import press as keyPress, mouseDown, mouseUp
from time import sleep

startAnimationWait = 1.25
abilityWait = 3.25
stopAnimationWait = 1.25

howManyTimes = 10
itemName = "Stone Level 40"

def make(abilitiesList: list[str]):
  for b in abilitiesList:
    # Starting a new item animation
    sleep(startAnimationWait)

    keyPress(b)
    sleep(abilityWait)

    # Completed product animation
    sleep(stopAnimationWait)


def click():
  mouseDown()
  sleep(0.2)
  mouseUp()


def estimateTotal(iterations: int, name: str, item: dict[str, list[str]]):
  totalMoves = len(item)
  timePer = startAnimationWait + (totalMoves * abilityWait) + stopAnimationWait
  totalTimeMins, remainingSeconds = divmod(timePer * totalMoves * iterations, 60)
  totalTimeHours, remainingMins = divmod(totalTimeMins, 60)

  print("%d loops of item %s. This will take around %d:%02d:%02d" % (iterations, name, int(totalTimeHours), int(remainingMins), int(remainingSeconds)))


class abilities:
  basicSynthesis = '1'
  basicTouch = '2'
  standardTouch = '3'
  greatStrides = '4'
  # 5
  wasteNot = '6'
  veneration = '7'
  innovation = '8'
  # 9
  # 0
  # -
  # =


goldsmith = {
  "Stone Level 32": [
    abilities.wasteNot,
    abilities.innovation,
    abilities.basicTouch,
    abilities.standardTouch,
    abilities.basicTouch,
    abilities.standardTouch,
    abilities.basicTouch,
    abilities.veneration,
    abilities.basicSynthesis
    ],

  "Stone Level 40": [
    abilities.wasteNot,
    abilities.innovation,

    abilities.basicTouch,
    abilities.standardTouch,

    abilities.basicTouch,
    abilities.standardTouch,

    abilities.basicTouch,

    abilities.veneration,
    abilities.basicSynthesis
    ]
}


blacksmith = {
}


armourer = {
}


leatherworker = {
}


if __name__ == "__main__":
  estimateTotal(howManyTimes, itemName, goldsmith)

  for w in range(3, 0, -1):
    sleep(1)
    print(w)

  for i in range(howManyTimes):
    print(f"Starting item number: {i}")

    # Left mouse click to press the Synthesis button
    click()

    make(goldsmith[itemName])
