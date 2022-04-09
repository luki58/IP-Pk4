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
            id: fluxreduction
            title: 'Flux-Based Reduction'
        
            BoxLayout:
                id:fluxbox
                orientation: 'horizontal'
                pos_hint:{'center_x': .35, 'center_y': .75}
                kepp_ratio: True
                allow_strech: True
                size_hint: (.55,.3)
            
            MDSlider:
                id:slider1
                pos_hint:{'center_x': .35, 'center_y': .6}
                size_hint_x: .55
                min: 0
                max: 100
            
            MDSlider:
                id:slider2
                pos_hint:{'center_x': .35, 'center_y': .55}
                size_hint_x: .55
                min: 0
                max: 100
                value: self.max
            
            MDFloatingActionButton:
                icon: "information-variant"
                font_size: "18sp"
                pos_hint:{'center_x': .75, 'center_y': .75}
            
            MDFillRoundFlatButton:
                id:fluxbutton
                pos_hint:{'center_x': .75, 'center_y': .85}
                size: dp(15), dp(15)
                text: "Go Flux"
                on_press: app.flux()
                disabled: True
            
        Tab:
            id: imagereduction
            title: 'Image Overview Reduction'
        
            BoxLayout:
                id:overviewbox
                orientation: 'horizontal'
                pos_hint:{'center_x': .35, 'center_y': .5}
                kepp_ratio: True
                allow_strech: True
                size_hint: (.4,.4)
            
            MDSlider:
                id:slider3
                pos_hint:{'center_x': .35, 'center_y': .2}
                size_hint_x: .55
                min: 0
                max: 100
            
            MDSlider:
                id:slider4
                pos_hint:{'center_x': .35, 'center_y': .1}
                size_hint_x: .55
                min: 0
                max: 100
                value: self.max
            
            MDFloatingActionButton:
                icon: "information-variant"
                font_size: "18sp"
                pos_hint:{'center_x': .75, 'center_y': .45}
            
            MDFillRoundFlatButton:
                id:overviewbutton
                pos_hint:{'center_x': .75, 'center_y': .6}
                size: dp(15), dp(15)
                text: "Go Overview"
                on_press: app.overview()
                disabled: True
        
        Tab:
            id: insight
            title: 'Analysis'
        
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

    def flux(self):
        self.root.ids.fluxbox.clear_widgets()
        #
        if self.datalen <= 50:
            flux_data = Flux(Data_raw, 20)
        elif self.datalen <= 100:
            flux_data = Flux(Data_raw, 40)
        elif self.datalen <= 300:
            flux_data = Flux(Data_raw, 80)
        elif self.datalen >= 300:
            flux_data = Flux(Data_raw, 140) 
        #
        graph = Graph(xlabel='Frames', ylabel='Flux', x_ticks_minor=5,
        y_grid_label=True, x_grid_label=True, padding=5, x_ticks_major=10, y_ticks_major=10,
        x_grid=True, y_grid=True, xmin=-0, xmax=len(flux_data), ymin=int(np.amin(flux_data)-0.5), ymax=int(np.amax(flux_data)+0.5))
        plot = LinePlot(color=[0, 0, 1, 1], line_width=1.5)
        plot.points = [(x,flux_data[x]) for x in range(0,len(flux_data)-1)]
        graph.add_plot(plot)
        #
        self.root.ids.fluxbox.add_widget(graph)
        #
        #self.root.ids.overviewbox.add_widget(graph)

if __name__ == "__main__":
    Ippk4App().run()