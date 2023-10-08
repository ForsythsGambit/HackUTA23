import streamlit as st
import pandas as pd
#import numpy as np
from random import randint  

value = randint(0,6)
r=6
killer = ""
#murder_weapon = ""
murder_location = ""
people =["Shawn","Kevin","Devin","Liam","Braelin","Anthony","Dhruv","Ivan","Seth","Tracy","Sai","Caden","Priyanka","Abby","Amanda","Brooklynn","David","Dhar","Eric","Kashika","Maeson","Malchus","Max","Mehul","Mika","mrunmayi","Neil","Samantha"]
#weapon =["Hammer","Knife","Vase","Katana","Nerf_Gun","Midterm","Poison","Lightning","Fire","Exam"] 
locations =['Library', 'Pickard', 'Fine Arts Bridge', 'University Center', 'Planetarium', 'Engineering Research Building', 'College Park','SEIR','SWSH',"Science Hall", "Nedderman Hall","The Commons","West Hall"]
xylocations = {
    "Library" : [32.729711101877164, -97.11289756227923],
    "Pickard" : [32.728999221890035, -97.1114415981052],
    "Fine Arts Bridge" : [32.73066273429193, -97.11458056700222],
    "University Center" : [32.7316145510585, -97.11103650951921],
    "Planetarium" : [32.730462943599655, -97.11212146579929],
    "Engineering Research Building" : [32.73328698351632, -97.11251909376378],
    "College Park" : [32.730668418221256, -97.10804861945682],
    "SEIR" : [32.72808413378668, -97.11299009208584],
    "SWSH" : [32.72767120776325, -97.11162756178405],
    "Science Hall" : [32.73068979530391, -97.11407334597426],
    "Nedderman Hall" : [32.73241974163169, -97.1138533100702],
    "The Commons" : [32.73276857449126, -97.11703536854183],
    "West Hall" : [32.73304410208603, -97.11847107981099]
}
chosenPeople = list(range(r))
#chosenWeapons = list(range(r))
chosenLocations = list(range(r))
#self,value,killer,murder_weapon,murder_location,people,weapon,locations,xylocations,r,chosenPeople,chosenWeapon,chosenLocation
class info():
    def __init__(self):
        
        self.r=r
        self.value = value
        self.killer = killer
        #self.murder_weapon = murder_weapon
        self.murder_location = murder_location
        self.people = people
        #self.weapon = weapon
        self.locations =locations
        self.xylocations = xylocations
        self.chosenPeople = chosenPeople
        #self.chosenWeapons = chosenWeapons
        self.chosenLocations = chosenLocations
        MapDict={
            "buildings" : [],
            "lat" : [],
            "lon" : [],
            "color" : []
        }
        for loc in xylocations:
            MapDict["buildings"].append(loc)
            MapDict["lat"].append(xylocations[loc][0])
            MapDict["lon"].append(xylocations[loc][1])
    
    def check(self,chosen, value, people):
        value = randint(0,len(people)-1)
        if people[value] not in chosen:
            return value
        
    def randomize(self,chosen,people,r):
        value = randint(0,len(people)-1)
        for i in range(0,r):
            value = randint(0,len(people)-1)
            while value is None or people[value] in chosen:
                value = self.check(chosen,value,people)
            else:
                chosen[i] = people[value]
    
    def choosePeople(self):
        self.chosenPeople = self.randomize(chosenPeople,people,len(chosenPeople))
        self.killer = chosenPeople[randint(0,len(chosenPeople)-1)]
        return chosenPeople
    def showKiller(self):
        return self.killer
    #def chooseWeapon(self):
        #self.chosenWeapons = self.randomize(chosenWeapons,weapon,len(chosenWeapons))
        #self.murder_weapon = chosenWeapons[randint(0,len(chosenWeapons)-1)]        
        #return chosenWeapons
    #def showWeapon(self):
        #return self.murder_weapon
    def chooseLocation(self):
        self.chosenLocations = self.randomize(chosenLocations,locations,len(chosenLocations))
        self.murder_location = chosenLocations[randint(0,len(chosenLocations)-1)]
        return chosenLocations
    def showLocation(self):
        return self.murder_location
    
    def choosexVal(self,i):
        return xylocations.get(chosenLocations[i])
    def chooseyVal(self,i):
        return xylocations.get(chosenLocations[i])