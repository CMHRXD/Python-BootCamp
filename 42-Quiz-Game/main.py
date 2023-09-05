
from replit import clear
from time import sleep
from question_model import QuestionModel as QuestionBuilder
from quiz_brain import QuizBrain
from data import question_data 


questionList = []

def init():
  for question in question_data:
    questionList.append(QuestionBuilder(question["text"], question["answer"]))
  
  # initialize the quiz
  quiz = QuizBrain(questionList)
  quiz.nextQuestion()
  
  while quiz.nextQuestion():
    sleep(3)
    clear()
  
init()