#1: Ask a virtual assistant:
def repeat1(string, count):
	"""
	Prints the given string the specified number of times.

	:param string: The string to print.
	:param count: The number of times to print the string.
	"""
	for _ in range(count):
		print(string)


def repeat2(string, count):
	"""
	Prints the given string the specified number of times.

	:param string: The string to print.
	:param count: The number of times to print the string.
	"""
	# Create the repeated string by multiplying and join with new lines
	result = (string + '\n') * count
	
	# Print the result
	print(result, end='')


def draw_rectangle(pattern, width, height):
	"""
	Draws a rectangle of the given dimensions using the specified string pattern.

	:param pattern: The string to use for drawing the rectangle.
	:param width: The width of the rectangle.
	:param height: The height of the rectangle.
	"""
	# Ensure the pattern is not empty and width and height are positive
	if not pattern or width <= 0 or height <= 0:
		raise ValueError("Pattern must be non-empty, and width and height must be positive integers.")
	
	# Create one line of the rectangle
	line = pattern * width
	
	# Print each line to form the rectangle
	for _ in range(height):
		print(line)

#2:
def print_right(text):
	string = " "*(40-len(text))+text
	print(string)
	return string

print_right("Monty")
print_right("Python's")
print_right("Flying Circus")

#3:
def triangle(string, height):
	height = int(height)
	for i in range(height):
		print(string*(i+1))

triangle("fnord", 5)

#4:
def rectangle(string, w, h):
	print((string*w + "\n")*h)

rectangle("8", 4,3)

#5:
def bottle_verse(num):
	BOB = "bottles of beer"
	print(f"{num} {BOB} on the wall\n{num} {BOB}\nTake one down, pass it around\n{num-1} {BOB} on the wall\n")

bottle_verse(99)