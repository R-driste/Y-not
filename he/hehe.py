#PUBLIC: name, age, status, bio, social

def getPublicUser(fname, lname, username, age, status, bio, social, id):
    getId = newId()
    return {'first-name':fname,
            'last-name':lname,
            'username':username,
            'age':age,
            'status': status,
            'bio':bio,
            'social':social,
            'id': getId}

def getPrivateUser(contact, password, id):
    return {'contact':contact,
            'password':password,
            'id':id}

def updateAge(col, attribute, id):
    fil = {'id':id}
    atr = {'age':attribute}
    col.update_one(filter=fil,atr=atr)

def updateCoord(col, lat, lng, id):
    fil = {'id': id}
    newvalues = { "$set": { 'coord': [lat, lng] } }
    col.update_one(fil, newvalues)

def newId():
    currentId = 0
    with open("C:/Users/stidr/Y not/he/ID.txt","r+") as f:
        currentId = int(f.read())
        f.seek(0)
        f.write(str(currentId+1))
        f.truncate()

    return currentId