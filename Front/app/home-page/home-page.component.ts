import { Component } from '@angular/core';
import { RESTAURANTS, Restaurants } from '../restaurants';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
  
})
export class HomePageComponent {
  restaurants: Restaurants[] = RESTAURANTS
}

