class Programming_Language_Course:
    def __init__(self, courseCode , startOfCourse , endOfCourse , courseFee , courseStructor ,courseLevel ):
        self.__courseCode=courseCode
        self._startOfCourse=startOfCourse
        self._endOfCourse=endOfCourse
        self._courseFee=courseFee
        self._courseStructor=courseStructor
        self._courseLevel =courseLevel 
        self._courseDays=[]
        self.dicShow={"Course_Code is":self.__courseCode}
    def _showInfo(self):
        return self.dicShow
    def add_Days(self,day):
         self._courseDays.append(day)
    @property
    def courseCode(self):
        return self.__courseCode
    @courseCode.setter
    def courseCode(self,courseCode):
        self.__courseCode= courseCode    
#//////////////////////////////
class Python(Programming_Language_Course):
    def __init__(self, courseCode , startOfCourse , endOfCourse , courseFee , courseStructor,courseLevel  ):
        super().__init__(courseCode,startOfCourse,endOfCourse,courseFee,courseStructor,courseLevel )
        self.dicPythonShow={"start of python course is":self._startOfCourse,"end of python course is":self._endOfCourse, "python course Fee is":self._courseFee,"python course structor is":self._courseStructor,"python course days is":self._courseDays,"course level is": self._courseLevel}
        self.dicShow.update(self.dicPythonShow)
    def showInfoPythonCourse(self):
        return self.dicShow
#//////////////////////////////
class Java(Programming_Language_Course):
    def __init__(self, courseCode , startOfCourse , endOfCourse , courseFee , courseStructor ,courseLevel):
        super().__init__(courseCode,startOfCourse,endOfCourse,courseFee,courseStructor,courseLevel)
        self.dicJavaShow={"start of java course is":self._startOfCourse,"end of java course is":self._endOfCourse, "java course Fee is":self._courseFee,"java course structor is":self._courseStructor,"java course days is":self._courseDays,"course level is": self._courseLevel}
        self.dicShow.update(self.dicJavaShow)
    def showInfoJavaCourse(self):
        return self.dicShow
#//////////////////////////////
class PHP(Programming_Language_Course):
    def __init__(self, courseCode , startOfCourse , endOfCourse , courseFee , courseStructor,courseLevel ):
        super().__init__(courseCode,startOfCourse,endOfCourse,courseFee,courseStructor,courseLevel)
        self.dicPHPshow={"start of PHP course is":self._startOfCourse,"end of PHP course is":self.   _endOfCourse, "PHP course Fee is":self._courseFee,"PHP course structor is":self._courseStructor,"PHP   course days is":self._courseDays,"course level is": self._courseLevel}
        self.dicShow.update(self.dicPHPshow)
    def showInfoPHPcourse(self):
        return self.dicShow
#////////////////////////////
p1=Python(2345,"1400/6/25","1400/9/3",2500,"mahdavi","Basic_level")
p1.add_Days("sunday")
p1.add_Days("tuesday")
p1.add_Days("wendesday")
p2=Python(3642,"1400/9/5","1400/12/20",3000,"mahdavi","ََAdvanced_level")
p2.add_Days("sunday")
p2.add_Days("tuesday")
p2.add_Days("wendesday")
j1=Java(5120,"1401/1/5","1401/2/3",2000,"karimi","Basic_level")
j1.add_Days("saturday")
j1.add_Days("sunday")
j1.add_Days("monday")
j2=Java(1245,"1401/2/5","1401/3/3",2200,"karimi","Advanced_level")
j2.add_Days("saturday")
j2.add_Days("sunday")
j2.add_Days("monday")
php1=PHP(2580,"1401/1/15","1401/3/15",5000,"ghodosi","Basic_level")
php1.add_Days("sunday")
php1.add_Days("tusesday")
php1.add_Days("wendesday")
php1.add_Days("thursday")
php2=PHP(2131,"1401/3/16","1401/4/3",5500,"ghodosi","Advanced_level")
php2.add_Days("sunday")
php2.add_Days("tusesday")
php2.add_Days("wendesday")
php2.add_Days("thursday")
list_show=[p1.showInfoPythonCourse(),p2.showInfoPythonCourse(),j1.showInfoJavaCourse(),j2.showInfoJavaCourse(),php1.showInfoPHPcourse(),php2.showInfoPHPcourse()]
for course in list_show:
    print(course,"\n")
