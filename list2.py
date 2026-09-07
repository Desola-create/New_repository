def emotions(): 
    emotions = ["happy", "sad", "angry", "excited"]
    print("*****************************************")
    print("total number of emotions:", len(emotions))
    print("*****************************************")
    a=100
    b=20.1
    print("Type of a:", type(a))
    print("Type of b:", type(b))

    print("***************************************")
    for feelings in emotions:
        print(feelings) 

    print("***************************************")
    print(type(emotions))

    print("*******************************************")
    emotions[1] = "confused"
    for feelings in emotions:
        print(feelings)

    print("*******************************************")
    emotions.append("nervous")
    for feelings in emotions:
     print(feelings)

    print("*******************************************")
    print("total number of emotions:", len(emotions))

    emotions_set = set(emotions)

def list_example():
   emotions()

def set_example():
   pass

def tuple_example():
   pass

def dictionary_example():
   pass

def start():
   pass

if __name__ == "__main__":
    emotions()