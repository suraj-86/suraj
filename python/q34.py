#waf to find in which line does word "learning" occur first.

def check_word():
    data = True
    line=1
    word="learning"
    with open("Practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print("found in ",line," line")
                return
            line+=1
    return -1

check_word()

