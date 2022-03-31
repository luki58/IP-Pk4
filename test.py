import os

from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window 

from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

KV = """
BoxLayout:
    orientation: 'vertical'
    id: boxlay

    MDToolbar:
        id: toolbar
        type_height: 'small'
        title: 'PK-4 Pipeline' 
    
        canvas:
            Rectangle:
                source: 'pk4-logo.png'
                size: self.size
                pos: toolbar.width-self.width, toolbar.y+self.height 
    MDTabs:
        id: tabs
        
        Tab:
            id: readin
            title: 'Data Read In'
            
            TextInput:
                id: path
                pos_hint:{'center_x': .5, 'center_y': .7}
                size_hint:0.5, 0.07
                hint_text: 'Enter Data-Path'
                halign: 'center'
            
            MDFillRoundFlatButton:
                pos_hint:{'center_x': .5, 'center_y': .6}
                size_hint:0.2, 0.07
                text: "Perform Data Reduction"
                on_press: app.inputpath()
                
        Tab:
            id: reduction
            title: 'Data Reduction'
            
        Tab:
            id: insight
            title: 'First Insight'
        
        Tab:
            id: setup
            title: 'Exp Setup'
            Image:
                source: 'pk4-setup.png'

<Tab>:

    MDLabel:
        id: label
        halign: 'center'
"""


class Tab(MDFloatLayout, MDTabsBase):
    """Class implementing content for a tab."""

class Ippk4App(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def inputpath(self):
        path = self.root.ids.path.text
        if os.path.exists(path) == True:
            print(f'The path is: {path}')
        else:
            print('No path found, try again')

if __name__ == "__main__":
    Ippk4App().run()