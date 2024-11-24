from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.actionbar import ActionButton
from kivy.uix.label import Label
from kivy.uix.widget import Widget

Builder.load_string("""
<ViewTooltip>:
    size_hint: None, None
    size: self.texture_size[0]+5, self.texture_size[1]+5
    canvas.before:
        Color:
            rgb: 0.2, 0.2, 0.2
        Rectangle:
            size: self.size
            pos: self.pos
""")

class ViewTooltip(Label):
    pass

class Tooltip(Widget):

    label = ViewTooltip(text="My Tooltip")
    
    def __init__(self, **kwargs):
        """
        _summary_
        """        
        super(Tooltip, self).__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos_over)
        
    def on_mouse_pos_over(self, *args):
        """
        _summary_
        """        
        if not self.get_root_window():
            return 
        
        pos = args[1]
        self.label.pos = pos
        Clock.unschedule(self.display_tooltip) # cancel scheduled event since I moved the cursor
        self.close_tooltip() # close if it"s opened
        if self.collide_point(*self.to_widget(*pos)):
            Clock.schedule_once(self.display_tooltip, 1)

    def close_tooltip(self, *args):
        """_summary_
        """                
        print("Tooltip-Text close: " + self.label.text)
        Window.remove_widget(self.label)

    def display_tooltip(self, *args):
        """_summary_
        """      
        print("Tooltip-Text display: " + self.label.text)  
        Window.add_widget(self.label)
    
    @property    
    def tooltip_text(self):
        """_summary_

        Args:
            text (_type_): _description_
        """        
        return self.label.text
    
    @tooltip_text.setter    
    def tooltip_text(self, text):
        """_summary_

        Args:
            text (_type_): _description_
        """        
        print("SetToolTip: " + text)
        self.label.text = text
# End-of-file (EOF)
