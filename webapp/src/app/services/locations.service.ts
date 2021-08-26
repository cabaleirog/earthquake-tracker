import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpParams } from '@angular/common/http';


export interface Location {
  identifier: string;
  name: string;
  latitude: number;
  longitude: number;
}

export interface LocationResponse {
  message: string;
  data: Location[];
}


@Injectable({
  providedIn: 'root'
})
export class LocationsService {

  constructor(private http: HttpClient) { }

  geLocations(): Observable<LocationResponse> {
    return this.http.get<LocationResponse>(`/locations`);
  }

}
