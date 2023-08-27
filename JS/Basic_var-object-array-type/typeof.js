let week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
console.log(typeof week); // -> object


let days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
let day = "Sunday";
   
console.log(typeof days); // -> object
console.log(typeof day); // -> string
   
console.log(days instanceof Array); // -> true
console.log(day instanceof Array); // -> false