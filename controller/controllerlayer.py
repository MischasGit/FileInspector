from model.modellayer import ModelLayer
from view.viewlayer import ViewLayer


class ControllerLayer():
    """
    _summary_

    Returns:
        _type_: _description_
    """    
    
    __view = None
    __model = None
    
    def __init__(self):
        """
        _summary_
        """        
        self.__view = ViewLayer()
        self.__model = ModelLayer()
    
    @property
    def view(self):
        """
        _summary_
        """                
        return self.__view
    
    @property
    def model(self):
        """
        _summary_
        """        
        return self.__model
# End-of-file (EOF)
