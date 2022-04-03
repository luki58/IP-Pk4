import os
#from PIL import Image as ImageImport

from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window 

from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

import pims

KV = """
BoxLayout:
    orientation: 'vertical'
    id: boxlay

    MDToolbar:
        id: toolbar
        type_height: 'small'
        title: 'PK-4 Pipeline' 
    
    MDTabs:
        id: tabs
        
        Tab:
            id: readin
            title: 'Data Read In'
            
            TextInput:
                id: path
                pos_hint:{'center_x': .5, 'center_y': .64}
                size_hint:0.5, 0.07
                hint_text: 'Enter Data-Path'
                halign: 'center'
            
            MDSpinner:
                id: spinner
                size_hint: None, None
                size: dp(46), dp(46)
                pos_hint: {'center_x': .5, 'center_y': .3}
                active: False
            
            MDFillRoundFlatButton:
                pos_hint:{'center_x': .5, 'center_y': .5}
                size_hint:0.1, 0.07
                text: "Load Data"
                on_press: app.inputpath()
        
            Image:
                source:'imgs/pk4-logo.png'
                pos_hint:{'center_x': .5, 'center_y': .8}
                allow_strech: True
                kepp_ratio: True
                size_hint: (.09,.09)
                
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
                source: 'imgs/pk4-setup.png'

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
        self.root.ids.spinner.active = True         #display loading item
        self.root.ids.path.text = ''
        if os.path.exists(path) == True:            #read data
            datalist = os.listdir(path)
            datacheck = False
            for i in datalist:
                if i[-1] == 'p':
                    datacheck = True
                    break;
            if datacheck != False:
                data = pims.open(path+"\*.bmp")    
                self.root.ids.path.hint_text = 'Loaded Successfully'
            else:
                self.root.ids.path.hint_text = 'No \*.bmp data found'
        else:
            self.root.ids.path.hint_text = 'Path does NOT exist. Try again!'
            
        self.root.ids.spinner.active = False
        
        return data

if __name__ == "__main__":
    Ippk4App().run()