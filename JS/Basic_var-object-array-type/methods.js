// The indexOf method is used to search the array to locate a given value

let names = ["Olivia", "Emma", "Mateo", "Samuel"];
console.log(names.indexOf("Mateo")); // -> 2
console.log(names.indexOf("Victor")); // -> -1 - since the element is not found


// The push method places the element given as its argument at the end of the array

console.log(names.length); // -> 4
names.push("Amelia");
console.log(nnames.length); // -> 5
console.log(nnames); // - > ["Olivia", "Emma", "Mateo", "Samuel", "Amelia"]

// The unshift method works similarly to push, the difference being that a new element is added to the beginning of the array. 

names.unshift("vikram");
console.log(names.indexOf("vikram")); // -> 0
console.log(names.length); // - > 6 ["vikram, "Olivia", "Emma", "Mateo", "Samuel", "Amelia"]


// The pop method allows you to remove the last element from the array

console.log(names.length); // -> 6
names.pop();
console.log(names.length); // -> 5
console.log(names); // -> ["vikram, "Olivia", "Emma", "Mateo", "Samuel"]

//The shift method works similarly to pop, only this time we remove the element from the beginning of the array

console.log(names.length); // -> 4   
names.shift();
console.log(names.length); // -> 5
console.log(names); // -> ["Olivia", "Emma", "Mateo", "Samuel"]


//The reverse method reverses the order of elements in the array

names.reverse();
console.log(names); // - > ["Samuel", "Mateo", "Emma", "Olivia"]


//The concat method creates a new array by attaching elements from the array given as an argument to the original array elements

let conames = ["Olivia", "Emma", "Mateo", "Samuel"];
let otherNames = ["William", "Jane"];
let allNames = conamesnames.concat( otherNames);
   
console.log(names); // -> ["Olivia", "Emma", "Mateo", "Samuel"]
console.log(otherNames); // -> ["William", "Jane"]
console.log(allNames); // -> ["Olivia", "Emma", "Mateo", "Samuel", "William", "Jane"]