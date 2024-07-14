class Fraction:

    def __init__(self, numerator, denominator) :
       self._numerator = int(numerator)     # let exception happen
       self._denominator = int(denominator) # let exception happen

       if self._denominator == 0 :
           raise ZeroDivisionError("denominator can't be 0")    # raise exception
       
    def __repr__(self) :
       return str(self._numerator) + '/' + str(self._denominator)

    def __float__(self) :
        return self._numerator / self._denominator
    
