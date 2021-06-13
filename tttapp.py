from game_status_function import game_status_check
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.label import Label

global count
global disable_function
count = 0
disable_function = False

class MainWidget(StackLayout):
    label_text = StringProperty("Player-1's turn")
    l = [[1,2,3],[4,5,6],[7,8,9]]
    btns=[[1,2,3],[4,5,6],[7,8,9]]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(3):
            for j in range(3):
                b = Button(text = f"_", size_hint=[0.33,0.25], font_name="Lcd.ttf", font_size=80, color=[0,1,0,1])
                b.bind(on_press = self.on_button_click)
                self.btns[i][j] = b
                self.add_widget(b)

    
    def on_button_click(self, widget):
        global disable_function
        if(not disable_function):
            pos=[]
            for i in range(len(self.btns)):
                for j in range(len(self.btns[i])):
                        if(self.btns[i][j] == widget):
                            pos=[i,j]
                            print(pos)
            global count
            count += 1
            if(count % 2 == 0):
                a="O"
            else:
                a="X"
            widget.text = a
            self.btns[pos[0]][pos[1]].disabled = True
            self.l[pos[0]][pos[1]] = a
            

            status = game_status_check(self.l)
            print(self.l, status)
            if(status[0] == "Can continue"):
                if(count%2 == 0):
                    self.label_text="Player-1's turn"
                else:
                    self.label_text="Player-2's turn"
            else:
                self.label_text = status[0] + "\nGame over"
                for i in range(3):
                    for j in range(3):
                        self.btns[i][j].disabled = True
                
                for i in range(3):
                    for j in range(3):
                        if(status[1] >=0 and status[1] < 8):
                            if(status[1] < 3):
                                if(i == status[1]):
                                    self.btns[i][j].disabled = False
                                    self.btns[i][j].color = [0,0,1,1]
                            elif(status[1] < 6):
                                if(i+3 == status[1]):
                                    self.btns[j][i].disabled = False
                                    self.btns[j][i].color = [0,0,1,1]
                            elif(status[1] == 6):
                                if(i == j):
                                    self.btns[i][j].disabled = False
                                    self.btns[i][j].color = [0,0,1,1]
                            elif(status[1] == 7):
                                if(i+j == 2):
                                    self.btns[i][j].disabled = False
                                    self.btns[i][j].color = [0,0,1,1]
                disable_function = True
                




class TTTApp(App):
    pass

TTTApp().run()
