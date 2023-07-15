from django.db import models


class Vehiculo(models.Model):
    marcas = [["Fiat", "Fiat"], ["Chevrolet", "Chevrolet"], ["@Ford", "Ford"],
              ["Toyota", "Toyota"]]
    ##[["valor que se guarda", "Valor que ve el Usuario"]]

    marca = models.CharField(max_length=20, choices=marcas, default="@Ford")

    modelo = models.CharField(max_length=100)

    serial_carroceria = models.CharField(max_length=50)

    serial_motor = models.CharField(max_length=50)

    categorias = [["Particular", "Particular"], ["transporte", "transporte"],
                  ["carga", "carga"]]

    categoria = models.CharField(max_length=20,
                                 choices=categorias,
                                 default="Particular")

    precio = models.PositiveIntegerField(default=0, help_text="En CLPesos")

                
  
    pub_date = models.DateTimeField(auto_now_add=True,
                                    help_text="Fecha Creacion")
    ##auto_now_add >Automatically set the field to now when the object is first created. Useful for creation of timestamps
    last_edit = models.DateTimeField(auto_now=True,
                                     help_text="Fecha ultima modificación")

    ## uto_now is to:[automatically] set the field to now every time the object is saved. Useful for "last-modified" timestamps

    class Meta:
        permissions = [("visualizar_catalogo", "Visualizar Catalogos")]

    def condicion_precio(self):
      #programo condiciones
      #retorna valores en base a la condiciones
      if self.precio >=0 and self.precio <=10000:
        return "Bajo"
      elif self.precio >10000 and self.precio <=30000:
        return"medio"
      
      else:
        return "alto"