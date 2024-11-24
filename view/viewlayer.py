import os

from kivy.app import App
from kivy.config import Config

# Config.set('graphics', 'borderless', '1')
Config.set("graphics", "width", "1200")
Config.set("graphics", "height", "800")
Config.set("graphics", "resizable", True)


# from kivy.core.window import Window
# Window.maximize()

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager

import system.const
from library.buttonover import ButtonOver

Builder.load_file(os.path.dirname(__file__) + "/viewlayer.kv")


class ActivityBar(GridLayout):
    pass


class ScreenFindDuplicates(Screen):
    """
    Klasse zeigt die Ergebnisse an

    Args:
        Screen (Screen): Übergabeparameter
    """

    def __init__(self, **kwargs):
        super(ScreenFindDuplicates, self).__init__(**kwargs)

    def on_enter(self, *args):
        Window.set_title(system.const.SCREEN_TITLE_FIND_DUPLICATES)
        return super().on_enter(*args)


class ScreenFilenameChange(Screen):
    """
    Klasse zeigt die Ergebnisse an

    Args:
        Screen (Screen): Übergabeparameter
    """

    def __init__(self, **kwargs):
        super(ScreenFilenameChange, self).__init__(**kwargs)

    def on_enter(self, *args):
        Window.set_title(system.const.SCREEN_TITLE_FILENAME_CHANGE)
        return super().on_enter(*args)


class ScreenInfo(Screen):
    """
    Klasse zeigt die Ergebnisse an

    Args:
        Screen (Screen): Übergabeparameter
    """

    def __init__(self, **kwargs):
        super(ScreenInfo, self).__init__(**kwargs)

    def on_enter(self, *args):
        Window.set_title(system.const.SCREEN_TITLE_INFO)
        return super().on_enter(*args)


class ScreenConfiguration(Screen):
    """
    Klasse zeigt die Ergebnisse an

    Args:    def __init__(self, **kwargs):
        super(ScreenTemplate, self).__init__(**kwargs)

        Screen (Screen): Übergabeparameter
    """

    def __init__(self, **kwargs):
        super(ScreenConfiguration, self).__init__(**kwargs)

    def on_enter(self, *args):
        Window.set_title(system.const.SCREEN_TITLE_CONFIGURATION)
        return super().on_enter(*args)


class ScreenManagerContainer(ScreenManager):
    """_summary_

    Args:
        ScreenManagerContainer (_type_): _description_
    """


class ViewLayer(GridLayout):
    """_summary_

    Args:
        GridLayout (_type_): _description_
    """


# End-of-file (EOF)
