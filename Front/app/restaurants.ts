export interface Restaurants{
    id: number;
    name: string;
    cuisine: string;
    rating: number;
    img: string;
}

export const RESTAURANTS: Restaurants[]=[
    {id:1,name: 'Bahandi' ,  cuisine: 'Burgers', rating: 4.5, img:"/assets/1.png"},
    {id:2,name: 'Hardees', cuisine: 'Mixed' , rating: 4.6,img:"/assets/1.png"},
    {id:3,name: 'Dodo-pizza' , cuisine: 'Pizza', rating: 4.0,img:"/assets/1.png"},
    {id:4,name: 'MacDonalds', cuisine:'Mixed', rating:4.7,img:"/assets/1.png"},
    {id:5,name:'BurgerKing',cuisine: 'Burgers',rating:4.6,img:"/assets/1.png"},
    {id:6,name:'KFC', cuisine: 'Chicken',rating : 4.8,img:"/assets/1.png"},
    {id:7, name: 'Salam-Bro', cuisine:'Burgers',rating: 4.2,img:"/assets/1.png"}
]
