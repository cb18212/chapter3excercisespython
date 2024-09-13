#1: Ask a virtual assistant:

#No
#Thou shalt not make a machine in the likeness of a human mind.

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