import urllib.request
import re

class Main:
    percent_found = False

    def find_type_of_data(self, teacherData, x):
        if(('\\r\\n                  ' in teacherData[x]) and ('%' in teacherData[x]) and (not self.percent_found)):
            item = teacherData[x].split("\\r\\n")[1]
            item = item.strip()
            item = item.split("None")[0]
            self.percent_found = True
            return item
        elif('<div class="grade" title="">' in teacherData[x]):
            item = teacherData[x].split('<div class="grade" title="">')[1]
            if('\\r\\n' in item):
                item = item.split("\\r\\n")[1]
                item = item.strip()
            return item

    def crawlURL(self, addedURL):
        url = addedURL
        with urllib.request.urlopen(url) as url_data:
            html = url_data.read()

        teacherData = re.findall(r'\">(.*?)</',str(html))
        output = ''
        addStuff = 0
        teacher = None
        grade = None
        teacher = teacherData[1]
        teacher = teacher.split("<title>")[1]
        teacher = teacher.split(" at ")[0]
        items = []
        if(teacher != "Rate My Professors -  Review Teachers and Professors, School Reviews, College Campus Ratings"):
            for x in range(len(teacherData)):
                temp = self.find_type_of_data(teacherData, x)
                if(temp != None):
                    items.append(temp)
                if(len(items) == 3):
                    break
            return teacher, items

main = Main()
total = {}
f = open("temp.txt", "w+")
for i in range(916674):
    temp = main.crawlURL('http://www.ratemyprofessors.com/ShowRatings.jsp?tid='+str(i)+'')
    if(temp != None):
        total[temp[0]] = temp[1]
        temp_list_string = ""
        for item in temp[1]:
            temp_list_string += item + " "
        f.write(temp[0] + " " + temp_list_string + "\n")
print(total)
