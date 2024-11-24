
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.properties import BooleanProperty, ObjectProperty
from kivy.uix.widget import Widget


class MouseOver(Widget):

    __inside = BooleanProperty(False)
    border_point = ObjectProperty(None)

    def __init__(self, **kwargs):
        """
        _summary_
        """        
        super(MouseOver, self).__init__(**kwargs)
        self.register_event_type("on_enter")
        self.register_event_type("on_leave")
        Window.bind(mouse_pos=self.on_mouse_pos_over)
        
    def on_mouse_pos_over(self, *args):
        """
        _summary_
        """        
        if not self.get_root_window():
            return 
        
        pos = args[1]
        is_inside = self.collide_point(*self.to_widget(*pos))
        if self.__inside == is_inside:
            return
        
        self.__inside = is_inside
        if is_inside:
            self.dispatch("on_enter")
        else:
            self.dispatch("on_leave")
    
    def on_enter(self):
        """
        _summary_
        """        
        self.opacity = 1.0

    def on_leave(self):
        """
        _summary_
        """        
        self.opacity = 0.6
            
Factory.register("MouseOver", MouseOver)
# End-of-file (EOF)

