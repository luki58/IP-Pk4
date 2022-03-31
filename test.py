from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
 
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

KV = """
BoxLayout:
    orientation: 'vertical'
    
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
                pos_hint:{'center_x': .5, 'center_y': .7}
                size_hint:0.3, 0.07
                hint_text: 'Enter Data-Path'
                halign: 'center'
            
            Button:
                pos_hint:{'center_x': .5, 'center_y': .6}
                size_hint:0.3, 0.07
                text: "Perform Data Reduction"
                
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


class Testwindow(MDApp):
    def build(self):
        return Builder.load_string(KV)

Testwindow().run()