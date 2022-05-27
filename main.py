class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):

        self.name = "Tunde"
        self.age = 25
        self.track = "fullstack"
        self.score = 99.9
        pass
    def speak(self):
        print("My name is ", self.name, "and I and my age is ", self.age, "and my track is ", self.track, "with the score of ", self.score)
    
    def edit_profile(self, change_name, change_age, change_track, get_score):
        self.change_name = str(input("Input your new name here: "))
        self.change_age = int(input("Input your new age here: "))
        self.chage_track = str(input("Input your new track here:"))
        self.get_score = 99.9
        print("Student name =",self.change_name, "age =", self.change_age, "track =", self.chage_track, "score =", self.chage_score)
        
