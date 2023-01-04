import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


delay = 3.0 # Pause between steps
brief_pause = 0.2 # Very short pause so that you can see whats happening
click = Button.left
click_time = 0
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

# X,Y positions where the cursor should go for each action
reset_pos = (1945, 607) # This is a generic position to ensure all menus are minimised
generic_rhs_pos = (2399, 705)

stats_pos = (1725, 101)
options_pos = (1730, 54)
save_pos = (1796, 342)

get_all_upgrades_pos = (2381, 176)
buy_100_pos = (2452, 274)

javascript_pos = (2405, 1170)
cortex_baker_pos = (2381, 1299)

legacy_pos = (2173, 102)
ascend_pos = (1919, 788)
reincarnate_pos = (1913, 142)
reincarnate_yes_pos = (1899, 735)

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_loop(self):
        self.running = True

    def stop_loop(self):
        self.running = False

    def move_to(self, to_pos: tuple[int, int]):
        # Where am I and where do I want to be
        x = int(0)
        y = int(0)
        x = to_pos[0] - mouse.position[0]
        y = to_pos[1] - mouse.position[1]

        mouse.move(x, y)

    def exit(self):
        self.stop_loop()
        self.program_running = False

    def accend(self):
        # Open Legacy Menu
        self.move_to(legacy_pos)
        mouse.click(click, click_time)
        time.sleep(brief_pause)

        # Click Ascend
        self.move_to(ascend_pos)
        mouse.click(click, click_time)

        # Wait for the animation or press escape
        time.sleep(4.0)

        # Click Reincarnate
        self.move_to(reincarnate_pos)
        mouse.click(click, click_time)
        time.sleep(brief_pause)

        # Accept Modal Menu
        self.move_to(reincarnate_yes_pos)
        mouse.click(click, click_time)
        time.sleep(brief_pause)

    def buy_all_upgrades(self):
        self.move_to(generic_rhs_pos)
        mouse.scroll(0,1000) # Scroll to TOP
        time.sleep(brief_pause)

        self.move_to(get_all_upgrades_pos)
        mouse.click(click, click_time)
        time.sleep(brief_pause)

    def set_buy_100(self):
        self.move_to(generic_rhs_pos)
        mouse.scroll(0,1000) # Scroll to TOP
        time.sleep(brief_pause)

        self.move_to(buy_100_pos)
        mouse.click(click, click_time)
        time.sleep(brief_pause)

    def buy_js(self):
        self.move_to(generic_rhs_pos)
        mouse.scroll(0,1000) # Scroll to BOTTOM
        time.sleep(brief_pause)

        self.move_to(javascript_pos)
        mouse.click(click, click_time)
        time.sleep(brief_pause)

    def buy_cortex(self):
        self.move_to(generic_rhs_pos)
        mouse.scroll(0,1000) # Scroll to BOTTOM
        time.sleep(brief_pause)

        self.move_to(cortex_baker_pos)
        mouse.click(click, click_time)
        time.sleep(brief_pause)

    def save_game(self):
        # Open Options
        self.move_to(options_pos)
        mouse.click(click, click_time)
        time.sleep(brief_pause)

        # Save Game
        self.move_to(save_pos)
        mouse.click(click, click_time)
        time.sleep(brief_pause)

        # Back to stats
        self.move_to(stats_pos)
        mouse.click(click, click_time)
        time.sleep(brief_pause)

        # Accept Modal Menu
        self.move_to(reset_pos)

    def run(self):
        while self.program_running:
            while self.running:
                # Save the game before any steps are taken this loop
                self.save_game()

                # Set buy 100
                self.set_buy_100()

                # Buy all upgrades 4 times
                self.buy_all_upgrades()
                time.sleep(self.delay)
                self.buy_all_upgrades()
                time.sleep(self.delay)
                self.buy_all_upgrades()
                time.sleep(self.delay*2)
                self.buy_all_upgrades()
                time.sleep(self.delay*2)

                self.buy_js()
                time.sleep(self.delay)
                self.buy_cortex()
                time.sleep(self.delay)
                self.buy_cortex()
                time.sleep(self.delay)

                self.buy_all_upgrades()
                time.sleep(self.delay)

                self.accend()
            time.sleep(brief_pause)

mouse = Controller()
click_thread = ClickMouse(delay, click)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_loop()
        else:
            click_thread.start_loop()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
