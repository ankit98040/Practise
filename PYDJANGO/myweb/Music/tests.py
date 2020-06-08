#name = ['ankit', 'swarnali', 'sanjukta']
#url=['https://www.facebook.com','https://google.com','https://linkedin.com']
#data = zip(name,url)


class College:
    def __init__(self, name = "RCC"):
        self.id = 2
        self.name = name
        self.contact = 1234

class Students:
    def __init__(self, college, name):
        self.college = college
        self.name = name


col1 = College("ECELL IITR")
col2 = College()
stu1 = Students(name = "pratik", college=col1)
print(stu1.name)

stu2 = Students(name = "ishita", college=col2)
print(stu2.name, stu2.college.name)