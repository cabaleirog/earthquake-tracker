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

  constructor() { }

  ngOnInit(): void {
  }

  updateData(): void {
    console.log(this.form.get('since')?.value);
    console.log(this.form.get('until')?.value);
  }
}
