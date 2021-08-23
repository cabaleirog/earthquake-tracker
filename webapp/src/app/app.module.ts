import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ClosestEarthquakeComponent } from './components/closest-earthquake/closest-earthquake.component';
import { EarthquakeTrackerComponent } from './pages/earthquake-tracker/earthquake-tracker.component';

@NgModule({
  declarations: [
    AppComponent,
    ClosestEarthquakeComponent,
    EarthquakeTrackerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
