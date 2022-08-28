class Marca:
    def __init__(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre


class TV:
    numTV = 0
    _canal = 1
    _precio = 500
    _volumen = 1
    def __init__(self, marca:Marca, estado, control:Control):
        self.marca = marca
        self.estado = estado
        self.control = control
    
    @classmethod
    def getNumTV(self):
        return cls.numTV

    @classmethod
    def setNumTV(self, numTV):
        cls.numTV = numTV

    def getCanal(self):
        return self._canal

    def setCanal(self, canal):
        if(canal > 0 and canal <= 120 and estado == True):
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
        if(volumen >= 0 and volumen <= 7 and estado == True):
            self._volumen = volumen

    def getControl(self):
        return self.control

    def setControl(self, control):
        self.control = control

    def getEstado(self):
        return self.estado
    
    def setEstado(self, estado):
        self.estado = estado

    def turnOn():
        estado = True

    def turnOff():
        estado = False

    def canalUp():
        if(canal < 120 and estado == True):
            self._canal += 1

    def canalDown():
        if(canal > 1 and estado == True):
            self._canal -= 1

    def volumenUp():
        if(volumen < 7 and estado == True):
            self._volumen += 1

    def volumenDown():
        if(canal >= 1 and estado == True):
            self._canal -= 1


class Control:
    def __init__(self, tv:TV):
        self._tv = tv

    def getTv():
        return self._tv = tv

    def setTv(self, tv):
        self._tv = tv
    
    def turnOn():
        tv.turnOn()

    def turnOff():
        tv.turnOff()

    def canalUp():
        tv.canalUp()

    def canalDown():
        tv.canalDown()

    def volumenUp():
        tv.volumenUp()

    def volumenDown():
        tv.volumenDown()

    def setCanal(canal):
        tv.setCanal(canal)

    def enlazar(self, TV:tv):
        tv.setControl(self)




