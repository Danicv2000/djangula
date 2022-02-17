from rest_framework import serializers
from .models import Semestre,Semestre_Cursado,Tipo_Curso,Plan_Estudio,EstudiantePerfil,Curso,ProfesorAsignatura,Grupo,Asignatura_Plan,Asignatura,Anno_Cursado,Disciplina,Profe_Responsabilidades,ProfesorPerfil, Anno, Responsabilidades, Categoria_Docente, Categoria_Cientifica, Titulo, Carrera, Users
from rest_framework.authtoken.models import Token


class UsersSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Users
        fields = ('id', 'name', 'email', 'is_profesor', 'is_estudiante' )


class TituloSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Titulo
        fields = ('id','titulo' )


class Categoria_CientificaSerializer(serializers.ModelSerializer): 
    class Meta:
        model =  Categoria_Cientifica
        fields = ('id','nombre' )

class Categoria_DocenteSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Categoria_Docente
        fields = ('id','nombre' )

class SemestreSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Semestre
        fields = ('id',' emestre' )

class CursoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Curso
        fields = ('id','curso' )

class Semestre_CursadoSerializer(serializers.ModelSerializer): 
    semestre = SemestreSerializer(many=True, read_only=True)
    curso  = CursoSerializer(many=True, read_only=True)
    class Meta:
        model = Semestre_Cursado
        fields = ('id', 'docencias','curso')

class Tipo_CursoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Tipo_Curso
        fields = ('id','nombre' )

class Plan_EstudioSerializer(serializers.ModelSerializer): 
    curso  = CursoSerializer(many=True, read_only=True)
    class Meta:
        model = Plan_Estudio
        fields = ('id', 'nombre','curso')


class ProfesorPerfilSerializer(serializers.ModelSerializer): 
    user = UsersSerializer(many=True, read_only=True)
    categoria_doc  = Categoria_DocenteSerializer(many=True, read_only=True)
    categorias_cientficas = Categoria_CientificaSerializer(many=True, read_only=True)
    titulo = TituloSerializer(many=True, read_only=True)
    class Meta:
        model = ProfesorPerfil
        fields = ('id', 'telefono',' movil', 'user','categoria_doc', 'categorias_cientficas','titulo')


class ResponsabilidadesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Responsabilidades
        fields = ('id','nombre','peso' )

class Profe_ResponsabilidadesSerializer(serializers.ModelSerializer): 
    responsabilidad = ResponsabilidadesSerializer(many=True, read_only=True)
    profesor  = UsersSerializer(many=True, read_only=True)
    class Meta:
        model = Profe_Responsabilidades
        fields = ('id', ' responsabilidad',' profesor')

class DisciplinaSerializer(serializers.ModelSerializer): 
    jefe_disciplina = Profe_ResponsabilidadesSerializer(many=True, read_only=True)
    class Meta:
        model = Disciplina
        fields = ('id', ' nombre',' jefe_disciplina')


class CarreraSerializer(serializers.ModelSerializer): 
    jefe_departamento = Profe_ResponsabilidadesSerializer(many=True, read_only=True)
    segundo_jefe = Profe_ResponsabilidadesSerializer(many=True, read_only=True)
    coordinador = Profe_ResponsabilidadesSerializer(many=True, read_only=True)
    class Meta:
        model = Carrera
        fields = ('id', 'nombre',' jefe_departamento', 'segundo_jefe', 'coordinador')


class AnnoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Anno
        fields = ('id','anno' )


class Anno_CursadoSerializer(serializers.ModelSerializer): 
    anno = AnnoSerializer(many=True, read_only=True)
    carrera  = CarreraSerializer(many=True, read_only=True)
    curso = CursoSerializer(many=True, read_only=True)
    tipo_curso = Tipo_CursoSerializer(many=True, read_only=True)
    plan = Plan_EstudioSerializer(many=True, read_only=True)
    principal_anno= Profe_ResponsabilidadesSerializer(many=True, read_only=True)
    class Meta:
        model = Anno_Cursado
        fields = ('id', 'anno','carrera', 'curso','tipo_curso', 'plan','principal_anno')


class AsignaturaSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Asignatura
        fields = ('id','nombre' )

class Asignatura_PlanSerializer(serializers.ModelSerializer): 
    asignatura = AsignaturaSerializer(many=True, read_only=True)
    disciplina = DisciplinaSerializer(many=True, read_only=True)
    plan = Plan_EstudioSerializer(many=True, read_only=True)
    tipo_curso = Tipo_CursoSerializer(many=True, read_only=True)
    semestre = SemestreSerializer(many=True, read_only=True)
    anno= AnnoSerializer(many=True, read_only=True)
    class Meta:
        model = Asignatura_Plan
        fields = ('id', 'cantidad_horas_plan','asignatura', 'disciplina','semestre',' plan', 'tipo_curso','anno',' plan')


class GrupoSerializer(serializers.ModelSerializer): 
    anno = Anno_CursadoSerializer(many=True, read_only=True)
    profesor_guia = Profe_ResponsabilidadesSerializer(many=True, read_only=True)
    class Meta:
        model = Grupo
        fields = ('id', 'grupo','anno', 'profesor_guia')


class ProfesorAsignaturaSerializer(serializers.ModelSerializer): 
    profesor = ProfesorPerfilSerializer(many=True, read_only=True)
    asignatura = Asignatura_PlanSerializer(many=True, read_only=True)
    curso = Semestre_CursadoSerializer(many=True, read_only=True)
    created_by = UsersSerializer(many=True, read_only=True)
    class Meta:
        model = ProfesorAsignatura
        fields = ('id','horas_conferencias','cant_grupos_conferencias', 'horas_cp', 'cant_grupos_cp','horas_cpc','cant_grupos_cpc', 'horas_lab', 'cant_grupos_lab','horas_taller','cant_grupos_taller', 'horas_seminarios', 'cant_grupos_seminario', 'profesor','asignatura', 'curso', 'created_by')

class EstudiantePerfilSerializer(serializers.ModelSerializer): 
    user = UsersSerializer(many=True, read_only=True)
    carrera = CarreraSerializer(many=True, read_only=True)
    class Meta:
        model = EstudiantePerfil
        fields = ('id', 'user','carrera')

