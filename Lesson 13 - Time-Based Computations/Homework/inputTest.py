import time
import random


def testLoop(testing = False, response = []):
    for count in range(5):
        if testing:
            answer = response[count]
            time.sleep(1 + random.random())
        else:
            answer = input("Say anything: ")
        print(answer)
    
if __name__ == "__main__":
    testLoop(testing = True, response = ["test1", "test2", "test3", "test4", "test5"])
    