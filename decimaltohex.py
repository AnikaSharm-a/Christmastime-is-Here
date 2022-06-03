# Getting hex value 
def getHexVal(x):
	h = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
	hexval = ""

	while x != 0:
		r = x % 16
		x //= 16
		hexval = h[r] + hexval

	if hexval == "": return "00"
	elif len(hexval) == 1: return "0" + hexval
	return hexval 

# Getting a colour when given rgb vals
def getColour(r, g, b):
	rHex = getHexVal(r)  
	gHex = getHexVal(g)  
	bHex = getHexVal(b)  
	return "#" + rHex + gHex + bHex