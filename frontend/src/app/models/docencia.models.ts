export class Users{
  id: any;
  nombre!: string;
  apellido!: string;
  email!: string;
  date_joined!: Date;
  active!: boolean;
  admin!: boolean;
  staff!: boolean;
  is_profesor!: boolean;
  is_estudiante!: boolean;
}

export class Titulo{
  id: any;
  nombre!: string;
}

export class Categoria_Cientifica{
  id: any;
  nombre!: string;
}

export class Categoria_Docente{
  id: any;
  nombre!: string;
}

export class Curso{
  id: any;
  curso!: string;
}

export class Semestre{
  semestres = [
    'Primero',
    'Segundo',
  ]

  id: any;
  semestre!: string;
}
export class Semestre_Cursado{
  id: any;
  semestre!: Semestre;
  curso!: Curso;
  
}

export class Tipo_Curso{
  id: any;
  nombre!: string;
}

export class Plan_Estudio{
  id: any;
  nombre!: string;
  curso_emp!: Curso;
}

export class ProfesorPerfil{
  id: any;
  user!: Users;
  telefono!: string
  movil!: string
  categoria_doc!: Categoria_Docente;
  categorias_cientficas!: Categoria_Cientifica;
  titulo!: Titulo;
}

export class Responsabilidades{
  id: any;
  nombre!: string;
  peso!: number;
}
export class Profe_Responsabilidades{
  id: any;
  responsabilidad!: Responsabilidades;
  profesor!: Users;
  
}
export class Disciplina{
  id: any;
  nombre!: string;
  jefe_disciplina!: Profe_Responsabilidades;
}
export class Carrera{
  id: any;
  carrera!: string
  jefe_departamento!: Profe_Responsabilidades;
  segundo_jefe!: Profe_Responsabilidades;
  coordinador!: Profe_Responsabilidades;
}
export class Anno{
  id: any;
  anno!: string;
}
export class Anno_Cursado{
  id: any;
  anno!: Anno;
  carrera !: Carrera;
  curso!: Curso;
  tipo_curso!: Tipo_Curso;
  plan!: Plan_Estudio;
  principal_anno!: Profe_Responsabilidades;
}
export class Asignatura{
  id: any;
  nombre !: string;
}
export class Asignatura_Plan{
  id: any;
  asignatura!: Asignatura;
  disciplina !: Disciplina;
  plan!: Plan_Estudio;
  tipo_curso!: Tipo_Curso;
  semestre!:Semestre;
  anno!: Anno;
  cantidad_horas_plan!: number;
}
export class Grupo{
  id: any;
  grupo!: string
  anno!: Anno;
  profesor_guia!: Profe_Responsabilidades;
}
export class ProfesorAsignatura{
  id: any;
  profesor!:ProfesorPerfil;
  asignatura !: Asignatura_Plan;
  curso!: Semestre_Cursado;
  created_by!: Users;
  horas_conferencias!: number;
  cant_grupos_conferencias!: number;
  horas_cp!: number;
  cant_grupos_cp !: number;
  horas_cpc!: number;
  cant_grupos_cpc!: number;
  horas_lab !: number;
  cant_grupos_lab!: number;
  horas_taller!: number;
  cant_grupos_taller!: number;
  horas_seminarios!: number;
  cant_grupos_seminario!: number;
}

export class EstudiantePerfil{
  id: any;
  user!: Users;
  carrera!: Carrera;
}