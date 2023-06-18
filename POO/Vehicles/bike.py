from typeguard import typechecked
from vehicle import Vehicle


@typechecked
class Bike(Vehicle):
    def __init__(self):
        super().__init__()

    @staticmethod
    def wheelie():
        print("""\
                                     o          _        _            _          
                        _o          /\_       _ \\\\o     (_)\__/o     (_)         
                      _< \_        _>(_)     (_)/<_       \_| \      _|/' \/     
                     (_)>(_)      (_)            (_)      (_)       (_)'  _\o_   
                     --------^     ---^---   ---^---     -------    -----------
        """)

