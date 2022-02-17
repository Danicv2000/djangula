from django.contrib import admin
from .models import Semestre,Semestre_Cursado,Tipo_Curso,Plan_Estudio,EstudiantePerfil,Curso,ProfesorAsignatura,Grupo,Asignatura_Plan,Asignatura,Anno_Cursado,Disciplina,Profe_Responsabilidades,ProfesorPerfil, Anno, Responsabilidades, Categoria_Docente, Categoria_Cientifica, Titulo, Carrera, Users

from django.utils.translation import gettext as _

class UserAdmin(admin.ModelAdmin):
   

    list_display = ('id', 'name', 'email',)
    list_display_links = ('id', 'name', 'email',)

    search_fields = (
        'email',
        'name',
        
    )

    list_filter = (
        'is_active',
        'is_staff',
        'date_joined',
        'modified',
    )

    readonly_fields = ('date_joined', 'modified',)

admin.site.register(ProfesorPerfil)
admin.site.register(Semestre)
admin.site.register(Anno)
admin.site.register(Categoria_Cientifica)
admin.site.register(Categoria_Docente)
admin.site.register(Titulo)
admin.site.register(Responsabilidades)
admin.site.register(Carrera)
admin.site.register(Curso)
admin.site.register(Profe_Responsabilidades)
admin.site.register(Disciplina)
admin.site.register(Anno_Cursado)
admin.site.register(Asignatura)
admin.site.register(Asignatura_Plan)
admin.site.register(Grupo)
admin.site.register(ProfesorAsignatura,ProfesorAsignaturaAdmin)
admin.site.register(EstudiantePerfil)
admin.site.register(Plan_Estudio)
admin.site.register(Tipo_Curso)
admin.site.register(Semestre_Cursado)
      
admin.site.register(Users)