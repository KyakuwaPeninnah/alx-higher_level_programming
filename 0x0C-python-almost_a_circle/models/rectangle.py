#!/usr/bin/python3
"""Module Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Class rectangle inheriting attributes of the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor that initializes Rectangle instances"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

  @property
  def width(self):
	  """Retrives width attribute"""
		 return self.__width

		 def height(self):
            """Retrives height attribute"""
                  return self.__height

		  def x(self):
           """Retrives x attribute"""
             return self.__x

	def y(self):
           """Retrives y attribute"""
                   return self.__y

		   @width.setter
		 def width(self, value):
			 """sets the width attribute"""
				 if not isinstance(value, int):
					 raise TypeError("width must be an integer")
				if value <= 0:
				  raise ValueError("width must be > 0")
				self.__width = value		
	 	@height.setter

	     def height(self, value): 
		     """sets the height attribute"""
                        if not isinstance(value, int):  
				raise TypeError("height must be an integer")
 	                                 if value <= 0:
	  raise ValueError("height must be > 0")

	    @x.setter
                   def x(self, value):
                           """sets the x attribute"""
                                   if not isinstance(value, int):
                                           raise TypeError("x must be an integer")
                                  if value <= 0:
                                    raise ValueError("x must be > 0")
                                  self.__x = value

		 @y.setter
		       def y(self, value):
	 	"""sets the y attribute"""
                                   if not isinstance(value, int):
                                           raise TypeError("y must be an integer")
                                if value <= 0:
		raise ValueError("y must be > 0")
                                self.__y = value
