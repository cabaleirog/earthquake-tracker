import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

export interface EarthquakeResponse {
  found: boolean;
  text?: string;
  magnitude?: number;
  scale?: string;
  location?: string;
  date?: Date;
}

const dummyResponse: EarthquakeResponse = {
  found: false,
  text: 'M 5.7 - South of Africa on June 30',
  magnitude: 5.7,
  scale: 'M',
  location: 'South of Africa',
  date: new Date(2021, 8, 20),
}

@Injectable({
  providedIn: 'root'
})
export class EarthquakesService {

  constructor() { }

  getClosest(city: string, since: Date, until: Date): Observable<EarthquakeResponse> {
    return of(dummyResponse);
  }

}
