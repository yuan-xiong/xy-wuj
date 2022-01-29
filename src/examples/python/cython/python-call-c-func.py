import os
from add_wrapper import add

# https://www.yanxurui.cc/posts/python/2017-06-18-3-ways-of-calling-c-functions-from-python/

if __name__ == '__main__':
	print("Test Python calling C function")

	add(1, 2)
