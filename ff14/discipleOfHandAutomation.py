#!/usr/bin/env python

# Summary:
# This code cannot simply be run out the box. Some assembly required. It currently is loaded with few recipes. You can
# just get more online or you can learn as you go.

# Remarks:
# - vgamepad would perhaps work better? It'd give me more control to press the synthesis button
# - This has a good list of button order but I don't like the rounded int waits: https://ffxivgillionaire.com/crafting-macros
# - I need a greater check for food around the standard for loop. I don't want a separate thread because I don't want it
#     to disturb the on-going craft. Just do it between crafts.
# - It would be good if I could queue up multiple item craft loops. This could allow for further dependency crafting.
#   - Although that would require a way to make it explicitly craft with HQ dependencies.

from pyautogui import press as keyPress, mouseDown, mouseUp
from time import sleep

startAnimationWait = 1.25
additionalButtonWait = 1.55 # This is for some of the actions that have extra animation
buttonWait = 1.45
stopAnimationWait = 3.25

itemName = "Stone Level 30 > 40"

abilities = {
  "Great Strides": '4',
  "Waste Not": '6',
  "Veneration": '7',
  "Innovation": '8'
}

actions = {
  "Basic Synthesis": '1',

  "Basic Touch": '2',
  "Standard Touch": '3'
}


def make(buttonList: list[str]):
  # Starting a new item animation
  sleep(startAnimationWait)

  for b in buttonList:
    keyPress(b)
    if (b in actions.values()):
      sleep(additionalButtonWait)
    
    sleep(buttonWait)

  # Completed product animation
  sleep(stopAnimationWait)


def click():
  mouseDown()
  sleep(0.2)
  mouseUp()


def estimateTotal(iterations: int, name: str, item: list[str]):
  """
  This will estimate how long crafting will take. Does not take into account actions vs abilities.
  """

  totalMoves = len(item)
  timePer = startAnimationWait + (totalMoves * (buttonWait + additionalButtonWait)) + stopAnimationWait
  totalTimeMins, remainingSeconds = divmod(timePer * totalMoves * iterations, 60)
  totalTimeHours, remainingMins = divmod(totalTimeMins, 60)

  print("%d loops of item %s. This will take around %d:%02d:%02d" % (iterations, name, int(totalTimeHours), int(remainingMins), int(remainingSeconds)))


def getCost(iterations: int, item: dict[str, int]):
  print("This will cost around:")

  for k in item.keys():
    print("- %s: %d" % (k, item[k] * iterations))

  print()


items = {
  "Stone Level 30 > 40": {
    "moves": [
      abilities["Waste Not"],
      abilities["Innovation"],

      actions["Basic Touch"],
      actions["Standard Touch"],
      
      actions["Basic Touch"],
      actions["Standard Touch"],
      
      actions["Basic Touch"],

      abilities["Veneration"],
      actions["Basic Synthesis"]
      ],
      "cost": {
        "stone": 1,
        "wind shard": 5
      }
  },
  "Maple": {
    "moves": [
      actions["Basic Touch"],
      actions["Basic Touch"],

      actions["Basic Synthesis"]
      ]
  }
}

if __name__ == "__main__":
  # howManyTimes, _ = divmod(21, 3)
  howManyTimes, _ = divmod(263, items[itemName]["cost"]["wind shard"])

  if ("moves" not in items[itemName].keys()):
    raise Exception("You need to define the item moves")
  
  estimateTotal(howManyTimes, itemName, items[itemName]["moves"])

  if ("cost" in items[itemName].keys()):
    getCost(howManyTimes, items[itemName]["cost"])

  print ("...")

  sleep(5)

  for w in range(3, 0, -1):
    sleep(1)
    print(w)

  for i in range(howManyTimes):
    print(f"Starting item number: {i}")

    # Left mouse click to press the Synthesis button
    click()

    make(items[itemName]["moves"])
