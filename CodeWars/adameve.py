class Human(object):
    type="Human"
class Man(Human):
    gender="Man"#male
class Woman(Human):
    gender="Woman" #female
def God():
    paradise=[]
    paradise.append(Man())
    paradise.append(Woman())
    return paradise