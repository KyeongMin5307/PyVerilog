from .PortIn import PortIn

class PortClk(PortIn):
    def __init__(self, attrs):
        attrs['width'] = 1
        PortIn.__init__(self, attrs)
