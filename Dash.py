mapx = 10; mapy = 100 ;running = True; level = {}
columncmd=["C","COLUMN","COL"];rowcmd=["R","ROW"];helpcmd=["H","HELP","HEL"];alldecor=["ALL","A"]
for x in range(mapx): level[x]="-"*mapy
exec("def printscreen():\n print('')\n for x in level: print(level[x])\n print('')")
def hasNumbers(inputString): return bool(any(x in "1234567890" for x in inputString))
sel_r = 0; sel_c = 0
def editlevel():
    for x in range(mapx):
        if x is sel_r: level[x]='='*(mapy-1-sel_c)+'+'+'='*(sel_c)
        else: level[x]='-'*(mapy-1-sel_c)+'|'+'-'*(sel_c)
while running:
    printscreen(); inpt = input()
    if inpt.capitalize() == "x".capitalize(): running = False
    elif any(x in helpcmd for x in inpt.upper()):
        if any(x in rowcmd for x in inpt.upper()): print("Use the ROW command to change your selected row coordinate.\n Example: r4 would set your selected row to 4.")
        elif any(x in columncmd for x in inpt.upper()): print("Use the COLUMN command to change your selected column coordinate.\n Example: c52 would set your selected row to 52.")
        elif any(x in alldecor for x in inpt.upper()): print("All Dash Commands:\n - ROW (#): Change selected row to #.\n - COLUMN (#): Change selected column to #.")
        else: print("Use the HELP command to get descriptions of other commands. Use HELP ALL or ha to see a list of commands.")
    elif any(x in rowcmd for x in inpt.upper()):
        if hasNumbers(inpt): exec("for x in range(mapx):\n if str(x) in inpt: sel_r = x-1")
        else:
            print('Current Row: ' + str(sel_r+1))
            if any(x in columncmd for x in inpt.upper()): print('Current Column: ' + str(sel_c+1))
    elif any(x in columncmd for x in inpt.upper()):
        if hasNumbers(inpt):
            found = False
            for x in reversed(range(mapy)): exec('if str(x) in inpt and found == False: sel_c = x-1; found = True')
        else:
            print("Current Column: " + str(sel_c+1))
            if any(x in rowcmd for x in inpt.upper()): print("Current Row: " + str(sel_r+1))
    editlevel()
