#!/usr/bin/env python3

import os
import curses

current_option = 0
options = []

def get_files():
   files = os.listdir('.')
   files.sort()
   return files

def change_option(option, direction):
   if direction == 'UP':
      option = len(options) - 1 if option == 0 else option - 1
   if direction == 'DOWN':
      option = 0 if option == len(options) - 1 else option + 1
   return option

def move_arrow(direction, screen):
   global current_option
   current_option = change_option(current_option, direction)
   screen.addstr(current_option, 0, "--> ", curses.color_pair(1))

stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
curses.start_color()
curses.use_default_colors()
curses.init_pair(1, curses.COLOR_RED, -1)
curses.init_pair(2, curses.COLOR_BLUE, -1)
stdscr.keypad(1)
stdscr.refresh()


key = ''
while key != ord('q'):
   if key == curses.KEY_RIGHT and os.path.isdir(os.getcwd() + '/' + options[current_option]):
      os.chdir(os.getcwd() + '/' + options[current_option])
      current_option = 0
   elif key == curses.KEY_LEFT:
      os.chdir('..')
      current_option = 0

   options = get_files()
   stdscr.clear()
   for i in range(len(options)):
      path = os.getcwd() + '/' + options[i]
      if os.path.isdir(path):
         stdscr.addstr(i, 0, "    " + options[i] + "/", curses.color_pair(2))
      else:
         stdscr.addstr(i, 0, "    " + options[i])

   if key == curses.KEY_UP:
      move_arrow('UP', stdscr)
   if key == curses.KEY_DOWN:
      move_arrow('DOWN', stdscr)
   else:
      move_arrow('', stdscr)

   stdscr.addstr(len(options) + 1, 0, "Hit 'ENTER' to change directory")
   stdscr.addstr(len(options) + 2, 0, "Hit 'q' to quit")
   key = stdscr.getch()

curses.endwin()
