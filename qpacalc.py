import tkinter as tk
from tkinter import ttk
from collections import defaultdict
course_temp = 0


class Application(tk.Frame):
  course_temp = 0
  names = {}
  len_menu = {}
  wei_menu = {}
  lengths = {} 
  weights = {}
  grades = {}

  output = None
  calc_button = None

  credits_now = None
  qpa_now = None
  def __init__(self, master):
    self.master = master
    tk.Frame.__init__(self, self.master)
    self.configure_gui()
    self.create_widgets()


  def configure_gui(self):
    self.master.title("QPA Calculator")  

      
  def create_widgets(self):
    tk.Label(self.master, text = "Current Credits").grid(row = 1, column = 0) 
    tk.Label(self.master, text = "Current QPA").grid(row = 0, column = 0)
    tk.Label(self.master, text = "How many courses would you like to factor in?").grid(row = 2, column = 0)

    self.qpa_now = tk.StringVar() # stores student's current QPA in an entry box
    qn_entry = tk.Entry(self.master, textvariable = self.qpa_now) # current QPA entry box
    qn_entry.grid(row = 0, column = 1)

    self.credits_now = tk.StringVar() # stores student's current credits
    cn_entry = tk.Entry(self.master, textvariable = self.credits_now) # current credits entry box
    cn_entry.grid(row = 1, column = 1)

    course_num = tk.StringVar(self.master) # stores number of courses for drop down menu
    course_num.set("0")
    course_num.trace("w", lambda var_name, var_index, operation: self.courselist(course_num)) # calls courselist function everytime dropdown option is changed
    num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10'] 
    tk.OptionMenu(self.master, course_num, *num_list).grid(row = 2, column = 1) # drop down that controls how many courses are shown

  def get_course_number(self, course_num):
    return int(course_num.get()) 

  def courselist(self, course_num, *args):
    len_lab = tk.Label(self.master, text = "Class Length")
    len_lab.grid(row = 3, column = 2)

    wei_lab = tk.Label(self.master, text = "Class Weight")
    wei_lab.grid(row = 3, column = 1)

    grade_lab = tk.Label(self.master, text = "Grade")
    grade_lab.grid(row = 3, column = 3)

    name_lab = tk.Label(self.master, text = "Coursename")
    name_lab.grid(row = 3, column = 0)

    try:
      # in try so that first selection doesn't break app
      self.calc_button.destroy()
      self.output.destroy()
      for i in range(self.course_temp):
        self.len_menu[i].destroy()
        self.wei_menu[i].destroy()
        self.grades[i].destroy()
        self.names[i].destroy()

    except:
      pass    

    self.course_temp = self.get_course_number(course_num)


    for j in range(self.course_temp):
      self.lengths[j] = tk.StringVar(self.master)
      self.weights[j] = tk.StringVar(self.master)
      self.lengths[j].set('1')
      self.weights[j].set('Regular')

      self.names[j] = tk.Entry(self.master)
      self.names[j].grid(row = 4 + j, column = 0)

      self.len_menu[j] = tk.OptionMenu(self.master, self.lengths[j], '1', '2', '0.5')
      self.len_menu[j].grid(row = 4 + j, column = 2)
      self.wei_menu[j] = tk.OptionMenu(self.master, self.weights[j], 'Regular', 'E1', 'E2')
      self.wei_menu[j].grid(row = 4 + j, column = 1)

      self.grades[j] = tk.Entry(self.master)
      self.grades[j].grid(row = 4 + j, column = 3)

    self.calc_button = tk.Button(self.master, command = self.calculate) # calculates
    self.calc_button.grid(row = 4 + self.course_temp, column = 2)
    self.calc_button.config(height = 1, width = 10)

    self.output = tk.Text(self.master, width=12, height=3, wrap=tk.WORD)
    self.output.grid(row = 4 + self.course_temp, column = 3)

  def calculate(self):
    self.output.delete(1.0, tk.END)
    cred = float(self.credits_now.get())
    qp = float(self.qpa_now.get()) * cred
    for i in range(self.course_temp):
      gp = 0
      cred += float(self.lengths[i].get())
      gp += float(self.grades[i].get())

      if self.lengths[i] == 'E1':
        gp += 5
      elif self.weights[i] == 'E2':
        gp += 10
      if gp < 65:
        qp += 0
      else:
        qp += (gp - 60) / 10  
    qpa = qp / cred    
    self.output.insert(tk.END, qpa) 

if __name__ == '__main__':
   root = tk.Tk()
   main_app =  Application(root)
   root.mainloop()