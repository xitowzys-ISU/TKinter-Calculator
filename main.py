import tkinter as tk
from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def evaluate_expression(self, example: str) -> float | str:
        pass

    @abstractmethod
    def negative(self, example: str) -> float| str:
        pass
    

class Calculator(ICalculator):
    def __init__(self) -> None:
        pass

    def evaluate_expression(self, example: str) -> float | str:
        try:
            return eval(example)
        except SyntaxError:
            return "Syntax Error"
    
    def negative(self, example: str) -> float| str:
        try:
            number: float = eval(example)
            number *= -1
            return number
        except SyntaxError:
            return "Invalid syntax"

class TkInterfaceCalculator:
    def __init__(self, calc_obj: ICalculator, btn_color: str, btn_font: str, btn_width: int, btn_height: int) -> None:
        self.__tk: tk.Tk = tk.Tk()
        self.__tk.title('Calculator')
        self.__tk.config(bg='#a8a4a4')

        self.__tk.resizable(width=0, height=0)

        self.screen: tk.Entry = tk.Entry(self.__tk, font='Arial 20 bold', bg='#727a7e', fg='white', width=18)
        self.__frame: tk.Frame = tk.Frame(self.__tk, bg='#a8a4a4', padx=10, pady=10)

        self.__btn_color: str = btn_color
        self.__btn_font: str = btn_font
        self.__btn_width: int = btn_width
        self.__btn_height: int = btn_height

        self.__calc_obj: ICalculator = calc_obj

        self.__button_list: list[list[str]] = [['C', '/'], ['7', '8', '9', '*'], ['4', '5', '6', '-'], ['1', '2', '3', '+'], ['+/-', '0', '.', '=']]

        self.__init_window()

    def __init_button(self) -> None:

        for i, buttons in enumerate(self.__button_list):
            for j, button in enumerate(buttons):
                if button == "C":
                    tk.Button(self.__frame, bg=self.__btn_color, text="C", font=self.__btn_font, width=10, height=self.__btn_height, command=lambda: self.__press_key("C")).grid(row=0, column=0, columnspan=3)
                elif button == "/":
                    tk.Button(self.__frame, bg=self.__btn_color, text="/", font=self.__btn_font, width=self.__btn_width, height=self.__btn_height, command=lambda: self.__press_key("/")).grid(row=0, column=3)
                else:
                    tk.Button(self.__frame, bg=self.__btn_color, text=button, font=self.__btn_font, width=self.__btn_width, height=self.__btn_height, command=lambda _button=button: self.__press_key(_button)).grid(row=i, column=j) 

    def __init_window(self) -> None:
        self.screen.pack()
        self.__frame.pack()

        self.__init_button()

    def __clear_screen(self):
        self.screen.delete(0, tk.END)

    def __press_key(self, num: str):
        print(num)
        if num == "C":
            self.__clear_screen()
        elif num == "=":
            self.__evaluate_expression()
        elif num == "+/-":
            self.__negative()
        else:
            self.screen.insert(tk.END, num)

    def __negative(self):
        result: float | str = self.__calc_obj.negative(example=self.screen.get())

        self.__clear_screen()

        if (type(result) is str):
            self.screen.insert(0, result)
        else:
            self.screen.insert(0, result)

    def __evaluate_expression(self):
        result: float | str = self.__calc_obj.evaluate_expression(example=self.screen.get())

        self.__clear_screen()

        if (type(result) is str):
            self.screen.insert(0, result)
        else:
            self.screen.insert(0, result)

    def run(self) -> None:
        self.__tk.mainloop()


if __name__ == "__main__":
    tkInt = TkInterfaceCalculator(
        calc_obj=Calculator(),
        btn_color="orange",
        btn_font="Arial 20 bold",
        btn_height=1,
        btn_width=3
    )
    tkInt.run()
