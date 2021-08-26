import { Input } from '@angular/core';
import { Component, OnInit } from '@angular/core';
import { EarthquakesService } from 'src/app/services/earthquakes.service';

interface EarthquakeData {
  event_id: string;
  latitude: number;
  longitude: number;
  magnitude: number;
  magnitude_type: string;
  place: string;
  time: string;  // UTC ISO Formatted date and time.
  title: string;
}

@Component({
  selector: 'app-closest-earthquake',
  templateUrl: './closest-earthquake.component.html',
  styleUrls: ['./closest-earthquake.component.scss']
})
export class ClosestEarthquakeComponent implements OnInit {
  @Input('city-identifier') cityIdentifier: string = '';
  @Input('city') city: string = '';
  @Input('since') sinceDate!: string;
  @Input('until') untilDate!: string;

  public data?: EarthquakeData;

  public magnitude: number = 0;

  public loading: boolean = true;

  constructor(private earthquakeService: EarthquakesService) { }

  ngOnInit(): void {
    this.loading = true;
    this.earthquakeService.getClosest(this.cityIdentifier, this.sinceDate, this.untilDate)
      .subscribe(
        (resp) => {
          console.log(resp);
          if (resp && resp['data']) {
            this.data = resp['data'];
          }
          this.loading = false;
        },
        (err) => {
          console.error(err);
          this.loading = false;
        }
      )
  }

  get foundOne(): boolean {
    return (this.data !== undefined && this.data !== null);
  }

  get asOf(): Date | null {
    if (this.data === null || this.data === undefined) {
      return null;
    }
    return new Date(this.data.time)
  }
}
