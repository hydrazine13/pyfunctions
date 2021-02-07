''' this function returns new string with each character rotated by integer rot.
    example - string "cheer" returns "jolly" when rotated by rot = 7 '''


def rotate(string, rot):
    newstring = ""
    rot = int(rot)
    rot = rot%26
    for i in range(len(string)):
        letter = string[i]
        if (ord(letter) >= 65 and ord(letter) <= 90):
            startchar = 'A'
        else:
            startchar = 'a'
        change = ord(letter) - ord(startchar) + rot
        change = change%26
        change = change + ord(startchar)
        change = chr(change)
        newstring = newstring + change
    return newstring
