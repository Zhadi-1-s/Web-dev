import {Pipe, PipeTransform} from '@angular/core';
import { Restaurants } from './restaurants';


@Pipe({
    name: 'filter'
})

export class FilterPipe implements PipeTransform{
    transform(restaurants: Restaurants[], searchText: string):any[] {
        if(!restaurants) return[];
        if(!searchText) return restaurants;

        searchText = searchText.toLowerCase();

        return restaurants.filter(val => {
            return val.name.toLowerCase().startsWith(searchText);
        });
    }
}