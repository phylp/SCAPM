import os
import time

clear_console = "clear" if os.name == "posix" else "CLS"

def clear(seconds):
	time.sleep(seconds)
	os.system(clear_console)

def wait(seconds):
	time.sleep(seconds)

def getch():
	try:
		import sys, tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
			return ch
	except ImportError:
		import msvcrt
		return msvcrt.getch()