from django.db import models

# Create your models here.
class Medico(models.Model):
    idMedico = models.IntegerField(primary_key=True)
    cedulaMed = models.IntegerField()
    nombreMed = models.CharField(max_length=15)
    apellidoMed = models.CharField(max_length=15)
    telefonoMed = models.IntegerField()
    correoMed = models.EmailField()
    hojaDeVidaMed = models.BinaryField()
    codEspecialidadM = models.IntegerField()

class Especialidad(models.Model):
    codEspecialidad = models.BigIntegerField()
    Especialidad = models.CharField(max_length=30)
    
class Servicio(models.Model):
    codigoCita = models.IntegerField(primary_key=True)
    fechaCM = models.DateField()
    horaCM = models.DateTimeField()
    descripcionCM = models.TextField()
    codTipoCitaC = models.IntegerField()
    confirmacionCM = models.CharField(max_length=5)
    idPacienteC = models.IntegerField()
    idMedicoC = models.IntegerField()

class TipoServicio(models.Model):
    codTipoCita = models.BigIntegerField()
    tipoCita = models.BigIntegerField()
    
class Paciente(models.Model):
    idPaciente = models.IntegerField(primary_key=True)
    cedulaPac = models.IntegerField()
    nombrePac = models.CharField(max_length=15)
    apellidoPac =  models.CharField(max_length=15)
    edadPac = models.IntegerField()
    telefonoPac = models.IntegerField()
    correoPac = models.EmailField()
    direccionPac = models.CharField(max_length=30)
    
class HistorialClinico(models.Model):
    codigoHistorial = models.IntegerField(primary_key=True)
    descripcionEventos = models.TextField()
    codAlergiaH = models.IntegerField()
    codMedicamentosH = models.IntegerField()
    codExamenesH = models.IntegerField()
    idPacienteH = models.IntegerField()
    
class Proveedor(models.Model):
    idProveedor = models.IntegerField()
    cedulaProv = models.BigIntegerField()
    nombreProv = models.CharField(max_length=15)
    apellidoProv = models.CharField(max_length=15)
    telefono = models.IntegerField()
    
class ProveedorProducto(models.Model):
    idProveedorPP = models.BigIntegerField()
    codigoProductoPP = models.BigIntegerField()
    
class Producto(models.Model):
    codigoProducto = models.IntegerField()
    nombreProd = models.CharField(max_length=15)
    descripcionProd = models.TextField()
    cantidadProd = models.IntegerField()
    precioProd = models.IntegerField()
    
class HistorialClinico(models.Model):
    codigoHistorial = models.BigIntegerField()
    descripcionEventos = models.TextField()
    codAlergiaH = models.IntegerField()
    codMedicamentosH = models.IntegerField()
    codEnfermedadesH = models.IntegerField()
    codExamenesH = models.IntegerField()
    idPacienteH = models.IntegerField()
    
class Alergias(models.Model):
    codAlergia = models.BigIntegerField()
    tipoAlergia = models.CharField(max_length=20)
    descripcionAlergia = models.TextField()

class Medicamnetos(models.Model):
    codMedicacion = models.IntegerField()
    tipoMedicacion = models.CharField(max_length=30)
    descripcionMedicacion = models.TextField()
    
class Enfermedades (models.Model):
    codEnfermedades = models.IntegerField()
    tipoEnfermedades = models.CharField(max_length=30)
    descripcionEnfermedades = models.TextField()    
    
class Examenes(models.Model):
    codExamenes = models.IntegerField()
    tipoExamenes = models.CharField(max_length=30)
    descripcionExamenes = models.TextField()

class Reclamo(models.Model):
    codigoReclamo = models.IntegerField()
    fechaRec = models.DateField()
    codTipoReclamoR = models.IntegerField()
    descripcionRec = models.TextField()
    idPacienteR = models.BigIntegerField()
    idMedico = models.BigIntegerField()
    
class Tipo(models.Models):
    codTipoReclamo = models.IntegerField()
    tipoReclamo = models.CharField(max_length=30)
    
