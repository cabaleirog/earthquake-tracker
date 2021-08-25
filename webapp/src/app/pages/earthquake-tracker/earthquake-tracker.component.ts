import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-earthquake-tracker',
  templateUrl: './earthquake-tracker.component.html',
  styleUrls: ['./earthquake-tracker.component.scss']
})
export class EarthquakeTrackerComponent implements OnInit {

  form = new FormGroup({
    since: new FormControl(''),
    until: new FormControl(''),
  })

  loading = false;

  public searchSince: string;
  public searchUntil: string;

  startDate: Date = new Date();
  endDate: Date = new Date();

  constructor() {
    const todayISO = (new Date()).toISOString().substr(0, 10);
    this.searchSince = todayISO;
    this.searchUntil = todayISO;
  }

  ngOnInit(): void {
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
}
