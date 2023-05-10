import { Component , OnInit} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Restaurants } from '../restaurants';
import { RestaurantService } from './restaurantService';

@Component({
  selector: 'app-restaurant-menu',
  templateUrl: './restaurant-menu.component.html',
  styleUrls: ['./restaurant-menu.component.css'],
  providers: [RestaurantService]
})

export class RestaurantMenuComponent implements OnInit{

  restaurantId!: number;
  restaurant: any;
  menu: any

  constructor(private route: ActivatedRoute, private restaurantService: RestaurantService){}

  ngOnInit(): void {
        this.restaurantId = +this.route.snapshot.params['id']!;
        this.menu = this.restaurantService.getMenuForRestaurant(this.restaurantId)
  }
}
