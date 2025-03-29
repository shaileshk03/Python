import tkinter as tk

calculation = ""

def add_to_calculator(symbol):
    global calculation
    #
    calculation += str(symbol)
    #
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

    pass

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_filed()
        text_result.insert(1.0, "Error")
    pass

def clear_filed():
    pass

root = tk.Tk()
# size of calculator
root.geometry("350x275")
text_result = tk.Text(root, width = 40, height = 5,  font = ("Arial", 24))
text_result.grid(columnspan=5)
#
root.mainloop()
