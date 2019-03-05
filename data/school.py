import urllib.request
import re

class School:

    def crawlURL_for_school(self, school):
        school = self.titleize_school(school)
        url = "https://www.ratemyprofessors.com/search.jsp?queryBy=schoolId&schoolName=" + school
        # with urllib.request.urlopen(url) as url_data:
        #     html = url_data.read()
        # teacherData = re.findall(r'\">(.*?)</',str(html))
        # output = ''
        # addStuff = 0
        # teacher = None
        # grade = None
        # teacher = teacherData[1]
        # teacher = teacher.split("<title>")[1]
        # teacher = teacher.split(" at ")[0]
        # items = []
        # if(teacher != "Rate My Professors -  Review Teachers and Professors, School Reviews, College Campus Ratings"):
        #     for x in range(len(teacherData)):
        #         temp = self.find_type_of_data(teacherData, x)
        #         if(temp != None):
        #             items.append(temp)
        #         if(len(items) == 3):
        #             break
        #     return teacher, items

    def get_teacher(self):
        print("hi")

    def titleize_school(self, school):
        temp_list = school.split(" ")
        for i in range(len(temp_list)):
            temp_list[i] = temp_list[i].title()
        return "+".join(temp_list)

school = School()
teachers = {}
f = open("teachers.txt", "w+")
temp = school.crawlURL_for_school("brigham young university")
