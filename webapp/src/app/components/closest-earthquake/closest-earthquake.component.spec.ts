import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClosestEarthquakeComponent } from './closest-earthquake.component';

describe('ClosestEarthquakeComponent', () => {
  let component: ClosestEarthquakeComponent;
  let fixture: ComponentFixture<ClosestEarthquakeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ClosestEarthquakeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ClosestEarthquakeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
