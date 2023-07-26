from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
from dataclasses import Field
from fastapi.security import OAuth2PasswordRequestForm, OAuth2AuthorizationCodeBearer
from jose import jwt
#1 ist damit wir passwort und username mit request mitgeben können, andee für screamer und authentifizieren
from typing import Union
from pydantic import BaseModel
from enum import Enum
from fastapi.responses import HTMLResponse

from fastapi import FastAPI


#persons= []



class Type(Enum):
    wählbar= "wählbar"
    nicht_wählbar= "nicht wählbar"
    
class Persons(BaseModel):
    vorname: str
    nachname: str
    alter: int
    email: str
    telefonnummer: str
    wählbar: Type
    
class Vote(BaseModel):
    person: Persons
    weight: int =1
    
persons= []

    
app= FastAPI()

#oauth2= OAuth2AuthorizationCodeBearer(tokenUrl="login")


@app.post("/persons")
async def create_person(person: Persons):
    for neueperson in persons:
        if neueperson.vorname== person.vorname and neueperson.nachname== person.nachname:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="already exist")
            
    persons.append(person)
    return("Die Person wurde hinzugefügt")

@app.get("/persons" )
async def show():
    #jwt.decode(token)
    return persons
    

@app.get("/persons")
async def show_person(person: Persons):
    return person
    
    
@app.post("/vote")
    
async def erhoehe_person(person: Persons, gewicht: Vote):
    person= gewicht.person
    #for person in Persons:
    if person.wählbar== Type.nicht_wählbar:
        gewicht.person==0
        return ("Diese Person ist nicht wählbar")
        
    #if person.wählbar==Type.wählbar:
        # checken ob person schon gewählt hat, stimme auf eine begrenzt also ob sie noch eine stimme hat 
    for wählen in persons:
        #if wählen.
        if wählen.person== gewicht.person:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="already voted")
                
        
            
        persons.append(gewicht)
     
    return(persons)

@app.get("/vote")
# liste von vote objekten werdeb übergeben ergebnisse der gewählten personen 
async def ergebnisse_zeigen(pers: Persons, vote: Vote):
    # alle wählbaren personen sollen in liste sein und die ergebnisse ausgewertet werden--> alle stimmen generell sollen ausgegeben werden pro person + der durchschnittliche anteil an den gesamt stimmen
    liste= []
    for neueperson in persons:
        if neueperson.wählbar==Type.wählbar:
        #for wählen in persons:
            alle_stimmenpropers= sum(wählen.weight for wählen in persons if wählen.person== neueperson)
            prozentualeanteile= alle_stimmenpropers/len(persons) * 100
            liste.append("Kandidat: "+ neueperson+ "Stimmen gesamt: "+ alle_stimmenpropers+ "Prozentualer Anteil: "+ prozentualeanteile )
            
    return liste