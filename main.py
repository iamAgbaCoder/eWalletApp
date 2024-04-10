from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.utils import rgba

Window.size = (310, 580)

class Binance(MDApp):
    
    def build(self):
        return Builder.load_file('main.kv')
    
    def current_slide(self, index):
        for i in range(3):
            if index == i:
                self.root.ids[f"slide{index}"].color = rgba(47, 46, 65, 255)
            else:
                self.root.ids[f"slide{i}"].color = rgba(233, 237, 240, 255)
    
    def next(self):
        self.root.ids.carousel.load_next(mode="next")
    
if __name__ == '__main__':
    Binance().run()
    
    

    