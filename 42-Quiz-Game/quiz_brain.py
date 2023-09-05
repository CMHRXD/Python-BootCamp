
class QuizBrain:
  def __init__(self, question_list):
    self.question_number = 0
    self.question_list = question_list
    self.score = 0
  
  def nextQuestion(self):
    if len(self.question_list) > self.question_number:
      
      question = self.question_list[self.question_number]
      self.question_number+=1
      guess = input(f"Q.{self.question_number}: {question.text}. ('True' or 'False') ?").lower()
      
      self.checkAnswer(guess,question.answer )
      return self.keepPlaying()
      
    else:
      print("You reach the end of the Quiz")
      return False
    
  def keepPlaying(self):
    option = input("Do you want to keep playing? ('y' or 'n') ?")
    if option == "y":
      return True
    else:
      return False
  
  def checkAnswer(self, guess, answer):
    if guess == answer.lower():
      self.score+=1
      print(f"You guess rigth") 
      print("Your current score is: ", self.score)
      return True
    else:
      print("The correct answer is: ", answer)
      print("Your current score is: ", self.score)
  