#TODO: Write a short note on strategy pattern

class Robot:

    def __init__(self, name):  
        self.name = name
        self.behavior = None

    def behave(self):
        if self.behavior == None: raise Exception("Robot behavior not defined!")
        print("{0}: Based on current position: the behavior object decides the next move".format(self.name))
        self.behavior()
        print("\tThe result returned by behavior object is sent to movement mechanisms for the robot {0}\n".format(self.name))

    def getName(self):  return self.name
        
    def setBehavior(self, func=None):
        if func == None: raise Exception("Behavior function must be defined!")
        self.behavior = func

if __name__ == "__main__":

    def aggressiveBehavior():
        print("\tAgressive Behaviour: if find another robot attack it")

    def defensiveBehavior():
        print("\tDefensive Behaviour: if find another robot run from it")

    def normalBehavior():
        print("\tNormal Behaviour: if find another robot ignore it")

    r1 = Robot("Big Robot")
    r2 = Robot("George v.2.1")
    r3 = Robot("R2")

    # check for error raised
    try: 
        r2.behave()
    except Exception as e:
        print(e)
        print("... continuing to check for other behavior")
    
    r1.setBehavior(aggressiveBehavior)
    r2.setBehavior(normalBehavior)
    r3.setBehavior(defensiveBehavior)
   
    print("--------------------------")
    r1.behave()
    r2.behave()
    r3.behave()
   
    # change the behaviors of each robot
    r1.setBehavior(normalBehavior)
    r2.setBehavior(defensiveBehavior)
    r3.setBehavior(aggressiveBehavior)
   
    print("--------------------------")
    r1.behave()
    r2.behave()
    r3.behave()
