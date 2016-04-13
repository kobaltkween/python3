"""
Simple five question math quiz which times and checks each question.
"""
from datetime import datetime, timedelta
import random
import time

class MathQuiz:
    
    def __init__(self, testing = False):
        """
        Set the number of questions in the quiz, set the testing mode toggle,
        and initialize the grading response string and times.
        """
        self.testing = testing
        self.numQuest = 5
        self._times = []
        self._graded = ""  
    
    @property
    def times(self):
        return self._times
    
    @times.setter
    def times(self, value):
        """
        Times shouldn't be able to be changed outside the class.
        """
        raise AttributeError("You cannot manually change the times.")
    
    @property
    def graded(self):
        return self._graded
    
    @graded.setter
    def graded(self, value):
        """
        Grading shouldn't be able to be changed outside the class.
        """
        raise AttributeError("You cannot manually change the grading.")
    
    def createQuestion(self):
        """
        Create a simple addition problem of two integers between 1 and 10
        """
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.question = "What is the sum of {0} and {1}? ". format(self.num1, self.num2)
        self.answer = self.num1 + self.num2
    
    def checkQuestion(self, questNum):
        """
        Take in the question number, check the user response against the answer,
        figure out how long it took to answer the question, and record the time
        and the "grade" info regarding the time and correctness of the response.
        """
        endTime = datetime.now()
        self.responseTime = round((endTime - self.startTime).seconds)
        self._times.append(self.responseTime)
        try: 
            self.response = int(self.response)
        except ValueError:
            self.response = "NaN"
        if  self.response == self.answer:
            grade = "right"
        else: 
            grade = "wrong"
        fullGrading = "Question #{0} took about {1} seconds to complete and was {2}.\n".format(questNum, self.responseTime, grade)
        self._graded += fullGrading
        if not self.testing:
            print("{0} is {1}!".format(self.response, grade))

    def adminQuiz(self, answers = []):
        """
        Administer five question quiz, which uses either user input
        or a list of answers (if testing for proper handling of 
        incorrect answers). 
        """
        for count in range(self.numQuest):
            self.createQuestion()
            self.startTime = datetime.now()
            if self.testing:
                time.sleep(1)
                if answers:
                    self.response = answers[count]
                else:
                    self.response = self.answer
            else:
                self.response = input(self.question)
            self.checkQuestion(count + 1)
        self.totalTime = sum(self.times)
        self.avgTime = self.totalTime / self.numQuest
        if not self.testing:
            self._graded += "You took {} seconds to finish the quiz.\n".format(self.totalTime)
            self._graded += "Your average time was {} seconds per question.".format(self.avgTime)
            print(self.graded)
        

if __name__ == "__main__":
    q = MathQuiz()
    q.adminQuiz()