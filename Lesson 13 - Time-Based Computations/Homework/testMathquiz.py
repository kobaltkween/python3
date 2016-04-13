import unittest
from mathquiz import MathQuiz
from datetime import datetime
import time
import random

class TestMathQuiz(unittest.TestCase):
    
    def setUp(self):
        self.quiz = MathQuiz(testing = True)
    
    def testCreateQuest(self):
        """
        Make sure the question creation method works properly.
        """
        self.quiz.createQuestion()
        expected = "What is the sum of {0} and {1}? ".format(self.quiz.num1, self.quiz.num2)
        self.assertEqual(self.quiz.question, expected, "Question text was incorrect.")
        self.assertEqual(self.quiz.answer, self.quiz.num1 + self.quiz.num2, "The answer should now be the sum of {0} and {1}".format(self.quiz.num1, self.quiz.num2))
    
    def testCheckQuestRight(self):
        """
        Make sure that the correct response to questions is processed properly.
        """
        self.quiz.startTime =  datetime.now()
        time.sleep(1)
        self.quiz.num1 = 1
        self.quiz.num2 = 3
        self.quiz.answer = self.quiz.num1 + self.quiz.num2
        self.quiz.response = "4"
        self.quiz.checkQuestion(1)
        self.assertEqual(self.quiz.responseTime, 1, "Response time is off.")
        self.assertEqual(self.quiz.times[0], self.quiz.responseTime, "Response time not recorded.")
        self.assertEqual(self.quiz.answer, self.quiz.response, "Response not converted to int properly.")
        expected = "Question #1 took about {0} seconds to complete and was right.\n".format(self.quiz.responseTime)
        self.assertEqual(self.quiz.graded, expected, "Graded message incorrect.")

    def testCheckQuestWrong(self):
        """
        Make sure that the wrong response to questions is processed properly.
        """
        self.quiz.startTime =  datetime.now()
        self.quiz.num1 = 1
        self.quiz.num2 = 3
        self.quiz.answer = self.quiz.num1 + self.quiz.num2
        self.quiz.response = "8"
        self.quiz.checkQuestion(1)
        self.assertNotEqual(self.quiz.answer, self.quiz.response, "Response not converted to int properly.")
        expected = "Question #1 took about {0} seconds to complete and was wrong.\n".format(self.quiz.responseTime)
        self.assertEqual(self.quiz.graded, expected, "Graded message incorrect.")
        self.quiz.response = "foo"
        self.quiz.checkQuestion(1)
        self.assertEqual(self.quiz.response, "NaN", "Non-integer response not handled correctly.")
    
    def testAdminQuiz(self):
        """
        Make sure administering the quiz works properly with correct answers.
        """
        self.quiz.adminQuiz()
        self.assertEqual(self.quiz.totalTime, 5, "Each question should have taken 1 second.")
        self.assertEqual(self.quiz.avgTime, 1, "Each question should have taken 1 second to answer.")
        self.assertFalse("wrong" in self.quiz.graded)
        
        
    def testAdminQuizWrong(self):
        """
        Make sure administering the quiz works properly with incorrect answers.
        """
        self.quiz.adminQuiz(answers = ["2", "3", "4", "5", "foo"])
        self.assertTrue("wrong" in self.quiz.graded)
        
    
if __name__ == "__main__":
    unittest.main()
        