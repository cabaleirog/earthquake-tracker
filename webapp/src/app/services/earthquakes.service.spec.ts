import { TestBed } from '@angular/core/testing';

import { EarthquakesService } from './earthquakes.service';

describe('EarthquakesService', () => {
  let service: EarthquakesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EarthquakesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
