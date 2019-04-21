from datetime import datetime

class Contacto:
	def __init__(self, nombre, apellido, email, telefono):
		self.nombre = nombre
		self.apellido = apellido
		self.email = email
		self.telefono = telefono

	def get_full_name(self):
		return self.nombre + " " + self.apellido

contacto = Contacto(nombre="Miguel", apellido="Cadenas", email="maraz@maraz.es", telefono="telefono",)

print(contacto.nombre)
print(contacto.get_full_name())


