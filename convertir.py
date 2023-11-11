class CheckErrors:
    def __init__(self, value_or_values, measure_from, measure_to):
        self.value_or_values = value_or_values
        self.measure_from = measure_from
        self.measure_to = measure_to
        self.monedas = ["EURO", "DOLLAR"]
        self.longitud = ["KM", "HM", "DAM", "M", "DM", "CM", "MM"]
        self.area = ["HA","KM2","HM2", "DAM2", "M2", "DM2", "CM2", "MM2"]
        self.volumen = ["KM3","HM3", "DAM3", "M3", "DM3", "CM3", "MM3"]
        self.liquidos = ["KL", "HL", "DAL", "L", "DL", "CL", "ML"]
        self.medida = None
        self.check_is_number()

    def check_is_number(self):
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

class MedidaArea(CheckErrors):
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
                self.value_or_values[i] = self.value_or_values[i] * 100**(indice_medida2 - indice_medida1)
            else:
                self.value_or_values[i] = self.value_or_values[i] / 100**(indice_medida1 - indice_medida2)

        print(self.value_or_values)

class MedidaVolumen(CheckErrors):
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
                self.value_or_values[i] = self.value_or_values[i] * 1000**(indice_medida2 - indice_medida1)
            else:
                self.value_or_values[i] = self.value_or_values[i] / 1000**(indice_medida1 - indice_medida2)

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

class MedidaMonedas(CheckErrors):
    def __init__(self, value_or_values, measure_from, measure_to):
        super().__init__(value_or_values, measure_from, measure_to)

    def cambio_monedas(self):
        import requests
        for i in range(len(self.value_or_values)):
            url='https://api.api-ninjas.com/v1/convertcurrency?have='+self.measure_from+'&want='+self.measure_to+'&amount='+str(self.value_or_values[i])
            response=requests.get(url,headers={'X-API-KEY':'xRIFC4JjW7IMhQpsVbYs4Q==IwpSgRDfoQ4zHbV1'})
            #print(response.text)
            valor = ""
            inicio = 0
            elementos = ["e", ".", "+"]
            for caracter in response.text:
                if caracter.isnumeric():
                    inicio = 1
                    valor += caracter
                elif (inicio == 1 and caracter in elementos):
                    valor += caracter
                if caracter == ",":
                    break
            if valor == "":
                raise (Exception)
            try:
                valor = float(valor)
            except ValueError:
                print("La transformación entre monedas no ha sido posible\n")
            self.value_or_values[i] = valor

class MedidaTiempo(CheckErrors):
    def __init__(self, value_or_values, measure_from, measure_to):
        super().__init__(value_or_values, measure_from, measure_to)
    
    def year_month(self, value, mode):
        if (mode == 0):
            value *= 12
        else:
            value /= 12
        return (value)

    def month_week(self, value, mode):
        if (mode == 0):
            value *= 4
        else:
            value /= 4
        return (value)
    
    def week_day(self, value, mode):
        if (mode == 0):
            value *= 7
        else:
            value /= 7
        return (value)
    
    def day_hour(self, value, mode):
        if (mode == 0):
            value *= 24
        else:
            value /= 24
        return (value)
    
    def hour_minute(self, value, mode):
        if (mode == 0):
            value *= 60
        else:
            value /= 60
        return (value)
    
    def minute_second(self, value, mode):
        if (mode == 0):
            value *= 60
        else:
            value /= 60
        return (value)

    def cambio_tiempo(self):
        indice = 0
        for i in self.tiempo:
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
            indice_medida1_copy = indice_medida1
            indice_medida2_copy = indice_medida2
            if mode == 0:
                while indice_medida1_copy < indice_medida2_copy:
                    if (indice_medida1_copy == 0):
                        self.value_or_values[i] = self.year_month(self.value_or_values[i], mode)
                    elif (indice_medida1_copy == 1):
                        self.value_or_values[i] = self.month_week(self.value_or_values[i], mode)
                    elif (indice_medida1_copy == 2):
                        self.value_or_values[i] = self.week_day(self.value_or_values[i], mode)
                    elif (indice_medida1_copy == 3):
                        self.value_or_values[i] = self.day_hour(self.value_or_values[i], mode)
                    elif (indice_medida1_copy == 4):
                        self.value_or_values[i] = self.hour_minute(self.value_or_values[i], mode)
                    elif (indice_medida1_copy == 5):
                        self.value_or_values[i] = self.minute_second(self.value_or_values[i], mode)
                    indice_medida1_copy += 1
            else:
                while indice_medida2_copy > indice_medida1_copy:
                    if (indice_medida2_copy == 5):
                        self.value_or_values[i] = self.minute_second(self.value_or_values[i], mode)
                    elif (indice_medida2_copy == 4):
                        self.value_or_values[i] = self.hour_minute(self.value_or_values[i], mode)
                    elif (indice_medida2_copy == 3):
                        self.value_or_values[i] = self.day_hour(self.value_or_values[i], mode)
                    elif (indice_medida2_copy == 2):
                        self.value_or_values[i] = self.week_day(self.value_or_values[i], mode)
                    elif (indice_medida2_copy == 1):
                        self.value_or_values[i] = self.month_week(self.value_or_values[i], mode)
                    elif (indice_medida2_copy == 0):
                        self.value_or_values[i] = self.year_month(self.value_or_values[i], mode)
                    indice_medida2_copy -= 1

class Conversor(MedidaLongitud, MedidasLiquidos, MedidaArea, MedidaVolumen, MedidaMonedas, MedidaTiempo):
    def __init__(self, value_or_values, measure_from, measure_to):
        super().__init__(value_or_values, measure_from, measure_to)
        self.check_measures()
    
    def check_measures(self):
        #print("Entro")
        if self.measure_from in self.monedas and self.measure_to in self.monedas:
            #print("Es Monedas")
            self.cambio_monedas()
        elif (self.measure_from in self.longitud and self.measure_to in self.longitud):
            #print("Es Longitud")
            self.cambio_longitudes()
        elif (self.measure_from in self.liquidos and self.measure_to in self.liquidos):
            #print("Es Liquido")
            self.cambio_liquidos()
        elif (self.measure_from in self.tiempo and self.measure_to in self.tiempo):
            #print("Es Tiempo")
            self.cambio_tiempo()
        elif (self.measure_from in self.area and self.measure_to in self.area):
            self.cambio_areas()
        elif (self.measure_from in self.volumen and self.measure_to in self.volumen):
            self.cambio_volumenes()
        else:
            raise(Exception("La conversión que intenta realizar no es posible, compruebe que los valores son correctos y que ambas medidas pertenecen al mismo dominio\n"))
        return(self.value_or_values)