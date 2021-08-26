import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { LocationsService, Location } from 'src/app/services/locations.service';

@Component({
  selector: 'app-earthquake-tracker',
  templateUrl: './earthquake-tracker.component.html',
  styleUrls: ['./earthquake-tracker.component.scss']
})
export class EarthquakeTrackerComponent implements OnInit {

  loading = false;

  public searchSince: string;
  public searchUntil: string;

  startDate: Date = this.dateWithDelta(new Date(), -7);
  endDate: Date = new Date();

  form = new FormGroup({
    since: new FormControl(this.startDate.toISOString().substr(0, 10)),
    until: new FormControl(this.endDate.toISOString().substr(0, 10)),
  })

  locations: Location[] = [];

  constructor(private locationsService: LocationsService) {
    this.searchSince = this.startDate.toISOString().substr(0, 10);
    this.searchUntil = this.endDate.toISOString().substr(0, 10);
  }

  ngOnInit(): void {
    this.locationsService.geLocations()
      .subscribe((resp) => {
        this.locations = resp.data;
      });
  }

  updateData(): void {
    this.loading = true;
    console.log(this.form.get('since')?.value);
    console.log(this.form.get('until')?.value);
    this.startDate = new Date(this.form.get('since')!.value);
    this.endDate = new Date(this.form.get('until')!.value);
    this.searchSince = (this.startDate).toISOString().substr(0, 10)
    this.searchUntil = (this.endDate).toISOString().substr(0, 10)
    setTimeout(() => {
      this.loading = false;
    }, 100);
  }

  private dateWithDelta(date: Date, delta: number) {
    const other = new Date(date);
    other.setDate(other.getDate() + delta);
    return other;
  }
}
