import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpParams } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class EarthquakesService {

  constructor(private http: HttpClient) { }

  getClosest(city: string, since: string, until: string): Observable<any> {
    const params = new HttpParams()
      .set('location', city)
      .set('starttime', since)
      .set('endtime', until);
    return this.http.get(`/earthquakes`, { params: params });
  }

}
