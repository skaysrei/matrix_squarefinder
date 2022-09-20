from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def read_root():
    return "running"

@app.get("/isthere")
def read_root():
    return "Hello world"


def es40(jsonFile, k):
	square = [-1, -1]

	f = open(jsonFile)
	data = json.load(f)
	f.close()

	print("\n\nInput jsonFile: \n")
	for row in data:
		print("\n", row)

	rows = len(data)
	cols = len(data[0])

	for y in range(0, cols - 1):
		#Exit the cycle if out of bound
		if (y + k) > rows-1:
			break
		for x in range(0, rows - 1):
			#Exit the cycle if out of bound
			if (x + k) > cols-1:
				break
			
			#Show current status
			print(f'\n\n({y} | {x})')
			print(data[x][y])
			print(data[x][y+k])
			print(data[x+k][y+k])
			print(data[x+k][y])
			#Checks if a square 'k' exists
			if 	data[x][y+k] - data[x][y] == 1 and \
				data[x+k][y+k] - data[x][y+k] == 1 and \
				data[x+k][y] - data[x+k][y+k] == 1:

				print("SQUARE FOUND!")

				#If the square is lower replace it
				if x >= square[1]:
					square[1] = x
					if y >= square[0]:
						square[0] = y
	
	return tuple(square)