class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(this, name, age, tracks, score):
        this.name = str(name)
        this.age = int(age)
        this.tracks = list(tracks)
        this.score = float(score)
        
    def change_name(this, name):
        this.name = str(name)
        print(this.name)

    def change_age(this, age):
        this.age = int(age)
        print(this.age)

    def add_track(this, track):
        this.tracks.append(str(track))
        print(this.tracks)

    def get_score(this):
        print(this.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age('34')
Bob.add_track("UI/UX")
Bob.get_score()
 