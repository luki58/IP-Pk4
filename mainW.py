import os
import numpy as np
import matplotlib.pyplot as plt
from math import sin
#from PIL import Image as ImageImport

from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window 
from kivy_garden.graph import Graph, LinePlot

from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.dialog import MDDialog

import pims

from dataoverview import Flux, Dataoverview 

KV="""
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
            
            MDTextField:
                id: path
                pos_hint:{'center_x': .5, 'center_y': .64}
                hint_text: 'Enter Data-Path'
                halign: 'center'
 
        Tab:
            id: fluxreduction
            title: 'Flux-Based Reduction'
            
        Tab:
            title:"three"
            
        Tab:
            title:"four"
    
<Tab>:
    MDLabel:
        id: label
        halign: 'center'    
"""

class Tab(MDFloatLayout, MDTabsBase):
    """Class implementing content for a tab."""
    
class Ippk4App(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        #self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string(KV)
    
    def inputpath(self):
        path = self.root.ids.path.text
        self.root.ids.path.text = ''
        if os.path.exists(path) == True:            #read data
            datalist = os.listdir(path)
            datacheck = False
            for i in datalist:
                if i[-1] == 'p':
                    datacheck = True
                    break;
            if datacheck != False:
                global Data_raw
                Data_raw = pims.open(path+"/*.bmp")    
                self.root.ids.path.hint_text = 'Loaded Successfully'
                self.root.ids.fluxbutton.disabled = False
                self.root.ids.overviewbutton.disabled = False
                self.datalen = len(Data_raw)
            else:
                self.root.ids.path.hint_text = 'No \*.bmp data found'
                self.root.ids.fluxbutton.disabled = True
        else:
            self.root.ids.path.hint_text = 'Path does NOT exist. Try again!'
            self.root.ids.fluxbutton.disabled = True
    
if __name__ == "__main__":
    Ippk4App().run()