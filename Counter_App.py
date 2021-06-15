import kivymd
from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.button import Button
from kivy.lang import Builder


kv ='''
BoxLayout:
    orientation:'vertical'
    MDLabel:
        id:counter_text
        text:'0'
        font_size:100
        pos_hint:{'center_x':0.5,'center_y':0.6}
        halign:'center'
        markup:True
    BoxLayout:
        orientation:'horizontal'
        padding : 50
        spacing:100
        BoxLayout:
            orientation:'horizontal'
            Button:
                id:reset
                text: "[color=#00ffcc]RESET[/color]"
                font_size:30
                on_press:app.reset()
                md_bg_color: 0.5,0.5,0.9,1
                markup: True
        BoxLayout:
            orientation:'horizontal'
            Button:
                id:increment
                text:'+1'
                font_size:30
                on_press:app.increment()
                md_bg_color: 0.5,0.5,0.9,1
                size : 150,100
                markup: True
        BoxLayout:
            orientation:'horizontal'
            Button:
                id:decrement
                text:'-1'
                font_size:30
                on_press:app.decrement()
                md_bg_color: 0.5,0.5,0.9,1
                size : 150,100
                markup: True

'''

class CounterApp(MDApp):
    counter = 0
    def build(self):
        return Builder.load_string(kv)


    def increment(self):
        self.counter += 1
        self.root.ids.counter_text.text = str(self.counter)

    def decrement(self):
        if self.counter > 0:
            self.counter -= 1
            self.root.ids.counter_text.text = str(self.counter)

    def reset(self):
        self.counter = 0
        self.root.ids.counter_text.text = str(self.counter)

CounterApp().run()