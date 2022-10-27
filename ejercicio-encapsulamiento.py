# Crear una clase llamada Persona en la cual se guarden: nombre, fecha_nacimiento, nacionalidad y dni. Crear otra clase llamada Alumno que va a heredar la clase Persona y ademas va a tener sus atributos: num_seguro, num_emergencia, matriculado (Boolean), el alumno tendra un metodo llamado mostrar_datos y ademas otro metodo llamado matricular en el cual si esta matriculado no se podra matricular, caso contrario, si. Y tambien tener otra clase Profesor que va a tener cta_pago y maestria (str) y el profesor puede mostrar su cta_pago y ademas si tiene maestria al momento de mostrar la cta_pago indicar que se le tiene que agregar 100 soles

class Persona:
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.dni = dni

    def mostrar_datos(self):
        return {
            'nombre': self.nombre,
            'fecha_nacimiento': self.fecha_nacimiento,
            'nacionalidad': self.nacionalidad,
            'dni': self.dni
        }

class Alumno(Persona):
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni, num_seguro, num_emergencia, matriculado):
        self.num_seguro = num_seguro
        self.num_emergencia = num_emergencia
        self.matriculado = matriculado
        super().__init__(nombre, fecha_nacimiento, nacionalidad, dni)
    
    def mostrar_datos(self):
        resumen = super().mostrar_datos()
        resumen['num_seguro'] = self.num_seguro
        resumen['num_emergencia'] = self.num_emergencia
        resumen['matriculado'] = self.matriculado
        return resumen
    
    def matricular(self):
        if self.matriculado:
            print('El alumno ya esta matriculado previamente')
        else:
            self.matriculado = True
            print('Se acaba de matricular al alumno')

class Profesor(Persona):
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni, cta_pago, maestria):
        self.cta_pago = cta_pago
        self.maestria = maestria
        super().__init__(nombre, fecha_nacimiento, nacionalidad, dni)
    
    def mostrar_datos(self):
        resumen = super().mostrar_datos()
        resumen['cta_pago'] = self.cta_pago
        resumen['maestria'] = self.maestria
        return resumen
    
    def mostrar_cuenta_pago(self):
        print('La cuenta pago del docente es:',self.cta_pago)
        if type(self.maestria) == str:
            print('Se le debe agregar 100 soles por tener maestria')
        print(self.mostrar_datos())

alumno01= Alumno('Alejandro Taquia','24-01-2000','peruana',44849098,123456,993707692,False)
alumno02= Alumno('Joel Taquia','24-01-1990','espanol',74849098,123457,993707692,True)
print(alumno01.mostrar_datos())
print(alumno02.mostrar_datos())
alumno01.matricular()
alumno02.matricular()
print(alumno01.mostrar_datos())
print(alumno02.mostrar_datos())

print('\n')

profesor01 = Profesor('Juan Perez','24-01-2000','peruana',44849098,'473-1231','Tecnologia')
profesor02 = Profesor('Karina Macedo','09-04-1989','peruana',46196076,'473-1234','Educacion')
profesor03 = Profesor('Alberto Barros','24-01-1969','ecuatoriana',49874512,'673-1231',False)

profesor01.mostrar_cuenta_pago()
profesor02.mostrar_cuenta_pago()
profesor03.mostrar_cuenta_pago()