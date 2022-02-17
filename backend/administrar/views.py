from django.shortcuts import render
from .serializers import UsersSerializer,TituloSerializer,Categoria_CientificaSerializer,Categoria_DocenteSerializer,SemestreSerializer,CursoSerializer,Semestre_CursadoSerializer,Tipo_CursoSerializer,Plan_EstudioSerializer,ProfesorPerfilSerializer,ResponsabilidadesSerializer,Profe_ResponsabilidadesSerializer,DisciplinaSerializer,CarreraSerializer,AnnoSerializer,Anno_CursadoSerializer,AsignaturaSerializer,Asignatura_PlanSerializer,GrupoSerializer,ProfesorAsignaturaSerializer,EstudiantePerfilSerializer

from .models import Semestre,Semestre_Cursado,Tipo_Curso,Plan_Estudio,EstudiantePerfil,Curso,ProfesorAsignatura,Grupo,Asignatura_Plan,Asignatura,Anno_Cursado,Disciplina,Profe_Responsabilidades,ProfesorPerfil, Anno, Responsabilidades, Categoria_Docente, Categoria_Cientifica, Titulo, Carrera, Users
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView , DestroyAPIView


class UsersListView(ListAPIView):
    serializer_class = UsersSerializer
    permission_classes = ()
    queryset = Users.objects.all()

class UsersCreateView(CreateAPIView):
    serializer_class = UsersSerializer
    permission_classes = ()

class UsersRetrieveView(RetrieveAPIView):
    serializer_class = UsersSerializer
    permission_classes = ()
    queryset = Users.objects.all()
    lookup_field = 'id'

class UsersUpdateView(UpdateAPIView):
    serializer_class = UsersSerializer
    permission_classes = ()
    queryset = Users.objects.all()
    lookup_field = 'id'

class UsersDestroyAPIView(DestroyAPIView):
    serializer_class = UsersSerializer
    permission_classes = ()
    queryset = Users.objects.all()
    lookup_field = 'id'


class TituloListView(ListAPIView):
    serializer_class = TituloSerializer
    permission_classes = ()
    queryset = Titulo.objects.all()

class TituloCreateView(CreateAPIView):
    serializer_class = TituloSerializer
    permission_classes = ()

class TituloRetrieveView(RetrieveAPIView):
    serializer_class = TituloSerializer
    permission_classes = ()
    queryset = Titulo.objects.all()
    lookup_field = 'id'

class TituloUpdateView(UpdateAPIView):
    serializer_class = TituloSerializer
    permission_classes = ()
    queryset = Titulo.objects.all()
    lookup_field = 'id'

class TituloDestroyView(DestroyAPIView):
    serializer_class = TituloSerializer
    permission_classes = ()
    queryset = Titulo.objects.all()
    lookup_field = 'id'

 
class Categoria_CientificaListView(ListAPIView):
    serializer_class = Categoria_CientificaSerializer
    permission_classes = ()
    queryset = Categoria_Cientifica.objects.all()

class Categoria_CientificaCreateView(CreateAPIView):
    serializer_class = Categoria_CientificaSerializer
    permission_classes = ()

class Categoria_CientificaRetrieveView(RetrieveAPIView):
    serializer_class = Categoria_CientificaSerializer
    permission_classes = ()
    queryset = Categoria_Cientifica.objects.all()
    lookup_field = 'id'

class Categoria_CientificaUpdateView(UpdateAPIView):
    serializer_class = Categoria_CientificaSerializer
    permission_classes = ()
    queryset = Categoria_Cientifica.objects.all()
    lookup_field = 'id'

class Categoria_CientificaDestroyView(DestroyAPIView):
    serializer_class = Categoria_CientificaSerializer
    permission_classes = ()
    queryset = Categoria_Cientifica.objects.all()
    lookup_field = 'id'



class Categoria_DocenteListView(ListAPIView):
    serializer_class = Categoria_DocenteSerializer
    permission_classes = ()
    queryset = Categoria_Docente.objects.all()

class Categoria_DocenteCreateView(CreateAPIView):
    serializer_class = Categoria_DocenteSerializer
    permission_classes = ()

class Categoria_DocenteRetrieveView(RetrieveAPIView):
    serializer_class = Categoria_DocenteSerializer
    permission_classes = ()
    queryset = Categoria_Docente.objects.all()
    lookup_field = 'id'

class Categoria_DocenteUpdateView(UpdateAPIView):
    serializer_class = Categoria_DocenteSerializer
    permission_classes = ()
    queryset = Categoria_Docente.objects.all()
    lookup_field = 'id'

class Categoria_DocenteDestroyView(DestroyAPIView):
    serializer_class = Categoria_DocenteSerializer
    permission_classes = ()
    queryset = Categoria_Docente.objects.all()
    lookup_field = 'id'

class SemestreListView(ListAPIView):
    serializer_class = SemestreSerializer
    permission_classes = ()
    queryset = Semestre.objects.all()

class SemestreCreateView(CreateAPIView):
    serializer_class = SemestreSerializer
    permission_classes = ()

class SemestreRetrieveView(RetrieveAPIView):
    serializer_class = SemestreSerializer
    permission_classes = ()
    queryset = Semestre.objects.all()
    lookup_field = 'id'

class SemestreUpdateView(UpdateAPIView):
    serializer_class = SemestreSerializer
    permission_classes = ()
    queryset = Semestre.objects.all()
    lookup_field = 'id'

class SemestreDestroyView(DestroyAPIView):
    serializer_class = SemestreSerializer
    permission_classes = ()
    queryset = Semestre.objects.all()
    lookup_field = 'id'

class CursoListView(ListAPIView):
    serializer_class = CursoSerializer
    permission_classes = ()
    queryset = Curso.objects.all()

class CursoCreateView(CreateAPIView):
    serializer_class = CursoSerializer
    permission_classes = ()

class CursoRetrieveView(RetrieveAPIView):
    serializer_class = CursoSerializer
    permission_classes = ()
    queryset = Curso.objects.all()
    lookup_field = 'id'

class CursoUpdateView(UpdateAPIView):
    serializer_class = CursoSerializer
    permission_classes = ()
    queryset = Curso.objects.all()
    lookup_field = 'id'

class CursoDestroyView(DestroyAPIView):
    serializer_class = CursoSerializer
    permission_classes = ()
    queryset = Curso.objects.all()
    lookup_field = 'id'

class Semestre_CursadoListView(ListAPIView):
    serializer_class =Semestre_CursadoSerializer
    permission_classes = ()
    queryset = Semestre_Cursado.objects.all()

class Semestre_CursadoCreateView(CreateAPIView):
    serializer_class = Semestre_CursadoSerializer
    permission_classes = ()

class Semestre_CursadoRetrieveView(RetrieveAPIView):
    serializer_class = Semestre_CursadoSerializer
    permission_classes = ()
    queryset = Semestre_Cursado.objects.all()
    lookup_field = 'id'

class Semestre_CursadoUpdateView(UpdateAPIView):
    serializer_class = Semestre_CursadoSerializer
    permission_classes = ()
    queryset = Semestre_Cursado.objects.all()
    lookup_field = 'id'
  
class Semestre_CursadoDestroyView(DestroyAPIView):
    serializer_class = Semestre_CursadoSerializer
    permission_classes = ()
    queryset = Semestre_Cursado.objects.all()
    lookup_field = 'id'

class Tipo_CursoListView(ListAPIView):
    serializer_class =Tipo_CursoSerializer
    permission_classes = ()
    queryset = Tipo_Curso.objects.all()

class Tipo_CursoCreateView(CreateAPIView):
    serializer_class = Tipo_CursoSerializer
    permission_classes = ()

class Tipo_CursoRetrieveView(RetrieveAPIView):
    serializer_class = Tipo_CursoSerializer
    permission_classes = ()
    queryset = Tipo_Curso.objects.all()
    lookup_field = 'id'

class Tipo_CursoUpdateView(UpdateAPIView):
    serializer_class = Tipo_CursoSerializer
    permission_classes = ()
    queryset = Tipo_Curso.objects.all()
    lookup_field = 'id'
  
class Tipo_CursoDestroyView(DestroyAPIView):
    serializer_class = Tipo_CursoSerializer
    permission_classes = ()
    queryset = Tipo_Curso.objects.all()
    lookup_field = 'id'  

class Plan_EstudioListView(ListAPIView):
    serializer_class = Plan_EstudioSerializer
    permission_classes = ()
    queryset = Plan_Estudio.objects.all()

class Plan_EstudioCreateView(CreateAPIView):
    serializer_class = Plan_EstudioSerializer
    permission_classes = ()

class Plan_EstudioRetrieveView(RetrieveAPIView):
    serializer_class = Plan_EstudioSerializer
    permission_classes = ()
    queryset = Plan_Estudio.objects.all()
    lookup_field = 'id'

class Plan_EstudioUpdateView(UpdateAPIView):
    serializer_class = Plan_EstudioSerializer
    permission_classes = ()
    queryset = Plan_Estudio.objects.all()
    lookup_field = 'id'

class Plan_EstudioDestroyView(DestroyAPIView):
    serializer_class = Plan_EstudioSerializer
    permission_classes = ()
    queryset = Plan_Estudio.objects.all()
    lookup_field = 'id'  

class ProfesorPerfilListView(ListAPIView):
    serializer_class = ProfesorPerfilSerializer
    permission_classes = ()
    queryset = ProfesorPerfil.objects.all()

class ProfesorPerfilCreateView(CreateAPIView):
    serializer_class = ProfesorPerfilSerializer
    permission_classes = ()

class ProfesorPerfilRetrieveView(RetrieveAPIView):
    serializer_class = ProfesorPerfilSerializer
    permission_classes = ()
    queryset = ProfesorPerfil.objects.all()
    lookup_field = 'id'

class ProfesorPerfilUpdateView(UpdateAPIView):
    serializer_class = ProfesorPerfilSerializer
    permission_classes = ()
    queryset = ProfesorPerfil.objects.all()
    lookup_field = 'id'
  
class ProfesorPerfilDestroyView(DestroyAPIView):
    serializer_class = ProfesorPerfilSerializer
    permission_classes = ()
    queryset = ProfesorPerfil.objects.all()
    lookup_field = 'id'

class ResponsabilidadesListView(ListAPIView):
    serializer_class = ResponsabilidadesSerializer
    permission_classes = ()
    queryset = Responsabilidades.objects.all()

class ResponsabilidadesCreateView(CreateAPIView):
    serializer_class = ResponsabilidadesSerializer
    permission_classes = ()

class ResponsabilidadesRetrieveView(RetrieveAPIView):
    serializer_class = ResponsabilidadesSerializer
    permission_classes = ()
    queryset = Responsabilidades.objects.all()
    lookup_field = 'id'

class ResponsabilidadesUpdateView(UpdateAPIView):
    serializer_class = ResponsabilidadesSerializer
    permission_classes = ()
    queryset = Responsabilidades.objects.all()
    lookup_field = 'id'

class ResponsabilidadesDestroyView(DestroyAPIView):
    serializer_class = ResponsabilidadesSerializer
    permission_classes = ()
    queryset = Responsabilidades.objects.all()
    lookup_field = 'id'  

class Profe_ResponsabilidadesListView(ListAPIView):
    serializer_class = Profe_ResponsabilidadesSerializer
    permission_classes = ()
    queryset =Profe_Responsabilidades.objects.all()

class Profe_ResponsabilidadesCreateView(CreateAPIView):
    serializer_class = Profe_ResponsabilidadesSerializer
    permission_classes = ()

class Profe_ResponsabilidadesRetrieveView(RetrieveAPIView):
    serializer_class = Profe_ResponsabilidadesSerializer
    permission_classes = ()
    queryset = Profe_Responsabilidades.objects.all()
    lookup_field = 'id'

class Profe_ResponsabilidadesUpdateView(UpdateAPIView):
    serializer_class = Profe_ResponsabilidadesSerializer
    permission_classes = ()
    queryset = Profe_Responsabilidades.objects.all()
    lookup_field = 'id'
  
class Profe_ResponsabilidadesDestroyView(DestroyAPIView):
    serializer_class = Profe_ResponsabilidadesSerializer
    permission_classes = ()
    queryset = Profe_Responsabilidades.objects.all()
    lookup_field = 'id'

class DisciplinaListView(ListAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = ()
    queryset =Disciplina.objects.all()

class DisciplinaCreateView(CreateAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = ()

class DisciplinaRetrieveView(RetrieveAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = ()
    queryset = Disciplina.objects.all()
    lookup_field = 'id'

class DisciplinaUpdateView(UpdateAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = ()
    queryset = Disciplina.objects.all()
    lookup_field = 'id'

class DisciplinaDestroyView(DestroyAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = ()
    queryset = Disciplina.objects.all()
    lookup_field = 'id'  
 
class CarreraListView(ListAPIView):
    serializer_class = CarreraSerializer
    permission_classes = ()
    queryset =Carrera.objects.all()

class CarreraCreateView(CreateAPIView):
    serializer_class = CarreraSerializer
    permission_classes = ()

class CarreraRetrieveView(RetrieveAPIView):
    serializer_class = CarreraSerializer
    permission_classes = ()
    queryset = Carrera.objects.all()
    lookup_field = 'id'

class CarreraUpdateView(UpdateAPIView):
    serializer_class = CarreraSerializer
    permission_classes = ()
    queryset = Carrera.objects.all()
    lookup_field = 'id'
  
class CarreraDestroyView(DestroyAPIView):
    serializer_class = CarreraSerializer
    permission_classes = ()
    queryset = Carrera.objects.all()
    lookup_field = 'id' 

class AnnoListView(ListAPIView):
    serializer_class = AnnoSerializer
    permission_classes = ()
    queryset =Anno.objects.all()

class AnnoCreateView(CreateAPIView):
    serializer_class = AnnoSerializer
    permission_classes = ()

class AnnoRetrieveView(RetrieveAPIView):
    serializer_class = AnnoSerializer
    permission_classes = ()
    queryset = Anno.objects.all()
    lookup_field = 'id'

class AnnoUpdateView(UpdateAPIView):
    serializer_class = AnnoSerializer
    permission_classes = ()
    queryset = Anno.objects.all()
    lookup_field = 'id'
  
class AnnoDestroyView(DestroyAPIView):
    serializer_class = AnnoSerializer
    permission_classes = ()
    queryset = Anno.objects.all()
    lookup_field = 'id '

class Anno_CursadoListView(ListAPIView):
    serializer_class = Anno_CursadoSerializer
    permission_classes = ()
    queryset =Anno_Cursado.objects.all()

class Anno_CursadoCreateView(CreateAPIView):
    serializer_class = Anno_CursadoSerializer
    permission_classes = ()

class Anno_CursadoRetrieveView(RetrieveAPIView):
    serializer_class = Anno_CursadoSerializer
    permission_classes = ()
    queryset = Anno_Cursado.objects.all()
    lookup_field = 'id'

class Anno_CursadoUpdateView(UpdateAPIView):
    serializer_class = Anno_CursadoSerializer
    permission_classes = ()
    queryset = Anno_Cursado.objects.all()
    lookup_field = 'id'
  
class Anno_CursadoDestroyView(DestroyAPIView):
    serializer_class = Anno_CursadoSerializer
    permission_classes = ()
    queryset = Anno_Cursado.objects.all()
    lookup_field = 'id'  

class AsignaturaListView(ListAPIView):
    serializer_class =AsignaturaSerializer
    permission_classes = ()
    queryset =Asignatura.objects.all()

class AsignaturaCreateView(CreateAPIView):
    serializer_class = AsignaturaSerializer
    permission_classes = ()

class AsignaturaRetrieveView(RetrieveAPIView):
    serializer_class = AsignaturaSerializer
    permission_classes = ()
    queryset = Asignatura.objects.all()
    lookup_field = 'id'

class AsignaturaUpdateView(UpdateAPIView):
    serializer_class = AsignaturaSerializer
    permission_classes = ()
    queryset = Asignatura.objects.all()
    lookup_field = 'id'
  
class AsignaturaDestroyView(DestroyAPIView):
    serializer_class = AsignaturaSerializer
    permission_classes = ()
    queryset = Asignatura.objects.all()
    lookup_field = 'id'  

class Asignatura_PlanListView(ListAPIView):
    serializer_class =Asignatura_PlanSerializer
    permission_classes = ()
    queryset =Asignatura_Plan.objects.all()

class Asignatura_PlanCreateView(CreateAPIView):
    serializer_class = Asignatura_PlanSerializer
    permission_classes = ()

class Asignatura_PlanRetrieveView(RetrieveAPIView):
    serializer_class = Asignatura_PlanSerializer
    permission_classes = ()
    queryset = Asignatura_Plan.objects.all()
    lookup_field = 'id'

class Asignatura_PlanUpdateView(UpdateAPIView):
    serializer_class = Asignatura_PlanSerializer
    permission_classes = ()
    queryset = Asignatura_Plan.objects.all()
    lookup_field = 'id'
  
class Asignatura_PlanDestroyView(DestroyAPIView):
    serializer_class = Asignatura_PlanSerializer
    permission_classes = ()
    queryset = Asignatura_Plan.objects.all()
    lookup_field = 'id'
  

class GrupoListView(ListAPIView):
    serializer_class =GrupoSerializer
    permission_classes = ()
    queryset =Grupo.objects.all()

class GrupoCreateView(CreateAPIView):
    serializer_class = GrupoSerializer
    permission_classes = ()

class GrupoRetrieveView(RetrieveAPIView):
    serializer_class = GrupoSerializer
    permission_classes = ()
    queryset = Grupo.objects.all()
    lookup_field = 'id'

class GrupoUpdateView(UpdateAPIView):
    serializer_class = GrupoSerializer
    permission_classes = ()
    queryset = Grupo.objects.all()
    lookup_field = 'id'

class GrupoDestroyView(DestroyAPIView):
    serializer_class = GrupoSerializer
    permission_classes = ()
    queryset = Grupo.objects.all()
    lookup_field = 'id' 

class ProfesorAsignaturaListView(ListAPIView):
    serializer_class =ProfesorAsignaturaSerializer
    permission_classes = ()
    queryset =ProfesorAsignatura.objects.all()

class ProfesorAsignaturaCreateView(CreateAPIView):
    serializer_class = ProfesorAsignaturaSerializer
    permission_classes = ()

class ProfesorAsignaturaRetrieveView(RetrieveAPIView):
    serializer_class = ProfesorAsignaturaSerializer
    permission_classes = ()
    queryset = ProfesorAsignatura.objects.all()
    lookup_field = 'id'

class ProfesorAsignaturaUpdateView(UpdateAPIView):
    serializer_class = ProfesorAsignaturaSerializer
    permission_classes = ()
    queryset = ProfesorAsignatura.objects.all()
    lookup_field = 'id'
  
class ProfesorAsignaturaDestroyView(DestroyAPIView):
    serializer_class = ProfesorAsignaturaSerializer
    permission_classes = ()
    queryset = ProfesorAsignatura.objects.all()
    lookup_field = 'id'  

class EstudiantePerfilListView(ListAPIView):
    serializer_class =EstudiantePerfilSerializer
    permission_classes = ()
    queryset =EstudiantePerfil.objects.all()

class EstudiantePerfilCreateView(CreateAPIView):
    serializer_class = EstudiantePerfilSerializer
    permission_classes = ()

class EstudiantePerfilRetrieveView(RetrieveAPIView):
    serializer_class = EstudiantePerfilSerializer
    permission_classes = ()
    queryset = EstudiantePerfil.objects.all()
    lookup_field = 'id'

class EstudiantePerfilUpdateView(UpdateAPIView):
    serializer_class = EstudiantePerfilSerializer
    permission_classes = ()
    queryset = EstudiantePerfil.objects.all()
    lookup_field = 'id'
  
class EstudiantePerfilDestroyView(DestroyAPIView):
    serializer_class = EstudiantePerfilSerializer
    permission_classes = ()
    queryset = EstudiantePerfil.objects.all()
    lookup_field = 'id'
  
