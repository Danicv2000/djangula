from django.urls import path

from .views import (UsersListView, UsersCreateView, UsersRetrieveView, UsersUpdateView, UsersDestroyAPIView,
                   TituloListView,TituloCreateView, TituloRetrieveView, TituloUpdateView,TituloDestroyView,
                   Categoria_CientificaListView, Categoria_CientificaCreateView, Categoria_CientificaRetrieveView, Categoria_CientificaUpdateView,Categoria_CientificaDestroyView,
                   Categoria_DocenteListView, Categoria_DocenteCreateView, Categoria_DocenteRetrieveView, Categoria_DocenteUpdateView, Categoria_DocenteDestroyView,
                   SemestreListView,SemestreCreateView, SemestreRetrieveView, SemestreUpdateView,SemestreDestroyView,
                   CursoListView, CursoCreateView, CursoRetrieveView, CursoUpdateView, CursoDestroyView,
                   Semestre_CursadoListView,Semestre_CursadoCreateView, Semestre_CursadoRetrieveView, Semestre_CursadoUpdateView,Semestre_CursadoDestroyView,
                   Tipo_CursoListView, Tipo_CursoCreateView, Tipo_CursoRetrieveView, Tipo_CursoUpdateView, Tipo_CursoDestroyView,
                   Plan_EstudioListView,Plan_EstudioCreateView, Plan_EstudioRetrieveView, Plan_EstudioUpdateView,Plan_EstudioDestroyView,
                   ProfesorPerfilListView, ProfesorPerfilCreateView, ProfesorPerfilRetrieveView, ProfesorPerfilUpdateView, ProfesorPerfilDestroyView,
                   ResponsabilidadesListView,ResponsabilidadesCreateView, ResponsabilidadesRetrieveView, ResponsabilidadesUpdateView,ResponsabilidadesDestroyView,
                   Profe_ResponsabilidadesListView, Profe_ResponsabilidadesCreateView, Profe_ResponsabilidadesRetrieveView, Profe_ResponsabilidadesUpdateView, Profe_ResponsabilidadesDestroyView,
                   DisciplinaListView,DisciplinaCreateView, DisciplinaRetrieveView, DisciplinaUpdateView,DisciplinaDestroyView,
                   CarreraListView, CarreraCreateView, CarreraRetrieveView,CarreraUpdateView, CarreraDestroyView,
                   AnnoListView,AnnoCreateView, AnnoRetrieveView, AnnoUpdateView,AnnoDestroyView,
                   Anno_CursadoListView, Anno_CursadoCreateView,Anno_CursadoRetrieveView, Anno_CursadoUpdateView, Anno_CursadoDestroyView,
                   AsignaturaListView,  AsignaturaCreateView,  AsignaturaRetrieveView,  AsignaturaUpdateView, AsignaturaDestroyView,
                   Asignatura_PlanListView,Asignatura_PlanCreateView, Asignatura_PlanRetrieveView, Asignatura_PlanUpdateView,Asignatura_PlanDestroyView,
                   GrupoListView, GrupoCreateView, GrupoRetrieveView,GrupoUpdateView, GrupoDestroyView,
                   ProfesorAsignaturaListView,ProfesorAsignaturaCreateView, ProfesorAsignaturaRetrieveView, ProfesorAsignaturaUpdateView,ProfesorAsignaturaDestroyView,
                   EstudiantePerfilListView,EstudiantePerfilCreateView, EstudiantePerfilRetrieveView, EstudiantePerfilUpdateView,EstudiantePerfilDestroyView)





urlpatterns = [
   path('users/',  UsersListView, name='user'),
   path('users/create/',UsersCreateView.as_view(), name='user_a'),
   path('users/<int:id>',UsersRetrieveView.as_view(), name='user_b'),
   path('users/<int:id>/update/',UsersUpdateView.as_view(),name='user_c'),
   path('users/<int:id>/delete/', UsersDestroyAPIView.as_view(),name='user_d'),

 # Titulos
   path('titulos/', TituloListView.as_view(),name='titulo'),
   path('titulos/create',TituloCreateView.as_view(), name='titulo_a'),
   path('titulos/<int:id>',TituloRetrieveView.as_view(), name='titulo_b'),
   path('titulos/<int:id>/update/',TituloUpdateView.as_view(),name='titulo_c'),
   path('titulos/<int:id>/delete/',TituloDestroyView.as_view(),name='titulo_d'),
                                        
                                        # Categorias Cientificas
   path('categoria_cientificas/', Categoria_CientificaListView.as_view(),name='categoria_cientifica'),
   path('categoria_cientificas/create', Categoria_CientificaCreateView.as_view(), name='categoria_cientifica_a'),
   path('categoria_cientificas/<int:id>',Categoria_CientificaRetrieveView.as_view(), name='categoria_cientifica_b'),
   path('categoria_cientificas/<int:id>/update/', Categoria_CientificaUpdateView.as_view(), name='categoria_cientifica_c'),
   path('categoria_cientificas/<int:id>/delete/', Categoria_CientificaDestroyView.as_view(), name='categoria_cientifica_d'),
           # Categorias docente
   path('categoria_docente/', Categoria_DocenteListView.as_view(),name='categoria_docente'),
   path('categoria_docentes/create', Categoria_DocenteCreateView.as_view(), name='categoria_docente_a'),
   path('categoria_docentes/<int:id>',Categoria_DocenteRetrieveView.as_view(), name='categoria_cientifica_b'),
   path('categoria_docentes/<int:id>/update/', Categoria_DocenteUpdateView.as_view(), name='categoria_docente_c'),   
   path('categoria_docentes/<int:id>/delete/', Categoria_DocenteDestroyView.as_view(), name='categoria_docente_d'),                                                       
                                      # Semestre  
   path('semestres/', SemestreListView.as_view(),name='semestre'),
   path('semestres/create', SemestreCreateView.as_view(), name='semestre_a'),
   path('semestres/<int:id>',SemestreRetrieveView.as_view(), name='semestre_b'),
   path('semestres/<int:id>/update/', SemestreUpdateView.as_view(), name='semestre_c'),    
   path('semestres/<int:id>/delete/',SemestreDestroyView.as_view(), name='semestre_d'),                                                                                                                                                                        
                                        # Cursos
   path('cursos/', CursoListView.as_view(),name='curso'),
   path('cursos/create', CursoCreateView.as_view(), name='curso_a'),
   path('cursos/<int:id>',CursoRetrieveView.as_view(), name='curso_b'),
   path('cursos/<int:id>/update/', CursoUpdateView.as_view(), name='curso_c'),      
   path('cursos/<int:id>/delete/', CursoDestroyView.as_view(), name='curso_d'),                                                                                                                          
                                        # Semestre_Cursado
   path('semestre_cursados/', Semestre_CursadoListView.as_view(),name='semestre_cursado'),
   path('semestre_cursados/create', Semestre_CursadoCreateView.as_view(), name='semestre_cursado_a'),
   path('semestre_cursados/<int:id>',Semestre_CursadoRetrieveView.as_view(), name='semestre_cursado_b'),
   path('semestre_cursados/<int:id>/update/', Semestre_CursadoUpdateView.as_view(), name='semestre_cursado_c'),                                                    
   path('semestre_cursados/<int:id>/delete/', Semestre_CursadoDestroyView.as_view(), name='semestre_cursado_d'),                                                                                                                    
                                        # Tipo_Curso
   path('tipo_cursos/', Tipo_CursoListView.as_view(),name='tipo_curso'),
   path('tipo_cursos/create', Tipo_CursoCreateView.as_view(), name='tipo_curso_a'),
   path('tipo_cursos/<int:id>',Tipo_CursoRetrieveView.as_view(), name='tipo_curso_b'),
   path('tipo_cursos/<int:id>/update/', Tipo_CursoUpdateView.as_view(), name='tipo_curso_c'),   
   path('tipo_cursos/<int:id>/delete/', Tipo_CursoDestroyView.as_view(), name='tipo_curso_d'),       
                                                                                  
                                        # Planes de Estudios
   path('plan_estudios/',  Plan_EstudioListView.as_view(),name='plan_estudio'),
   path('plan_estudios/create',  Plan_EstudioCreateView.as_view(), name='plan_estudio_a'),
   path('plan_estudios/<int:id>', Plan_EstudioRetrieveView.as_view(), name='plan_estudio_b'),
   path('plan_estudios/<int:id>/update/', Plan_EstudioUpdateView.as_view(), name='plan_estudio_c'),                                                                                                                                                     
   path('plan_estudios/<int:id>/delete/', Plan_EstudioDestroyView.as_view(), name='plan_estudio_d'),  
                                   # Profesor perfil
   path('profesorperfiles/', ProfesorPerfilListView.as_view(),name='profesorperfil'),
   path('profesorperfiles/create',  ProfesorPerfilCreateView.as_view(), name='profesorperfil_a'),
   path('profesorperfiles/<int:id>', ProfesorPerfilRetrieveView.as_view(), name='profesorperfil_b'),
   path('profesorperfiles/<int:id>/update/', ProfesorPerfilUpdateView.as_view(), name='profesorperfil_c'),                                                                                                                                                                                    
   path('profesorperfiles/<int:id>/delete/', ProfesorPerfilDestroyView.as_view(), name='profesorperfil_d'),                                                                                                                                                                                                                                      
                                         # Responsabilidades

   path('responsabilidades/', ResponsabilidadesListView.as_view(),name='responsabilidad'),
   path('responsabilidades/create',  ResponsabilidadesCreateView.as_view(), name='responsabilidad_a'),
   path('responsabilidades/<int:id>', ResponsabilidadesRetrieveView.as_view(), name='responsabilidad_b'),
   path('responsabilidades/<int:id>/update/', ResponsabilidadesUpdateView.as_view(), name='responsabilidad_c'),                                                                                                                                                                                                                   
   path('responsabilidades/<int:id>/delete/', ResponsabilidadesDestroyView.as_view(), name='responsabilidad_d'),                                                                                                                                                                                                                                                                               
                                       # profe Responsabilidades

   path('profe_responsabilidades/', Profe_ResponsabilidadesListView.as_view(),name='profe_responsabilidad'),
   path('profe_responsabilidades/create',  Profe_ResponsabilidadesCreateView.as_view(), name='profe_responsabilidad_a'),
   path('profe_responsabilidades/<int:id>', Profe_ResponsabilidadesRetrieveView.as_view(), name='profe_responsabilidad_b'),
   path('profe_responsabilidades/<int:id>/update/', Profe_ResponsabilidadesUpdateView.as_view(), name='profe_responsabilidad_c'),                                                                                                                                                                                                                         
   path('profe_responsabilidades/<int:id>/delete/', Profe_ResponsabilidadesDestroyView.as_view(), name='profe_responsabilidad_d'),                                                                                                                                                                                                                                                                         
                                      
                                      
                                      
                                        # Disciplinas
   path('disciplinas/', DisciplinaListView.as_view(),name='disciplina'),
   path('disciplinas/create', DisciplinaCreateView.as_view(), name='disciplina_a'),
   path('disciplinas/<int:id>',DisciplinaRetrieveView.as_view(), name='disciplina_b'),
   path('disciplinas/<int:id>/update/', DisciplinaUpdateView.as_view(), name='disciplina_c'),                                                                 
   path('disciplinas/<int:id>/delete/', DisciplinaDestroyView.as_view(), name='disciplina_d'),                                                                                                                     
                                           
                                        # Carreras
   path('carreras/', CarreraListView.as_view(),name='carrera'),
   path('carreras/create',CarreraCreateView.as_view(), name='carrera_a'),
   path('carreras/<int:id>',CarreraRetrieveView.as_view(), name='carrera_b'),
   path('carreras/<int:id>/update/',CarreraUpdateView.as_view(), name='carrera_c'),                                                                                
   path('carreras/<int:id>/delete/',CarreraDestroyView.as_view(), name='carrera_d'),                                                                                                                                      
                                        # Annos
                                       
   path('annos/', AnnoListView.as_view(),name='anno'),
   path('annos/create',AnnoCreateView.as_view(), name='anno_a'),
   path('annos/<int:id>',AnnoRetrieveView.as_view(), name='anno_b'),
   path('annos/<int:id>/update/',AnnoUpdateView.as_view(), name='anno_c'),                                                                                                               
   path('annos/<int:id>/delete/',AnnoDestroyView.as_view(), name='anno_d'),                                                                                                                                                                               
                                      
                               # Annos cursado
                                       
   path('annos_cursado/', Anno_CursadoListView.as_view(),name='anno_cursado'),
   path('annos_cursado/create',Anno_CursadoCreateView.as_view(), name='anno_cursado_a'),
   path('annos_cursado/<int:id>',Anno_CursadoRetrieveView.as_view(), name='anno_cursado_b'),
   path('annos_cursado/<int:id>/update/',Anno_CursadoUpdateView.as_view(), name='anno_cursado_c'),                                                                                                                                    
   path('annos_cursado/<int:id>/delete/', Anno_CursadoDestroyView.as_view(), name='anno_cursado_d'),                                                                                                                                                                          
                                      
                                        # Asignaturas
   path('asignaturas/', AsignaturaListView.as_view(),name='asignatura'),
   path('asignaturas/create',AsignaturaCreateView.as_view(), name='asignatura_a'),
   path('asignaturas/<int:id>',AsignaturaRetrieveView.as_view(), name='asignatura_b'),
   path('asignaturas/<int:id>/update/',AsignaturaUpdateView.as_view(), name='asignatura_c'),                                                                                                                          
   path('asignaturas/<int:id>/delete/',AsignaturaDestroyView.as_view(), name='asignatura_d'),                                                                                                                                                                                          
                                        # Asignatura_Plan
   path('asignaturas_plan/', Asignatura_PlanListView.as_view(),name='asignatura_plan'),
   path('asignaturas_plan/create',Asignatura_PlanCreateView.as_view(), name='asignatura_plan_a'),
   path('asignaturas_plan/<int:id>',Asignatura_PlanRetrieveView.as_view(), name='asignatura_plan_b'),
   path('asignaturas_plan/<int:id>/update/',Asignatura_PlanUpdateView.as_view(), name='asignatura_plan_c'),                                                                                                                                                
   path('asignaturas_plan/<int:id>/delete/',Asignatura_PlanDestroyView.as_view(), name='asignatura_plan_d'),                                                                                                                                                                                                  
                                        # Grupos
                         
   path('grupos/', GrupoListView.as_view(),name='grupo'),
   path('grupos/create',GrupoCreateView.as_view(), name='grupo_a'),
   path('grupos/<int:id>',GrupoRetrieveView.as_view(), name='grupo_b'),
   path('grupos/<int:id>/update/',GrupoUpdateView.as_view(), name='grupo_c'),                                                                                                                                                              
   path('grupos/<int:id>/delete/',GrupoDestroyView.as_view(), name='grupo_d'),                                                                                                                                                                                                            
                                      
                                      
                      # Profesor Asignatura
                                       
   path('profesorasignaturas/', ProfesorAsignaturaListView.as_view(),name='profesorasignatura'),
   path('profesorasignaturas/create',ProfesorAsignaturaCreateView.as_view(), name='profesorasignatura_a'),
   path('profesorasignaturas/<int:id>',ProfesorAsignaturaRetrieveView.as_view(), name='profesorasignatura_b'),
   path('profesorasignaturas/<int:id>/update/',ProfesorAsignaturaUpdateView.as_view(), name='profesorasignatura_c'),                                                                                                                                                 
   path('profesorasignaturas/<int:id>/delete/',ProfesorAsignaturaDestroyView.as_view(), name='profesorasignatura_d'),                                                                                                                                                                                                       
                                     
                                   
                                   # Estudiante Perfil
                                       
   path('estudianteperfiles/', EstudiantePerfilListView.as_view(),name='estudianteperfil'),
   path('estudianteperfiles/create',EstudiantePerfilCreateView.as_view(), name='estudianteperfil_a'),
   path('estudianteperfiles/<int:id>',EstudiantePerfilRetrieveView.as_view(), name='estudianteperfil_b'),
   path('estudianteperfiles/<int:id>/update/',EstudiantePerfilUpdateView.as_view(), name='estudianteperfil_c'),                                                                                                                                                             
   path('estudianteperfiles/<int:id>/delete/',EstudiantePerfilDestroyView.as_view(), name='estudianteperfil_d'),   

                                 
]












