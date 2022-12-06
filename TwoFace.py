import arcade

from Criminal import Criminal

MOD = 1
class TwoFace(Criminal):
    #sets a different
   def __init__(self, texture):
       super().__init__(texture)
       self.health = (2 - MOD)
