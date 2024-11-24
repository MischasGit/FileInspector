"""
FileInspector



"""

import kivy
from kivy.app import App

import system.const
from controller.controllerlayer import ControllerLayer

kivy.require("2.2.0")


class StartView(App):
    """
    StartView

    Args:
        App (_type_): _description_

    Returns:
        _type_: _description_
    """

    __controller = None

    def __init__(self, **kwargs):
        """
        _summary_
        """
        super().__init__(**kwargs)
        self.__controller = ControllerLayer()

    def build(self):
        """_summary_

        Returns:
            _type_: _description_
        """

        App.title = system.const.SCREEN_TITLE_FIND_DUPLICATES

        return self.__controller.view


if __name__ == "__main__":
    StartView().run()
# End-of-file (EOF)
