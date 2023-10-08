import random
import streamlit as st
import base64
import selection
def anagram(inp):
	inp=inp.lower()
	return ''.join(random.sample(inp,len(inp)))

def toBinary(inp):
	inp=inp.lower()
	return ''.join(format(ord(i), '08b')+" " for i in inp)

def numSub(inp):
	inp=inp.lower()
	inp=[*inp]
	#inp=[i for i in inp i.lower()]
	out=[]
	for char in inp:
		char=char.lower()
		match char:
			case "a":
				out.append("/\\ ")
			case "b":
				out.append("8 ")
			case "c":
				out.append("< ")
			case "d":
				out.append("|) ")
			case "e":
				out.append("3 ")
			case "f":
				out.append("|= ")
			case "g":
				out.append("6 ")
			case "h":
				out.append(")-( ")
			case "i":
				out.append("1 ")
			case "j":
				out.append("_/ ")
			case "k":
				out.append("[< ")
			case "l":
				out.append("| ")
			case "m":
				out.append("|V| ")
			case "n":
				out.append("/V ")
			case "o":
				out.append("0 ")
			case "p":
				out.append("|* ")
			case "q":
				out.append("0, ")
			case "r":
				out.append("|2 ")
			case "s":
				out.append("5 ")
			case "t":
				out.append("7` ")
			case "u":
				out.append("(_) ")
			case "v":
				out.append("\\/ ")
			case "w":
				out.append("\\/\\/ ")
			case "x":
				out.append("% ")
			case "y":
				out.append("`/ ")
			case "z":
				out.append(">_ ")
			case _:
				out.append("   ")
	fin=""
	"""
	for ch in inp:
		fin+=str(ch)
	"""
	return "".join(out)

"""
def hangman(showLocation):
	strike = 0
	lowerlocation=showLocation.lower()
	lowerguess = guess.lower()
	while (strike<5) || (correct==len(lowerguess)):
		if (lowerguess in lowerlocation):
			correct+=1
		else:
			strikes+=1
	if(correct==len(lowerguess)):
		return win
	else:
		return lose
	#name

file_ = open("/Desktop/HUTA/images/smth.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)"""

print(numSub("Walter"))