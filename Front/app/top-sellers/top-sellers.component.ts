import { Component } from '@angular/core';
import { RESTAURANTS, Restaurants } from '../restaurants';


@Component({
  selector: 'app-top-sellers',
  templateUrl: './top-sellers.component.html',
  styleUrls: ['./top-sellers.component.css']
})
export class TopSellersComponent {
  restaurants: Restaurants[] = RESTAURANTS
}
