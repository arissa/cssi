
import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))


class QuizQuestion(object):
  def __init__(self, question, guess, correct):
    self.question = question
    self.guess = guess
    self.correct = correct
  def IsQuestionCorrect(self):
    return self.guess == self.correct

class MainHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = jinja_environment.get_template('hello.html')
    self.response.out.write(template.render(template_values))

class QuizHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {'name' : self.request.get('name')}
    template = jinja_environment.get_template('quiz.html')
    self.response.out.write(template.render(template_values))

class GradeQuizHandler(webapp2.RequestHandler):
  def get(self):
    wrong_answers = []
    addition_guess = self.request.get('addition')
    capital_guess = self.request.get('capital')
    addition_question = QuizQuestion('What is 3 + 4?', addition_guess, '7')
    capital_question = QuizQuestion('What is the capital of California?', capital_guess.lower(), 'sacramento')
    if not addition_question.IsQuestionCorrect():
      wrong_answers.append(addition_question)
    if not capital_question.IsQuestionCorrect():
      wrong_answers.append(capital_question)
    if wrong_answers:
      success_message = 'fail'
    else:
      success_message = 'pass'

    template_values = {
    'wrong_answers':wrong_answers, 
    'name': self.request.get('name'),
    'success_message':success_message}

    template = jinja_environment.get_template('grade_quiz.html')
    self.response.out.write(template.render(template_values))

routes = [('/', MainHandler),('/quiz', QuizHandler), ('/grade_quiz', GradeQuizHandler)]

app = webapp2.WSGIApplication(routes, debug=True)
