class Event:

    def __init__(self):
        print("hello world")

    ''' Basically this need to be able to read a dictionary
    and determine what kind of calculation to perform based
    on what type of event it will be. What type of modifier
    it actually is. Does it roll a dice set. Does it directly
    modified the existing value. Does it add to the value,
    or multiply it? Is there a condition that has to be met?
    All good questions...'''

    def calculate(self, value):
        print("do nothing")
