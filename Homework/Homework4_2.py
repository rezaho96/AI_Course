from abc import ABC ,abstractmethod
from enum import Enum
class OfficialEmployment(ABC):
    def __init__(self,name,family,nationalCode,major,address):
        self._name=name
        self._family=family
        self._nationalCode=nationalCode
        self._major=major
        self._address=address
    @abstractmethod
    def score_calculation(self):
        pass
#........................................
class FreeParticipant(OfficialEmployment):
    def __init__(self, name, family, nationalCode, major, address, interviewScore, writtenScore):
        super().__init__(name, family, nationalCode, major, address)
        self.__interviewScore=interviewScore
        self.__writenScore=writtenScore
    @property
    def interviewScore(self):
        return self.__interviewScore
    @interviewScore.setter
    def interveiwScore(self,interviewScore):
        self.__interviewScore=interviewScore
    @property
    def writtenScore(self):
        return self.__writenScore
    @writtenScore.setter
    def writenScore(self,writenScore):
        self.__writenScore=writenScore
    def score_calculation(self):
        return  (self.__interviewScore+self.__writenScore)/2
    
    def showInfo(self):
       return f"name is :{self._name} / family is: {self._family} / naational code is : {self._nationalCode} / major is: {self._major} / address is: {self._address} / final score is:{self.score_calculation()}"
#........................................
    
class EliteScholar(OfficialEmployment):
    def __init__(self, name, family, nationalCode, major, address, GPA, universityRankingScore):
        super().__init__(name, family, nationalCode, major, address)
        
        if 16<=GPA<17.5:
            self.__GPA=60
        elif 17.5<=GPA<18.5:
            self.__GPA=80
        elif 18.5<=GPA<=20:
            self.__GPA=100
        
        self.__universityRankingScore=universityRankingScore
    @property
    def univercityRankingScore(self):
         return self.__universityRankingScore
    @univercityRankingScore.setter
    def univercityRankingScore(self,univercityRankingScore):
        self.__universityRankingScore=univercityRankingScore
    def score_calculation(self):
        return (self.__GPA+self.__universityRankingScore)/2
    
    def showInfo(self):
       return f"name is :{self._name} / family is: {self._family} / naational code is : {self._nationalCode} / major is: {self._major} / address is: {self._address} / final score is:{self.score_calculation()}"
#//////////////////////
class UniversityRankingScore(Enum):
    rank1=100
    rank2=80
    rank3=60
#........................................

class ContractualEmployee(OfficialEmployment):
    def __init__(self, name, family, nationalCode, major, address, averagePerformanceScore, workExperience):
        super().__init__(name, family, nationalCode, major, address)
        self.__averagePerformanceScore=averagePerformanceScore
        self.__workExperience=workExperience
        
        if 1<=self.__workExperience<=5:
            self.__workExperienceCoefficient=.1
        elif self.__workExperience>5:
            self.__workExperienceCoefficient=.2
        
    @property
    def averagePerformanceScore(self):
        return self.__averagePerformanceScore
    @averagePerformanceScore.setter
    def averagePerformanceScore(self,averagePerformanceScore):
        self.__averagePerformanceScore=averagePerformanceScore
    @property
    def workExperience(self):
        return self.__workExperience
    @workExperience.setter
    def workExperience(self,workExperience):
        self.__workExperience=workExperience
    def score_calculation(self): 
        return self.__averagePerformanceScore+(self.__workExperienceCoefficient*self.__averagePerformanceScore)
    
    def showInfo(self):
       return f"name is :{self._name} / family is: {self._family} / naational code is : {self._nationalCode} / major is: {self._major} / address is: {self._address} / final score is:{self.score_calculation()}"

# --------------------main-------------------------
freeParticipant1=FreeParticipant("ali","ghorbani",546897285,"ensani","shiraz_taleghani",80,50)
eliteScholar1=EliteScholar("reza","hoseini",548742215,"riazi","tehran_gharb",18.7,UniversityRankingScore.rank1.value)
contractualEmployee1=ContractualEmployee("mohamad","velayati",24361598,"tajrobi","mashhad_karimkhan",90,6)
list_participants=[freeParticipant1,eliteScholar1,contractualEmployee1]
list_accepted=[]
for participants in list_participants:
    if participants.score_calculation()>90:
        list_accepted.append(participants.showInfo())
print(f"list accepted is: {list_accepted}")
