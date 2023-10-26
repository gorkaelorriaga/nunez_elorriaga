class CheckErrors:
    def __init__(self, value_or_values, measure_from, measure_to):
        self.value_or_values = value_or_values
        self.measure_from = measure_from
        self.measure_to = measure_to
        self.monedas = ["EURO", "DOLLAR"]
        self.longitud = ["KM", "HM", "DAM", "M", "DM", "CM", "MM"]
        self.liquidos = ["KL", "HL", "DAL", "L", "DL", "CL", "ML"]
        self.medida = None
        self.check_is_number()

    def check_is_number(self):
        '''Comprueba si un valor o un iterable de valores es convertible a numérico.
        
        Params:
            - value_or_values: valor/iterable.
            
        Devuelve:
            - True si se cumple y nada si no.'''
        if not self.check_input_type() or (self.check_input_type() == 1 and self.value_or_values and len([self.value_or_values])==1):
            self.value_or_values = [float(self.value_or_values)]
        for elem in self.value_or_values: #Si es 1 solo lo hará para ese valor. #Si es Str todos sus elementos deben ser Nums para que el Str completo lo sea.
            float(elem)
        self.check_measures()
        #return value_or_values
        
    def check_input_type(self)->int:
        if type(self.value_or_values)==str:
            return 0
        elif type(self.value_or_values)==int or type(self.value_or_values)==float:
            return 1
        else:
            return 2
        
    def check_measures(self):
        print("Entro")
        if self.measure_from in self.monedas and self.measure_to in self.monedas:
            print("Es Monedas")
        elif (self.measure_from in self.longitud and self.measure_to in self.longitud):
            print("Es Longitud")
        elif (self.measure_from in self.liquidos and self.measure_to in self.liquidos):
            print("Es Liquido")

class MedidaLongitud(CheckErrors):
    def __init__(self, value_or_values, measure_from, measure_to):
        super().__init__(value_or_values, measure_from, measure_to)
        self.cambio_medidas()

    def cambio_medidas(self):
        indice = 0
        for i in self.longitud:
            if self.measure_from == i:
                indice_medida1 = indice
            if self.measure_to == i:
                indice_medida2 = indice
            indice += 1
        
        if indice_medida1 < indice_medida2:
            mode = 0
        else:
            mode = 1
        
        for i in range(len(self.value_or_values)):
            if mode == 0:
                self.value_or_values[i] = self.value_or_values[i] * 10**(indice_medida2 - indice_medida1)
            else:
                self.value_or_values[i] = self.value_or_values[i] / 10**(indice_medida1 - indice_medida2)

        print(self.value_or_values)

class MedidasLiquidos(CheckErrors):
    def __init__(self, value_or_values, measure_from, measure_to):
        super().__init__(value_or_values, measure_from, measure_to)
        self.cambio_medidas()

    def cambio_medidas(self):
        indice = 0
        for i in self.liquidos:
            if self.measure_from == i:
                indice_medida1 = indice
            if self.measure_to == i:
                indice_medida2 = indice
            indice += 1
        
        if indice_medida1 < indice_medida2:
            mode = 0
        else:
            mode = 1
        
        for i in range(len(self.value_or_values)):
            if mode == 0:
                self.value_or_values[i] = self.value_or_values[i] * 10**(indice_medida2 - indice_medida1)
            else:
                self.value_or_values[i] = self.value_or_values[i] / 10**(indice_medida1 - indice_medida2)

        print(self.value_or_values)

#class Convertir:
    