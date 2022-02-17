import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';



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

  createTitulo(titulo: { nombre: any; }): Observable<any> {
    let body = {
      nombre:titulo.nombre,

    }
    let a = this.http.post(this.url + "users/create/", body, {
      headers: this.headersC,
    });
    console.log(a);
    return a;
  }

  update(titulo): Observable<any> {
    let body = {
      nombre: users.nombre,
    }
    let a = this.http.put(this.url + 'users/update/', body, {
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
