#light

module hw08

//
// sum5xplus3 L
//
// Given a list L of integers, computes sum (5*x+3) for over all x in L.
// Example: sum5xplus3 [3; 1; 2] => 39
// 
// NOTE: write this using a higher-order approach, in 
// particular using List.map and List.sum.  Do not use
// other List. functions.
// 
let sum5xplus3 L = 
  let L = List.map(fun x -> (5*x+3)) L
  List.sum L
