import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EarthquakeTrackerComponent } from './earthquake-tracker.component';

describe('EarthquakeTrackerComponent', () => {
  let component: EarthquakeTrackerComponent;
  let fixture: ComponentFixture<EarthquakeTrackerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EarthquakeTrackerComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EarthquakeTrackerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
