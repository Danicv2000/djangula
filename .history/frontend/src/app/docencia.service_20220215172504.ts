import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Users ,Titulo,Categoria_Cientifica, Categoria_Docente,Curso,Semestre,Semestre_Cursado,
         Tipo_Curso,Plan_Estudio,ProfesorPerfil,Responsabilidades,  Disciplina, Carrera,Anno,Anno_Cursado, Asignatura,Asignatura_Plan,
         Grupo,ProfesorAsignatura,EstudiantePerfil} from './models/docencia.models';


@Injectable({
  providedIn: 'root'
})
export class DocenciaService {
  public url: string;
  public headers: any;
  public headersC = new HttpHeaders().set("Content-Type", "application/json");



  constructor(
    public http: HttpClient,
  ) {
    this.url = 'http://localhost:8000/administrar/';


  }

  createUsers(users: { nombre: any; apellido: any;
              email: any;date_joined: any;
              active: any;admin: any;staff: any;
              is_profesor: any;is_estudiante: any;}): Observable<any> {
    let body = {
      nombre:users.nombre,
      apellido:users.apellido,
      email:users.email,
      date_joined:users.date_joined,

      is_profesor:users.is_profesor,
      is_estudiante:users.is_estudiante,


    }
    let a = this.http.post(this.url + "users/create/", body, {
      headers: this.headersC,
    });
    console.log(a);
    return a;
  }

  update(id:number, users: { nombre: any; apellido: any;
      email: any;date_joined: any;
      active: any;admin: any;staff: any;
      is_profesor: any;is_estudiante: any; }): Observable<any> {
    let body = {
      nombre: users.nombre,
      apellido:users.apellido,
      email:users.email,
      date_joined:users.date_joined,
     is_profesor:users.is_profesor,
      is_estudiante:users.is_estudiante,
    }
    let a = this.http.put(this.url + 'users/' + id.toString() + '/update/', body, {
      headers: this.headersC,
    });
    return a;
  }

  delete(id: any): Observable<any> {
    return this.http.delete(this.url + 'users/' + id + 'delete/',{
      headers: this.headersC,
    });

  }

  findByUsers(id:number): Observable<any> {
    let a = this.http.get(this.url + 'users/' + id, {headers:this.headersC});
    return a;
  }
  listUsers(): Observable<any> {
    let a = this.http.get(this.url + 'users/', {
      headers: this.headersC,
    });
    return a;
  }

}
