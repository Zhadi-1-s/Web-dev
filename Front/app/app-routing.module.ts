import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RestaurantsComponent } from './restaurants/restaurants.component';
import { HomePageComponent } from './home-page/home-page.component';
import { TopSellersComponent } from './top-sellers/top-sellers.component';
import { RestaurantMenuComponent } from './restaurant-menu/restaurant-menu.component';
import { AdminsComponent } from './admins/admins.component';
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  {path : 'restaurants', component: RestaurantsComponent},
  {path: '',component:HomePageComponent},
  {path:'home',component:HomePageComponent},
  {path: 'restaurants/:id', component: RestaurantMenuComponent},
  {path:'top-sellers',component:TopSellersComponent},
  {path: 'admins', component: AdminsComponent},
  {path:'login',component:LoginComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
