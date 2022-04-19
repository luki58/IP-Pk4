import os
import numpy as np
import matplotlib.pyplot as plt
#from PIL import Image as ImageImport

from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window 
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

import pims

from dataoverview import Flux, Dataoverview 

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
            
            MDTextField:
                id: path
                pos_hint:{'center_x': .5, 'center_y': .64}
                size: dp(100), dp(30)
                hint_text: 'Enter Data-Path'
                halign: 'center'
            
            MDFillRoundFlatButton:
                pos_hint:{'center_x': .5, 'center_y': .5}
                size: dp(30), dp(15)
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
        
            MDBoxLayout:
                id:fluxbox
                orientation: 'horizontal'
                pos_hint:{'center_x': .35, 'center_y': .7}
                kepp_ratio: True
                allow_strech: True
                size_hint: (.55,.3)   
                
            MDFillRoundFlatButton:
                id:fluxbutton
                pos_hint:{'center_x': .75, 'center_y': .7}
                size: dp(15), dp(15)
                text: "Go Flux"
                on_press: app.flux()
                disabled: True
            
        Tab:
            id: insight
            title: 'First Insight'
        
        Tab:
            id: setup
            title: 'Exp Setup'
            Image:
                source: 'imgs/pk4-setup110422.png'

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
                Data_raw = pims.open(path+"\*.bmp")    
                self.root.ids.path.hint_text = 'Loaded Successfully'
                self.root.ids.fluxbutton.disabled = False
            else:
                self.root.ids.path.hint_text = 'No \*.bmp data found'
                self.root.ids.fluxbutton.disabled = True
        else:
            self.root.ids.path.hint_text = 'Path does NOT exist. Try again!'
            self.root.ids.fluxbutton.disabled = True

    def flux(self):
        self.root.ids.fluxbox.clear_widgets()
        #
        flux_data = Flux(Data_raw, 40)
        #
        #self.root.ids.spinner.active = False        #hide loading item
        arr_ref =  np.arange(len(flux_data))
        plt.style.use(['science','no-latex'])
        fig, ax = plt.subplots(dpi=80)
        ax.plot(arr_ref, flux_data)
        ax.grid(color='grey', linestyle='-', linewidth=0.2, alpha=0.5)
        #                            
        self.root.ids.fluxbox.add_widget(FigureCanvasKivyAgg(plt.gcf()))
               
        

if __name__ == "__main__":
    Ippk4App().run()