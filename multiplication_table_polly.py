#!/usr/local/bin/python3
import os, boto3
import sys

defaultRegion = 'eu-west-1'
defaultUrl = 'https://polly.'+ defaultRegion +'.amazonaws.com'
defaultTmpDir = os.getcwd() + "/tmp"

def connectToPolly(regionName=defaultRegion, endpointUrl=defaultUrl):
    return boto3.client('polly', region_name=regionName, endpoint_url=endpointUrl)

def speak(polly, text, format='mp3', voice='Joanna'):
    resp = polly.synthesize_speech(OutputFormat=format, Text=text, VoiceId=voice)
    soundfile = open(defaultTmpDir + '/speech.mp3', 'wb')
    soundBytes = resp['AudioStream'].read()
    soundfile.write(soundBytes)
    soundfile.close()
    os.system('afplay '+ defaultTmpDir +'/speech.mp3')  # Works only on Mac OS, sorry
    os.remove(defaultTmpDir + '/speech.mp3')

polly = connectToPolly()
# L'opérateur m'a donné un nombre a multiplier
speak(polly, "Which number should I multiply ?")
number = int(input('Which number should I multiply ?\n'))

speak(polly, "Allright, let's multiply " + str(number) + ' !')

# Je crée une boucle pour calculer la table de multiplication de 1 à 10 pour ce nombre
for multiplier in range(1,11):
    # Cette instruction écrit la multiplication du nombre par un multiplicateur de 1 à 10 dans la console
    speak(polly, str(number) + " times " + str(multiplier) + " equals " + str(number*multiplier))
    print(number,'x',multiplier,'=',number*multiplier)