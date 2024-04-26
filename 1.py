import fileinput 
import re

input = fileinput.input(files ='day1.txt')
result = 0

words = ["nollanvändesintrtrorjag", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def partone():

    for line in input:
        res = ""
        for char in line:
            if char.isdigit():
                res = str(char)
                break
        for char in line[::-1]:
            if char.isdigit():
                res += str(char)
                break
        result += int(res)
    return result


def f(s):
    oldchar = ''
    groups = []
    letters = ''
    for char in s.strip():
        if char.isdigit():
            if letters:
                groups.append(letters.strip())
            groups.append(char)
            letters = ''
        else:
            letters = letters + char
    if letters:
        groups.append(letters.strip())
    return groups

def parttwo():
    result = 0
    for line in input:
        res = ""
        found = False
        for i in f(line):
            if i.isdigit():
                res = str(i)
                break
            else:
                foundwords = [word for word in words if word in i]
                prevhigh = 999999999999999
                prevword = ''
                if foundwords:
                    for word in foundwords:
                        if i.find(word) < prevhigh:
                            prevhigh = i.find(word)
                            prevword = word
                    res = res + str(words.index(prevword))
                    break
        for i in f(line)[::-1]:

            if i.isdigit():
                res = res + str(i)
                break
            else:
                foundwords = [word for word in words if word in i]
                prevhigh = -1
                prevword = ''
                if foundwords:
                    for word in foundwords:
                        if i.rindex(word) > prevhigh:
                            prevhigh = i.rindex(word)
                            prevword = word
                    res = res + str(words.index(prevword))
                    break
        result += int(res)

    return result


print(parttwo())