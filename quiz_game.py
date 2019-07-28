import tkinter
import random


class QuizGame():
    def __init__(self):
        self.window = tkinter.Tk()
        self.label1 = tkinter.Message(self.window,text = 'Quiz Game',width = 200)
        self.label2 = tkinter.Message(self.window,text = 'question',width = 200)
        self.a = tkinter.Button(master = self.window,text = 'General Knowledge',command = self.answer_a,height = 5,width = 35)
        self.b = tkinter.Button(master = self.window,text = 'Sports',command = self.answer_b,height = 5, width = 35)
        self.c = tkinter.Button(master = self.window,text = 'Food',command = self.answer_c,height = 5,width = 35)
        self.d = tkinter.Button(master = self.window,text = 'Geography',command = self.answer_d,height = 5,width = 35)
        self.next = tkinter.Button(master = self.window,text = 'Next',command = self.next,height = 5,width = 35)
        self.questions,self.answers,self.correct_ans = [],[],[]
        self.question_num = ['Question 1','Question 2','Question 3','Question 4']
        self.num = 0
        
    def run(self):
        self.label1.pack()
        self.label2.pack()
        self.a.pack()
        self.b.pack()
        self.c.pack()
        self.d.pack()
        self.next.pack()
        self.window.mainloop()
        
    def next(self):
        if len(self.questions) == 0 and self.next['text'] != 'Reset':
            self.label2.config(text = 'Total Score: {}'.format(self.score()))
            self.next.config(text = 'Reset')
            return
        if self.next['text'] == 'Reset':
            self.reset()
            return
        self.label1.config(text = self.question_num[0])
        del self.question_num[0]
        self.label2.config(text = self.questions[0][0])
        self.a.config(text=self.questions[0][1])
        self.b.config(text=self.questions[0][2])
        self.c.config(text=self.questions[0][3])
        self.d.config(text=self.questions[0][4])
        del self.questions[0]
        self.num += 1
        
        
    def reset(self):
        self.questions,self.answers,self.correct_ans = [],[],[]
        self.question_num = ['Question 1','Question 2','Question 3','Question 4']
        self.a.config(text = 'General Knowledge')
        self.b.config(text = 'Sports')
        self.c.config(text = 'Food')
        self.d.config(text = 'Geography')
        self.next.config(text = 'Next')
        self.label2.config(text = 'question')
      
    def answer_a(self):
        if self.num == 0 and len(self.questions) != 0:
            self.questions = []
            self.generate_questions('General Knowledge')
        elif self.a['text'] == 'General Knowledge':
            self.generate_questions('General Knowledge')
        elif len(self.answers) == self.num:
            self.answers[self.num-1] = self.a['text']
        elif self.a['text'] not in self.answers:
            self.answers.append(self.a['text'])
        
    def answer_b(self):
        if self.num == 0 and len(self.questions) != 0:
            self.questions = []
            self.generate_questions('Sports')
        elif self.b['text'] == 'Sports':
            self.generate_questions('Sports')
        elif len(self.answers) == self.num:
            self.answers[self.num-1] = self.b['text']
        elif self.b['text'] not in self.answers:
            self.answers.append(self.b['text'])
            
    def answer_c(self):
        if self.num == 0 and len(self.questions) != 0:
            self.questions = []
            self.generate_questions('Food')
        elif self.c['text'] == 'Food':
            self.generate_questions('Food')
        elif len(self.answers) == self.num:
            self.answers[self.num-1] = self.c['text']
        elif self.c['text'] not in self.answers:
            self.answers.append(self.c['text'])
            
    def answer_d(self):
        if self.num == 0 and len(self.questions) != 0:
            self.questions = []
            self.generate_questions('Geography')
        elif self.d['text'] == 'Geography':
            self.generate_questions('Geography')
        elif len(self.answers) == self.num:
            self.answers[self.num-1] = self.d['text']
        elif self.d['text'] not in self.answers:
            self.answers.append(self.d['text'])
        
    def generate_questions(self,subject):
        if subject == 'General Knowledge':
            self.subject1()
        elif subject == 'Sports':
            self.subject2()
        elif subject == 'Food':
            self.subject3()
        elif subject == 'Geography':
            self.subject4()
                
    def subject1(self):
        question_file = open('questions.txt','r')
        file_questions = question_file.readlines()
        question_file.close()
        question_lines = random.sample(range(0,20),4)
        for i in question_lines:
            line = file_questions[i].strip().split(';')
            self.questions.append([line[0],line[1],line[2],line[3],line[4]])
            self.correct_ans.append(line[5])
            
    def subject2(self):
        question_file = open('questions.txt','r')
        file_questions = question_file.readlines()
        question_file.close()
        question_lines = random.sample(range(21,30),4)
        for i in question_lines:
            line = file_questions[i].strip().split(';')
            self.questions.append([line[0],line[1],line[2],line[3],line[4]])
            self.correct_ans.append(line[5])
            
    def subject3(self):
        question_file = open('questions.txt','r')
        file_questions = question_file.readlines()
        question_file.close()
        question_lines = random.sample(range(31,38),4)
        for i in question_lines:
            line = file_questions[i].strip().split(';')
            self.questions.append([line[0],line[1],line[2],line[3],line[4]])
            self.correct_ans.append(line[5])
            
    def subject4(self):
        question_file = open('questions.txt','r')
        file_questions = question_file.readlines()
        question_file.close()
        question_lines = random.sample(range(39,53),4)
        for i in question_lines:
            line = file_questions[i].strip().split(';')
            self.questions.append([line[0],line[1],line[2],line[3],line[4]])
            self.correct_ans.append(line[5])
            
    def score(self):
        total = 0
        for ans,cor_ans in zip(self.answers,self.correct_ans):
            if ans == cor_ans:
                total += 1
        return total
        
            
            
            
    
game = QuizGame()
game.run()
    
