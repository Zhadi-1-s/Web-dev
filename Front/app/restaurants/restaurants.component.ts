import { Component } from '@angular/core';
import { RESTAURANTS , Restaurants } from '../restaurants';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-restaurants',
  templateUrl: './restaurants.component.html',
  styleUrls: ['./restaurants.component.css']
})
export class RestaurantsComponent {
  restaurants: Restaurants[] = RESTAURANTS;

  searchItem:any;

  // constructor(private http:HttpClient){
  //   this.http.get<Restaurants[]>('/api/restaurants').subscribe(data=>{
  //     this.restaurants = data
  //   })
  // }
}

