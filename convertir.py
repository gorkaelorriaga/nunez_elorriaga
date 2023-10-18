class CheckErrors:
    def check_is_number(self,value_or_values)->list:
        '''Convierte un valor o los valores de un iterable a float.
        
        Params:
            - value_or_values: valor/iterable.
            
        Devuelve:
            - Lista con el Elem o los Elems.'''
        if not self.check_input_type(value_or_values)or(self.check_input_type(value_or_values)and value_or_values and len([value_or_values])==1):
            value_or_values=[float(value_or_values)] #Convertirlo en lista evita errores en el for de debajo sea cual sea su longitud.
        for i in range(len(value_or_values)): #Si es 1 solo lo hará para ese valor. #Si es Str todos sus elementos deben ser Nums para que el Str completo lo sea.
            value_or_values[i]=float(value_or_values[i])
        return value_or_values
    def check_input_type(self,value_or_values)->bool:
        '''Comprueba si un input es Str o no.
        
        Params:
            - value_or_values: input.
            
        Devuelve:
            - Bool.'''
        if type(value_or_values)==str:
            return False
        else:
            return True


#class Convertir:
    