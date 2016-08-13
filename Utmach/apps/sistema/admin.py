from django.contrib import admin

# Register your models here.
from models import * 

admin.site.register(Estudiante)
admin.site.register(Paralelo)
admin.site.register(Materia)
admin.site.register(Matricula)
admin.site.register(Nota)
admin.site.register(EstadoPersona)
admin.site.register(EstadoMatricula)
admin.site.register(Nivel)
admin.site.register(Periodo)
admin.site.register(Hora)
admin.site.register(TipoPersona)
admin.site.register(Persona)
admin.site.register(Docente)
admin.site.register(Sesion)