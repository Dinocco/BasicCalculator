from tkinter import *

j = 0

uwu = Tk() 
uwu.title("Calculadora")
uwu.geometry("410x600")
uwu.rowconfigure(0, weight = 1)
uwu.columnconfigure(0, weight = 1)
uwu.configure(bg = "black")
uwu.resizable(0, 0)

obo = Entry(uwu, width = 64, bg = "gray")
obo.place(x = 10, y = 10, height = 100)
obo.configure(font = "Times 45")

calc = Entry(uwu, width = 15, bg = "gray")
calc.place(x = 355, y = 10)
calc.configure(font = "Times 14")


def guardar_num():
        obo_state = obo.get()
        global obo_old
        obo_old = obo_state


def get_numero(n):
        global j
        obo.insert(j, n)
        j += 1


def get_operacion(operator):
        global j
        op_length = len(operator)
        obo.insert(j, operator)
        j += op_length
        guardar_num()
        clear_entry()
        calc.insert(j, operator)


def clear_entry():
        obo.delete(0, END)
        calc.delete(0, END)


def undo():
        obo_state = obo.get()
        if len(obo_state):
                obo_nuevo = obo_state[:-1] # Menos 1
                clear_entry()
                obo.insert(0, obo_nuevo)
        else:
                clear_entry()
                obo.insert(0, "Error")


def resultado():
        obo_state = obo.get()
        try:
                final_exp = obo_old + obo_state
                result = eval(final_exp)
                clear_entry()
                obo.insert(0, result)
        except:
                clear_entry()
                obo.insert(0, "Error")
def botones():
        xd = Button(uwu, width = 10, height = 3, bd = "10")
        xd.place(x = 10, y = 520)

        xd = Button(uwu, text = "0", width = 10, height = 3, bd = "10", command = lambda: get_numero(0))
        xd.place(x = 110, y = 520)

        xd = Button(uwu, text = ".", width = 10, height = 3, bd = "10", command = lambda: get_numero("."))
        xd.place(x = 210, y = 520)

        xd = Button(uwu, text = "=", width = 10, height = 3, bd = "10", command = lambda: resultado())
        xd.place(x = 310, y = 520)

        xd = Button(uwu, text = "1", width = 10, height = 3, bd = "10", command = lambda: get_numero(1))
        xd.place(x = 10, y = 440)

        xd = Button(uwu, text = "2", width = 10, height = 3, bd = "10", command = lambda: get_numero(2))
        xd.place(x = 110, y = 440)

        xd = Button(uwu, text = "3", width = 10, height = 3, bd = "10", command = lambda: get_numero(3))
        xd.place(x = 210, y = 440)

        xd = Button(uwu, text = "+", width = 10, height = 3, bd = "10", command = lambda: get_operacion("+"))
        xd.place(x = 310, y = 440)

        xd = Button(uwu, text = "4", width = 10, height = 3, bd = "10", command = lambda: get_numero(4))
        xd.place(x = 10, y = 360)

        xd = Button(uwu, text = "5", width = 10, height = 3, bd = "10", command = lambda: get_numero(5))
        xd.place(x = 110, y = 360)

        xd = Button(uwu, text = "6", width = 10, height = 3, bd = "10", command = lambda: get_numero(6))
        xd.place(x = 210, y = 360)

        xd = Button(uwu, text = "-", width = 10, height = 3, bd = "10", command = lambda: get_operacion("-"))
        xd.place(x = 310, y = 360)

        xd = Button(uwu, text = "7", width = 10, height = 3, bd = "10", command = lambda: get_numero(7))
        xd.place(x = 10, y = 280)

        xd = Button(uwu, text = "8", width = 10, height = 3, bd = "10", command = lambda: get_numero(8))
        xd.place(x = 110, y = 280)

        xd = Button(uwu, text = "9", width = 10, height = 3, bd = "10", command = lambda: get_numero(9))
        xd.place(x = 210, y = 280)

        xd = Button(uwu, text = "x", width = 10, height = 3, bd = "10", command = lambda: get_operacion("*"))
        xd.place(x = 310, y = 280)

        xd = Button(uwu, text = "1/x", width = 10, height = 3, bd = "10", command = lambda: get_operacion("1/"))
        xd.place(x = 10, y = 200)

        xd = Button(uwu, text = "x²", width = 10, height = 3, bd = "10", command = lambda: get_operacion("**2"))
        xd.place(x = 110, y = 200)

        xd = Button(uwu, text = "√", width = 10, height = 3, bd = "10", command = lambda: get_operacion("**(0.5)"))
        xd.place(x = 210, y = 200)

        xd = Button(uwu, text = "÷", width = 10, height = 3, bd = "10", command = lambda: get_operacion("/"))
        xd.place(x = 310, y = 200)

        xd = Button(uwu, text = "%", width = 10, height = 3, bd = "10", command = lambda: get_operacion("%"))
        xd.place(x = 10, y = 120)

        xd = Button(uwu, text = "UwU", width = 10, height = 3, bd = "10", command = lambda: get_numero("Secret Button"))
        xd.place(x = 110, y = 120)

        xd = Button(uwu, text = "DEL", width = 10, height = 3, bd = "10", command = lambda: undo())
        xd.place(x = 210, y = 120)

        xd = Button(uwu, text = "CE", width = 10, height = 3, bd = "10", command = lambda: clear_entry())
        xd.place(x = 310, y = 120)

botones()        

uwu.mainloop()
