import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
  BACKGROUND_COLOR = '#1f211f'
  TEXT_COLOR = '#bbc9bf'
  ENTRY_BACKGROUND = '#1f211f'
  WORD_FONT = 'georgia', 12
  MENU_FONT = "Helvetica", 12, 'bold'

  # initializing class variables so that they can be dynamically created and destroyed by courselist
  course_temp = 0 # number of courses user wants to calculate into their qpa
  cred_menu = {} # option menus for credits
  wei_menu = {} # option menus for course weights
  credits = {} # options for cred_menu
  weights = {} # options for wei_menu
  grades = {} # entry boxes for course grades
  names = {} # entry boxes for course names

  output = None # initializes output box, so it may be used by multiple functions
  calc_button = None # initilaizes output box, so it may be used by multiple functions
  credits_now = None # initializes initial credits entry box, so it may be used by multiple functions
  qpa_now = None # initializes initial qpa entry box, so it may be used by multiple functions

  def __init__(self, master):
    self.master = master
    tk.Frame.__init__(self, self.master)
    self.configure_gui()
    self.create_widgets()

  def configure_gui(self):
    self.master.title("QPA Calculator")
    self.master['bg'] = self.BACKGROUND_COLOR
     
  def create_widgets(self):
    cur_cred_lab = tk.Label(self.master, text = "Current Credits")
    cur_cred_lab.grid(row = 1, column = 0, sticky = tk.E)
    cur_cred_lab['bg'] = self.BACKGROUND_COLOR
    cur_cred_lab['fg'] = self.TEXT_COLOR
    cur_cred_lab['font'] = self.WORD_FONT

    cur_qpa_lab = tk.Label(self.master, text = "Current QPA")
    cur_qpa_lab.grid(row = 0, column = 0, sticky = tk.E)
    cur_qpa_lab['bg'] = self.BACKGROUND_COLOR
    cur_qpa_lab['fg'] = self.TEXT_COLOR
    cur_qpa_lab['font'] = self.WORD_FONT

    how_many_lab = tk.Label(self.master, text = "How many courses would you like to factor in?")
    how_many_lab.grid(row = 2, column = 0, padx = 5, sticky = tk.W)
    how_many_lab['bg'] = self.BACKGROUND_COLOR
    how_many_lab['fg'] = self.TEXT_COLOR
    how_many_lab['font'] = self.WORD_FONT

    self.qpa_now = tk.StringVar()
    qn_entry = tk.Entry(self.master, textvariable = self.qpa_now)
    qn_entry.grid(row = 0, column = 1, sticky = tk.W)
    qn_entry['bg'] = self.ENTRY_BACKGROUND
    qn_entry['fg'] = self.TEXT_COLOR
    qn_entry['font'] = self.MENU_FONT

    self.credits_now = tk.StringVar() 
    cn_entry = tk.Entry(self.master, textvariable = self.credits_now)
    cn_entry.grid(row = 1, column = 1, sticky = tk.W)
    cn_entry['bg'] = self.ENTRY_BACKGROUND
    cn_entry['fg'] = self.TEXT_COLOR
    cn_entry['font'] = self.MENU_FONT

    course_num = tk.StringVar(self.master) 
    course_num.set("0")
    course_num.trace("w", lambda var_name, var_index, operation: self.courselist(course_num)) # calls courselist function everytime dropdown option is changed
    num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9','10'] 

    course_num_menu = tk.OptionMenu(self.master, course_num, *num_list) #
    course_num_menu.grid(row = 2, column = 1)
    course_num_menu['bg'] = self.BACKGROUND_COLOR
    course_num_menu['fg'] = self.TEXT_COLOR
    course_num_menu['menu'].config(bg = self.BACKGROUND_COLOR, fg = self.TEXT_COLOR, font = self.MENU_FONT)
    course_num_menu['activebackground'] = self.BACKGROUND_COLOR
    course_num_menu['activeforeground'] = self.TEXT_COLOR
    course_num_menu['highlightthickness'] = 0
    course_num_menu['width'] = 5
    course_num_menu['font'] = self.MENU_FONT

  def get_course_number(self, course_num):
    # allows courselist function to get course_num from create_widgets function
    return int(course_num.get()) 

  def courselist(self, course_num, *args):
    # is called whenever course_num_menu is changed
    # destroys then creates widgets that allow user to calculate
    # their QPA based on a specified number of courses
    cred_lab = tk.Label(self.master, text = "Credits")
    cred_lab.grid(row = 3, column = 2)
    cred_lab['bg'] = self.BACKGROUND_COLOR
    cred_lab['fg'] = self.TEXT_COLOR
    cred_lab['font'] = self.WORD_FONT

    wei_lab = tk.Label(self.master, text = "Weight")
    wei_lab.grid(row = 3, column = 1)
    wei_lab['bg'] = self.BACKGROUND_COLOR
    wei_lab['fg'] = self.TEXT_COLOR
    wei_lab['font'] = self.WORD_FONT

    grade_lab = tk.Label(self.master, text = "Grade")
    grade_lab.grid(row = 3, column = 3)
    grade_lab['bg'] = self.BACKGROUND_COLOR
    grade_lab['fg'] = self.TEXT_COLOR
    grade_lab['font'] = self.WORD_FONT

    name_lab = tk.Label(self.master, text = "Name (optional)")
    name_lab.grid(row = 3, column = 0)
    name_lab['bg'] = self.BACKGROUND_COLOR
    name_lab['fg'] = self.TEXT_COLOR
    name_lab['font'] = self.WORD_FONT

    try:
      # in try so that first selection doesn't break app
      self.calc_button.destroy()
      self.output.destroy()
      for i in range(self.course_temp):
        self.cred_menu[i].destroy()
        self.wei_menu[i].destroy()
        self.grades[i].destroy()
        self.names[i].destroy()

    except:
      pass    

    self.course_temp = self.get_course_number(course_num)

    for j in range(self.course_temp):
    # this loop creates entry boxes based on option menu that gives course_number
      self.credits[j] = tk.StringVar(self.master) 
      self.credits[j].set('1')

      self.weights[j] = tk.StringVar(self.master)
      self.weights[j].set('Regular')

      self.names[j] = tk.Entry(self.master)
      self.names[j].grid(row = 4 + j, column = 0)
      self.names[j]['bg'] = self.ENTRY_BACKGROUND
      self.names[j]['fg'] = self.TEXT_COLOR
      self.names[j]['font'] = self.MENU_FONT

      self.cred_menu[j] = tk.OptionMenu(self.master, self.credits[j], '1', '2', '0.5')
      self.cred_menu[j].grid(row = 4 + j, column = 2, padx = 10)
      self.cred_menu[j]['bg'] = self.ENTRY_BACKGROUND
      self.cred_menu[j]['fg'] = self.TEXT_COLOR
      self.cred_menu[j]['font'] = self.MENU_FONT
      self.cred_menu[j]['menu'].config(bg = self.BACKGROUND_COLOR, fg = self.TEXT_COLOR, font = self.MENU_FONT)
      self.cred_menu[j]['activebackground'] = self.BACKGROUND_COLOR
      self.cred_menu[j]['activeforeground'] = self.TEXT_COLOR
      self.cred_menu[j]['highlightthickness'] = 0
      self.cred_menu[j]['width'] = 5

      self.wei_menu[j] = tk.OptionMenu(self.master, self.weights[j], 'Regular', 'E1', 'E2')
      self.wei_menu[j].grid(row = 4 + j, column = 1, padx = 10)
      self.wei_menu[j]['bg'] = self.ENTRY_BACKGROUND
      self.wei_menu[j]['fg'] = self.TEXT_COLOR
      self.wei_menu[j]['font'] = self.MENU_FONT
      self.wei_menu[j]['menu'].config(bg = self.BACKGROUND_COLOR, fg = self.TEXT_COLOR, font = self.MENU_FONT)
      self.wei_menu[j]['activebackground'] = self.BACKGROUND_COLOR
      self.wei_menu[j]['activeforeground'] = self.TEXT_COLOR
      self.wei_menu[j]['highlightthickness'] = 0
      self.wei_menu[j]['width'] = 6

      self.grades[j] = tk.Entry(self.master)
      self.grades[j].grid(row = 4 + j, column = 3, padx = 10)
      self.grades[j]['bg'] = self.ENTRY_BACKGROUND
      self.grades[j]['fg'] = self.TEXT_COLOR
      self.grades[j]['font'] = self.MENU_FONT
      self.grades[j]['width'] = 5

    self.calc_button = tk.Button(self.master, command = self.calculate, text = 'Calculate')
    self.calc_button.grid(row = 4 + self.course_temp, column = 0, sticky = tk.E)
    self.calc_button.config(height = 1, width = 10)
    self.calc_button['bg'] = self.ENTRY_BACKGROUND
    self.calc_button['fg'] = self.TEXT_COLOR
    self.calc_button['font'] = self.WORD_FONT

    self.output = tk.Text(self.master, width = 15, height = 2, wrap=tk.WORD)
    self.output.grid(row = 4 + self.course_temp, column = 1, padx = 10, pady = 10, sticky = tk.E)

    self.output['bg'] = self.ENTRY_BACKGROUND
    self.output['fg'] = self.TEXT_COLOR
    self.output['font'] = self.MENU_FONT

  def calculate(self):
    # calculates QPA and prints it in output box
    self.output.delete(1.0, tk.END)
    try:
      cred = float(self.credits_now.get()) 
      qp = float(self.qpa_now.get()) * cred 
      for i in range(self.course_temp):
        gp = 0 
        cred += float(self.credits[i].get())
        gp += float(self.grades[i].get())
        if self.weights[i].get() == 'E1':
          gp += 5
        elif self.weights[i].get() == 'E2':
          gp += 10    
        if gp < 65:
          qp += 0  
        else:
          gp = (gp - 60) / 10 # converting grade point to quality points
          gp *= float(self.credits[i].get()) # adjusts quality points to reflect class credits
          qp += gp
      qpa = qp / cred    
      self.output.insert(tk.END, round(qpa, 5)) 
    except:
      self.output.insert(tk.END,"Fill all required boxes.")  

if __name__ == '__main__':
   root = tk.Tk()
   main_app =  Application(root)
   root.mainloop()