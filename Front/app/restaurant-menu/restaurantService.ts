import {Injectable} from '@angular/core'

@Injectable({
    providedIn: 'root'
})

export class RestaurantService{
    rest = [
        {
            id: 1,
            name: 'Bahandi',
            menu:[
                {name: 'ChickenBurger', price:'1500'},
                {name: 'Burger', price: '1700'},
                {name: 'Mixburger', price: '1600'}
            ]
        },
        {
            id:2,
            name: 'Hardees',
            menu:[
                {name: 'DoubleMixburger', price:'2300'},
                {name: 'BarbequeBurger', price:'2500'},
                {name:'TandyrSamsa', price:'2000'}
            ]
        },
        {
            id:3,
            name: 'DodoPizza',
            menu:[
                {name: 'Margarita',price:3700},
                {name:'Peperoni',price:3700},
                {name: 'Beshbarmak',price:5000}
            ]
        },
        {
            id:4,
            name:'Macdonalds',
            menu:[
                {name:'Hamburger',price:800},
                {name:'CheesBurger',price:1000},
                {name:'ChickenBurger',price:900}
            ]
        },
        {
            id:5,
            name:'BurgerKing',
            menu:[
                {name:'BurgerCombo',price:1300},
                {name:'CheesBurgerCombo',price:1600},
                {name:'BigTastyCombo',price:2000}
            ]
        },
        {
            id:6,
            name:'KFC',
            menu:[
                {name:'Chikcen-Basket L',price:5300},
                {name:'Basket M',price:4200},
                {name:'Basket S',price:3500}
            ]
        },
        {
            id:7,
            name:'Salam-Bro',
            menu:[
                {name: 'Combo for both', price : 3290},
                {name: 'Iftar-Menu',price:3500},
                {name:'chicken-combo',price:1890}
            ]
        }
    ]
    constructor(){}

    getRestaurants(){
        return this.rest;
    }
    getRestaurantById(id: number){
        return this.rest.find((r)=> r.id == id);
    }
    getMenuForRestaurant(id: number){
        const rest = this.getRestaurantById(id);
        return rest?.menu
    }
}