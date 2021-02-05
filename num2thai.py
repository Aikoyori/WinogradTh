singlenumlist = ["ศูนย์","หนึ่ง","สอง","สาม","สี่","ห้า","หก","เจ็ด","แปด","เก้า"]
oneslist = ["","เอ็ด","สอง","สาม","สี่","ห้า","หก","เจ็ด","แปด","เก้า"]
tenslist = ["","","ยี่","สาม","สี่","ห้า","หก","เจ็ด","แปด","เก้า"]
genericlist = ["","หนึ่ง","สอง","สาม","สี่","ห้า","หก","เจ็ด","แปด","เก้า"]
placeslist = ["","สิบ","ร้อย","พัน","หมื่น","แสน"]
millionword = "ล้าน"
negativeword = "ลบ"
dotword = "จุด"
percentword = "เปอร์เซ็นต์"

def num2thai(num):
    numstr = str(num)
    numstr.replace(",","")
    percent = (numstr[-1]=="%")
    if(percent):
        numstr=numstr[:-1]

    negate = numstr[0]=="-"
    if negate:
        numstr = numstr[1:]
    dottedsplitter = numstr.split(".")
    finalstring=negativeword if negate else ""

    for enumdot,dotsections in enumerate(dottedsplitter):
        if(enumdot==0):
            numstrnormal = dotsections
            if(len(dotsections)==1):
                finalstring+=singlenumlist[int(numstrnormal)]
            else:   
                numstreverse = numstrnormal[::-1]
                numwindex = list(enumerate(numstreverse))[::-1]
                    
                numsections = [numwindex[::-1][i:i+6:][::-1] for i in range(0, len(numwindex), 6)][::-1]
                
                for secionnum,sections in enumerate(numsections):
                    for digit,number in sections:
                        number = int(number)
                        if(digit%6==0):
                            finalstring+=oneslist[number]+placeslist[digit%6]
                        elif(digit%6==1):
                            finalstring+=tenslist[number]+placeslist[digit%6]
                        else:
                            finalstring+=genericlist[number]+placeslist[digit%6]
                    finalstring+="" if secionnum == len(numsections)-1 else millionword
        else: 
            for char in dotsections:
                finalstring+=singlenumlist[int(char)]
        finalstring+=dotword if enumdot < len(dottedsplitter)-1 else ""
    if(percent):
        finalstring+=percentword
    return finalstring
