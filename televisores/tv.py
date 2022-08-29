class TV:
    numTV = 0
    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.control = None
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        TV.numTV += 1
    
    @classmethod
    def getNumTV(cls):
        return cls.numTV

    @classmethod
    def setNumTV(cls, numTV):
        cls.numTV = numTV

    def getCanal(self):
        return self._canal

    def setCanal(self, canal):
        if(canal > 0 and canal <= 120 and self.estado == True):
            self._canal = canal
    
    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio):
        self._precio = precio

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getVolumen(self):
        return self._volumen

    def setVolumen(self, volumen):
        if(volumen >= 0 and volumen <= 7 and self.estado == True):
            self._volumen = volumen

    def getControl(self):
        return self.control

    def setControl(self, control):
        self.control = control

    def getEstado(self):
        return self.estado
    
    def setEstado(self, estado):
        self.estado = estado

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def canalUp(self):
        if(self._canal < 120 and self.estado == True):
            self._canal += 1

    def canalDown(self):
        if(self._canal > 1 and self.estado == True):
            self._canal -= 1

    def volumenUp(self):
        if(self._volumen < 7 and self.estado == True):
            self._volumen += 1

    def volumenDown(self):
        if(self._volumen >= 1 and self.estado == True):
            self._volumen -= 1