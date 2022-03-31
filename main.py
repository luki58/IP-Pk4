from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase



class MainWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("main.kv")

class TesteApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    TesteApp().run()
    

###############################
KV = """
MDBoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: 'Example Tabs'

    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch(*args)


<Tab>:

    MDLabel:
        id: label
        text: 'Tab 0'
        halign: 'center'
"""


class Tab(MDFloatLayout, MDTabsBase):
    """Class implementing content for a tab."""


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(20):
            # Add a new tab to the MDTabs Layout.
            self.root.ids.tabs.add_widget(Tab(title=f"Tab {i}"))

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        """Called when the tab is switched.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        """

        instance_tab.ids.label.text = f" This is the content of {tab_text}"


Example().run()