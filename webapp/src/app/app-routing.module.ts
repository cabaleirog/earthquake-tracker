import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EarthquakeTrackerComponent } from './pages/earthquake-tracker/earthquake-tracker.component';

const routes: Routes = [
  {
    path: '',
    component: EarthquakeTrackerComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
