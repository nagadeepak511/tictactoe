from game_status_function import game_status_check
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty

global count
count = 0

class MainWidget(StackLayout):
    label_text = StringProperty("Player-1's turn")
    l = [[1,2,3],[4,5,6],[7,8,9]]
    
    def on_button_click(self, widget, x, y):
        global count
        count+=1
        a=""
        print(f"{count}  {count%2}")
        if(count%2 != 0):
            a="X"
        else:
            a="O"
        widget.disabled = True
        widget.text = a
        self.l[x][y] = a
        
        status = game_status_check(self.l)
        print(self.l, status)
        if(status == "Can continue"):
            if(count%2 == 0):
                self.label_text="Player-1's turn"
            else:
                self.label_text="Player-2's turn"
        else:
            self.label_text = status + "\nGame over"


class TTTApp(App):
    pass

TTTApp().run()