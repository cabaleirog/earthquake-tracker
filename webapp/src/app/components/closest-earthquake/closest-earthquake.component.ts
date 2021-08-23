import { Input } from '@angular/core';
import { Component, OnInit } from '@angular/core';
import { EarthquakeResponse, EarthquakesService } from 'src/app/services/earthquakes.service';

@Component({
  selector: 'app-closest-earthquake',
  templateUrl: './closest-earthquake.component.html',
  styleUrls: ['./closest-earthquake.component.scss']
})
export class ClosestEarthquakeComponent implements OnInit {
  @Input('city') city: string = '';
  @Input('since') sinceDate!: Date;
  @Input('until') untilDate!: Date;

  public data!: EarthquakeResponse;

  constructor(private earthquakeService: EarthquakesService) { }

  ngOnInit(): void {
    this.earthquakeService.getClosest(this.city, this.sinceDate, this.untilDate)
      .subscribe((resp: EarthquakeResponse) => {
        this.data = resp;
      })
  }

}
