from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import UsersManager



class Users(AbstractUser):
    name = None
   
    email = models.EmailField(max_length=50, unique=True)
    date_joined = models.DateTimeField(verbose_name='Dia de Union', auto_now_add=True)

    is_profesor = models.BooleanField(verbose_name='Profesor', default=False)
    is_estudiante = models.BooleanField(verbose_name='Estudiante', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UsersManager()
        
    def __str__(self):
        return self.email


class Titulo(models.Model):
    titulo = models.CharField(max_length=20,unique=True)

    class Meta:
        verbose_name = ('Título')
        verbose_name_plural = ('Títulos')
        ordering = ('titulo',)

    def __str__(self):
        return self.titulo



class Categoria_Cientifica(models.Model):
    nombre = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'Categoría Científica'
        verbose_name_plural = 'Categorías Científicas'
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

 


class Categoria_Docente(models.Model):
    nombre = models.CharField(max_length=120, unique=True)

    class Meta:
        verbose_name = ('Categoría Docente')
        verbose_name_plural = ('Categorías Docentes')
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    curso = models.CharField(max_length=50, verbose_name='Curso',unique=True)

    class Meta:
        verbose_name = ('Curso')
        verbose_name_plural = 'Cursos'
        ordering = ('curso',)

    def __str__(self):
        return self.curso


class Semestre(models.Model):
    semestres = (
        ('Primero', 'Primero'),
        ('Segundo', 'Segundo'),
    )
    semestre = models.CharField(max_length=20, choices=semestres)

    class Meta:
        ordering = ('semestre',)

    def __str__(self):
        return self.semestre


class Semestre_Cursado(models.Model):
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, related_name='semestres', on_delete=models.CASCADE)

    class Meta:
        ordering = ('curso',)

    def __str__(self):
        return '%s %s' % (self.semestre, self.curso)

  

class Tipo_Curso(models.Model):
    cursos = (
        ('Diurno', 'Diurno'),
        ('Encuentro', 'Encuentro'),
        ('Distancia', 'Distancia'),
    )
    nombre = models.CharField(max_length=50, choices=cursos)
    
    class Meta:
        verbose_name = ('Tipo de Curso')
        verbose_name_plural = ('Tipos de Cursos')
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre



class Plan_Estudio(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    # tipo_curso = models.ForeignKey(Tipo_Curso,on_delete=models.SET_NULL,blank=True,null=True)
    curso_emp = models.ForeignKey(Curso, verbose_name='Curso de Comienzo', on_delete=models.CASCADE,
                                  related_name='plans')

    # anno = models.ForeignKey(Anno, on_delete=models.CASCADE, related_name='plans')

    class Meta:
        verbose_name = u'Plan de Estudio'
        verbose_name_plural = u'Planes de Estudio'
        ordering = ('nombre',)

    def __str__(self):
        return '%s' % (self.nombre,)



class ProfesorPerfil(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    telefono = models.CharField(verbose_name='Teléfono', max_length=20, blank=True, null=True)
    movil = models.CharField(verbose_name='Teléfono Móvil', max_length=20, blank=True, null=True)
    categoria_doc = models.ForeignKey(Categoria_Docente, related_name='profesores', verbose_name=u'Categoría Docente',
                                      on_delete=models.SET_NULL, blank=True, null=True)
    categorias_cientficas = models.ManyToManyField(Categoria_Cientifica, related_name='profesores_cat_cientifica')
    titulo = models.ForeignKey(Titulo, related_name='profesores', on_delete=models.SET_NULL, blank=True, null=True)


    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):
        return self.user.name 


   



class Responsabilidades(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    peso = models.IntegerField(verbose_name='Peso de Responsabilidad')

    # profes_resp = models.ManyToManyField(User,through=Profe_Responsabilidades)

    class Meta:
        verbose_name = 'Responsabilidad'
        verbose_name_plural = 'Responsabilidades'
        ordering = ('peso',)

    def __str__(self):
        return self.nombre

 


class Profe_Responsabilidades(models.Model):
    responsabilidad = models.ForeignKey(Responsabilidades, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Users, related_name='funciones', related_query_name='funcion',
                                 verbose_name='Profesor Responsable',
                                 on_delete=models.CASCADE)

    class Meta:
        ordering = ('responsabilidad',)


class Disciplina(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    jefe_disciplina = models.ForeignKey(Profe_Responsabilidades, related_name='disciplinas',
                                        related_query_name='disciplina',
                                        verbose_name='Jefe de Disciplina', on_delete=models.SET_NULL,
                                        blank=True,
                                        null=True, )
    def __str__(self):
        return self.nombre


class Carrera(models.Model):
    carrera = models.CharField(max_length=50, verbose_name='Carrera', unique=True)
    jefe_departamento = models.ForeignKey(Profe_Responsabilidades,
                                          on_delete=models.SET_NULL,
                                          blank=True,
                                          null=True,
                                          verbose_name='Jefe de Departamento',
                                          related_name='carrera_jefedepartamento')
    segundo_jefe = models.ForeignKey(Profe_Responsabilidades,
                                     on_delete=models.SET_NULL,
                                     blank=True,
                                     null=True,
                                     verbose_name='Segundo Jefe de Departamento',
                                     related_name='carrera_segundo_jefe')
    coordinador = models.ForeignKey(Profe_Responsabilidades,
                                    on_delete=models.SET_NULL,
                                    blank=True,
                                    null=True,
                                    verbose_name='Coordinador de Carrera',
                                    related_name='carrera_coordinador')

    def __str__(self):
        return self.carrera


class Anno(models.Model):
    anno = models.CharField(max_length=50, verbose_name='Año',unique=True)

    def __str__(self):
        return self.anno


class Anno_Cursado(models.Model):
    anno = models.ForeignKey(Anno, on_delete=models.CASCADE, related_name='annos_cursados', verbose_name='Año')
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='annos')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='annos')
    tipo_curso = models.ForeignKey(Tipo_Curso, verbose_name='Tipo de Curso', on_delete=models.CASCADE,
                                   related_name='annos')
    plan = models.ForeignKey(Plan_Estudio, on_delete=models.CASCADE, related_name='annos',
                             verbose_name='Plan de Estudio')
    principal_anno = models.ForeignKey(Profe_Responsabilidades,
                                       on_delete=models.SET_NULL,
                                       blank=True,
                                       null=True,
                                       related_name='annos_ppa',
                                       verbose_name='Profesor Principal de Año')

    class Meta:
        verbose_name = ('Año')
        verbose_name_plural = 'Años'
        ordering = ('-curso',)
        unique_together = ('anno','carrera','curso','plan','tipo_curso')



    def __str__(self):
        return '%s %s %s' % (self.anno, self.carrera, self.curso)


class Asignatura(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.nombre,)


class Asignatura_Plan(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name='asignaturas_plan')
    disciplina = models.ForeignKey(Disciplina, related_name='asignaturas', related_query_name='asignatura',
                                   verbose_name='Disciplina',
                                   on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan_Estudio, on_delete=models.CASCADE, related_name='asignaturas_plan')
    tipo_curso = models.ForeignKey(Tipo_Curso, verbose_name='Tipo de Curso', on_delete=models.CASCADE,
                                   related_name='asignaturas')
    cantidad_horas_plan = models.IntegerField(verbose_name='Horas por Plan')
    semestre = models.ForeignKey(Semestre, on_delete=models.SET_NULL, blank=True, null=True)
    anno = models.ForeignKey(Anno, related_name='asiganturas', verbose_name=u'Año', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.asignatura, self.plan)


class Grupo(models.Model):
    grupo = models.CharField(max_length=10, verbose_name='Grupo')
    anno = models.ForeignKey(Anno_Cursado, related_name='grupos',
                             related_query_name='grupo', verbose_name='Año', on_delete=models.CASCADE)
    profesor_guia = models.ForeignKey(Profe_Responsabilidades,
                                      on_delete=models.SET_NULL,
                                      related_name='grupos',
                                      blank=True,
                                      null=True,
                                      verbose_name='Profesor Guía')


    def __str__(self):
        return '%s %s' % (self.grupo, self.anno)



class Subgrupo(models.Model):
    subgrupo = models.CharField(max_length=10, verbose_name='Subgrupo')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='subgrupos')

    def __str__(self):
        return self.subgrupo


class ProfesorAsignatura(models.Model):
    profesor = models.ForeignKey(ProfesorPerfil, on_delete=models.CASCADE, related_name='impartidas',
                                 related_query_name='impartida')
    asignatura = models.ForeignKey(Asignatura_Plan, on_delete=models.CASCADE, related_name='impartidas',
                                   related_query_name='impartida')
    curso = models.ForeignKey(Semestre_Cursado, verbose_name='Curso', on_delete=models.CASCADE,
                              related_name='impartidas')

    created_by = models.ForeignKey(Users,
                                   on_delete=models.CASCADE,
                                   related_name='docencias_created')

    horas_conferencias = models.IntegerField(verbose_name='Cantidad de Horas Conferencia', blank=True, null=True,
                                             default=0)
    cant_grupos_conferencias = models.IntegerField(verbose_name='Cantidad Grupos Conferencia', blank=True, null=True,
                                                   default=0)

    horas_cp = models.IntegerField(verbose_name='Cantidad de Horas Clase Practica', blank=True, null=True, default=0)
    cant_grupos_cp = models.IntegerField(verbose_name='Cantidad Grupos Clase Practica', blank=True, null=True,
                                         default=0)
    horas_cpc = models.IntegerField(verbose_name='Cantidad de Horas Clase Practica Computadoras', blank=True, null=True,
                                    default=0)
    cant_grupos_cpc = models.IntegerField(verbose_name='Cantidad Grupos Clase Practica Computadoras', blank=True,
                                          null=True,
                                          default=0)
    horas_lab = models.IntegerField(verbose_name='Cantidad de Horas Laboratorio', blank=True, null=True, default=0)
    cant_grupos_lab = models.IntegerField(verbose_name='Cantidad Grupos Laboratorio', blank=True,
                                          null=True,
                                          default=0)
    horas_taller = models.IntegerField(verbose_name='Cantidad de Horas Taller', blank=True, null=True, default=0)
    cant_grupos_taller = models.IntegerField(verbose_name='Cantidad Grupos Taller', blank=True,
                                             null=True,
                                             default=0)
    horas_seminarios = models.IntegerField(verbose_name='Cantidad de Horas Seminario', blank=True, null=True, default=0)
    cant_grupos_seminario = models.IntegerField(verbose_name='Cantidad Grupos Seminario', blank=True, null=True,
                                                default=0)


class EstudiantePerfil(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True, related_name='estudiantes')
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='estudiantes')

    def __str__(self):
        return self.user


class Relacion (models.Model):
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Relacionb(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    plan_Estudio = models.ForeignKey(Plan_Estudio, on_delete=models.CASCADE)

class Relacionc(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    categoria_doc = models.ForeignKey(Categoria_Docente, on_delete=models.CASCADE)
    categorias_cientficas = models.ManyToManyField(Categoria_Cientifica, on_delete=models.CASCADE)
    titulo = models.ManyToManyField(Titulo, on_delete=models.CASCADE)

class Relacion(models.Model):
    profesor= models.OneToOneField(Users, on_delete=models.CASCADE)
    responsabilidad = models.ForeignKey(Categoria_Docente, on_delete=models.CASCADE)
 



class RelacionInLine(admin.TabularInline):
    model = Relacion
    extra = 1
