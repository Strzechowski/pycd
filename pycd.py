#!/usr/bin/env python3

import os
import curses

current_option = 0
options = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']

def change_option(option, direction):
   if direction == 'UP':
      option = len(options) - 1 if option == 0 else option - 1
   if direction == 'DOWN':
      option = 0 if option == len(options) - 1 else option + 1
   return option

def move_arrow(direction, screen):
   global current_option
   #for i in range(8):
   #   screen.delch(current_option, 0)
   current_option = change_option(current_option, direction)
   screen.addstr(current_option, 0, "--> ")


stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
stdscr.keypad(1)
stdscr.refresh()


key = ''
while key != ord('q'):
   stdscr.refresh()
   for i in range(len(options)):
      stdscr.addstr(i, 0, "    " + options[i])

   if key == curses.KEY_UP:
      move_arrow('UP', stdscr)
   elif key == curses.KEY_DOWN:
      move_arrow('DOWN', stdscr)

   stdscr.addstr(len(options), 0, "Hit 'q' to quit")
   key = stdscr.getch()

curses.endwin()
