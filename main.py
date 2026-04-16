from pyscript import document, display

# class
class Classmate:
    def __init__(self, name, section, favorite_subject): 
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject
    # introduce() method
    def introduce(self):
        display(f'Hi, I am {self.name} from section {self.section} and my favorite subject is {self.favorite_subject}', target='output')

# dictionary
classmates_list = [
    Classmate("Kaitlyn Nardo", "Ruby", "PE"),
    Classmate("Jade Cabitigan", "Ruby", "Math"),
    Classmate("Enzo Villeges", "Ruby", "PE"),
    Classmate("Tar Canete", "Ruby", "Science"),
    Classmate("Koby Baylonz", "Topaz", "TLE")
]

# add classmate
def add_classmate(e):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    if name and section and subject:
        new_student = Classmate(name, section, subject)
        classmates_list.append(new_student)

        # clears previuos message
        document.getElementById("output").innerHTML = ""
        display(f"{new_student.name} added successfully!", target="output")

        # for new studnet
        document.getElementById("name").value = ""
        document.getElementById("section").value = ""
        document.getElementById("subject").value = ""

# output
def introduce(e):
    document.getElementById("output").innerHTML = ""
    
# introuce() 
    for person in classmates_list:
        person.introduce()