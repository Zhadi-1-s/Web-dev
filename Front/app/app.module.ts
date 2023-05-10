import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RestaurantsComponent } from './restaurants/restaurants.component';
import { HomePageComponent } from './home-page/home-page.component';
import { TopSellersComponent } from './top-sellers/top-sellers.component';
import { RestaurantMenuComponent } from './restaurant-menu/restaurant-menu.component';
import { AdminsComponent } from './admins/admins.component';
import { FormsModule } from '@angular/forms';
import { LoginComponent } from './login/login.component';
import { Pipe,PipeTransform } from '@angular/core';
import { FilterPipe } from './toSearch.pipe';
import {MatInputModule} from '@angular/material/input';
import {MatAutocompleteModule} from '@angular/material/autocomplete';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent,
    RestaurantsComponent,
    HomePageComponent,
    TopSellersComponent,
    RestaurantMenuComponent,
    AdminsComponent,
    LoginComponent,
    FilterPipe
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    MatAutocompleteModule,
    MatInputModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
