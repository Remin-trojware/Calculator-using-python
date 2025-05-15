#This whole code is Develped by "Remin Tom Denny"-Remin_trojware
import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("600x600")
        
        self.displaylabel = tk.Label(root, text="", height=2, anchor="e", font=("Arial", 24), bg="gray", fg="green")
        self.displaylabel.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        self.isoperatorclicked = False
        self.oldvalue = ""
        self.operator = ""
        
        # Define the buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('-', 4, 3),
            ('clr', 5, 0, 4)
        ]
        
        # Add buttons to grid
        for (text, row, col, *span) in buttons:
            button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=span[0] if span else 1, padx=5, pady=5, sticky="nsew")
        
        # Adjust grid to expand properly
        for r in range(6):
            root.grid_rowconfigure(r, weight=1)
        for c in range(4):
            root.grid_columnconfigure(c, weight=1)
    
    def on_button_click(self, text):
        if text in '0123456789.':
            if self.isoperatorclicked:
                self.displaylabel.config(text=text)
                self.isoperatorclicked = False
            else:
                current_text = self.displaylabel.cget("text")
                self.displaylabel.config(text=current_text + text)
        elif text in '+-x/':
            self.operator = text
            self.oldvalue = self.displaylabel.cget("text")
            self.isoperatorclicked = True
        elif text == "=":
            newvalue = float(self.displaylabel.cget("text"))
            if self.operator == "+":
                result = float(self.oldvalue) + newvalue
            elif self.operator == "-":
                result = float(self.oldvalue) - newvalue
            elif self.operator == "x":
                result = float(self.oldvalue) * newvalue
            elif self.operator == "/":
                if newvalue != 0:
                    result = float(self.oldvalue) / newvalue
                else:
                    self.displaylabel.config(text="Error")
                    return
            self.displaylabel.config(text=str(result))
            self.operator = ""
        elif text == "clr":
            self.displaylabel.config(text="")
            self.oldvalue = ""
            self.operator = ""

# Create the main window and the calculator
root = tk.Tk()
calc = Calculator(root)
root.mainloop()
