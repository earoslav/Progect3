class Widget:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
    def printInfo(self):
        print(f"Напис віджета: {self.text}")    
        print(f"Розташування віджета: {self.x}, {self.y}")  
class Button(Widget):
    def __init__(self, text, x, y):
        super().__init__(text, x, y)
        self.is_clicked = False
    def click(self):
        self.is_clicked = True
        print("")    