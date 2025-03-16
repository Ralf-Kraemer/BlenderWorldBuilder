import sys
import os
import random

print("Hi there!")
print("Input start")
startID = int(input())
print("Input end")
endID = int(input())
print("Input minimum step size")
minStepSize = int(input())
print("Input maximum step size")
maxStepSize = int(input())

currentID = startID

while currentID <= endID:
    print(currentID)
    foo = hex(currentID)
    bar = foo.replace("0x", "")
    
    if len(bar) == 0:
        print("missing input")
    elif len(bar) == 1:
        bar = "0" + bar
    elif len(bar) >= 2:
        bar = "" + bar
        
    print(bar)
    os.system("/Applications/Blender.app/Contents/MacOS/blender -b -P ./run.py ./input/template.blend " + bar)
    currentID = currentID + random.randrange(minStepSize, maxStepSize)
    
if currentID >= endID:
    print("Done.")