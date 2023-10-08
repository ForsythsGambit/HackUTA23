import streamlit as st
import pandas as pd
import numpy as np
import selection
import time
import random
import puzzles

"""Displays the locations on a map and allow the player to switch which building is selected."""
#https://discuss.streamlit.io/t/map-plotting-using-streamlit-map/

x=0

grey="#808080" #grey
selected ="#FF0000" #red
@st.cache_data
def start_game(inp=None):
	chosenWeapon = []
	chosenPeople = []
	chosenLocation = []
	x = 0
	selected = ""
	thing = selection.info()
	#chosenWeapon = thing.chooseWeapon()
	chosenLocation = thing.chooseLocation()
	chosenPeople = thing.choosePeople()
	killer = thing.showKiller()
	#murder_weapon = thing.showWeapon()
	murder_location = thing.showLocation()
	chosenX = list(range(0,len(chosenLocation)))
	chosenY = list(range(0,len(chosenLocation)))	

	for i in range(0,len(chosenLocation)):
		chosenX[i] = thing.chooseyVal(i)
		chosenY[i] = thing.chooseyVal(i)
	
	

	
	df = pd.DataFrame([
		{"Locations": chosenLocation[0],"People": chosenPeople[0], "Suspects": False},
		{ "Locations": chosenLocation[1],"People": chosenPeople[1], "Suspects": False},
		{"Locations": chosenLocation[2],"People": chosenPeople[2], "Suspects": False},
		{ "Locations": chosenLocation[3],"People": chosenPeople[3], "Suspects": False},
		{ "Locations": chosenLocation[4],"People": chosenPeople[4], "Suspects": False},
		{"Locations": chosenLocation[5],"People": chosenPeople[5], "Suspects": False}
		])
	edited_df = st.data_editor(df, num_rows="dynamic", width= 1000)
	
	lat = list(range(0,len(chosenX)))
	long = list(range(0,len(chosenX)))
		#print(chosenX[0][0])
		#print(chosenY[0][1])
	
	for i in range(0,len(chosenX)):
		lat[i] = chosenX[i][0]
		long[i] = chosenY[i][1]

	grey="#808080" #grey
	selected ="#FF0000" #red

	ArlingtonMapDictionary={
	'buildings' : chosenLocation,
	'lat' : lat,
	'lon' : long,
	'color' : [grey,grey,grey,grey,grey,grey]
	}

	ArlingtonMapDataFrame=pd.DataFrame({
		'buildings' : chosenLocation,
		'lat' : lat,
		'lon' : long,
		'color' : [grey,grey,grey,grey,grey,grey]
	})
	print(killer)
	shuffledPeople=chosenPeople.copy()
	random.shuffle(shuffledPeople)
	return chosenPeople, chosenLocation, chosenX, chosenY, lat, long,x,ArlingtonMapDictionary,ArlingtonMapDataFrame,selected,killer,murder_location,shuffledPeople



#checks to see if answer is rightr
def checkAnswer(person, location):
	if person == killer and location == murder_location:
		st.write("YOU WIN")
	else:
		st.write("you need to sleep")

#Create a Restart game func
def restart():
	x+=1
	start_game(x)
chosenPeople, chosenLocation, chosenX, chosenY, lat, long,x,ArlingtonMapDictionary,ArlingtonMapDataFrame,selected,	killer,murder_location,shuffledPeople = start_game(x)
#print(shuffledPeople)

@st.cache_data
def getClue(index):
	""""Take an index (of the chosenLocation) then use puzzles.py to generate a clue for a suspect"""
	#print("getting clue from indice of "+str(index))
	if shuffledPeople[index]==killer:
		#print("indice is "+str(index)+" which is "+shuffledPeople[index])
		while True:
			r=random.randint(0,5)
			if r != index:
				index=r
				print("subbed index is "+str(r)+" who is "+shuffledPeople[r])
				break
	match index:
		case 0:
			return puzzles.anagram(shuffledPeople[index])
		case 4:
			return puzzles.anagram(shuffledPeople[index])
		case 1:
			return puzzles.toBinary(shuffledPeople[index])
		case 5:
			return puzzles.toBinary(shuffledPeople[index])
		case 2:
			return puzzles.numSub(shuffledPeople[index])
		case 3:
			return puzzles.numSub(shuffledPeople[index])
		case _:
			return index

	

location = st.selectbox("Investigate which building?",(chosenLocation),index=None)

if location != None:
	ChoiceIndex=ArlingtonMapDictionary['buildings'].index(location)
	st.write("Decode the clue to eliminate a suspect: "+str(getClue(ChoiceIndex)))
	for indice in range(0,len(ArlingtonMapDataFrame["color"])):
		if ArlingtonMapDataFrame["color"][indice]==selected and ChoiceIndex != indice:
			ArlingtonMapDataFrame["color"][indice]=grey
		if ArlingtonMapDataFrame["color"][indice]==grey and ChoiceIndex == indice:
			ArlingtonMapDataFrame["color"][indice]=selected
st.map(ArlingtonMapDataFrame, latitude='lat', longitude='lon', color='color',size=5)
#if selected in ArlingtonMapDataFrame['color']:
#    ArlingtonMapDataFrame['color'][ArlingtonMapDataFrame.index[ChoiceIndex]]="#FF0000"



people = st.selectbox("Which Person?",(chosenPeople))
#weapon = st.selectbox("Which Weapon?",(chosenWeapon))

#starts to check answers
if st.button ("Submit Answer"):
	checkAnswer(killer, murder_location)
if st.button("Restart"):
	restart()