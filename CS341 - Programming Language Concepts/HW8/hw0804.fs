#light

module hw08

//
// countBetween A B L
//
// Given a list L of integers, counts A < x < B : x in L.
// Example: countBetween 20 60 [100; 19; 90; 50; 60; 45] => 2
// 
// NOTE: write this using a higher-order approach, in 
// particular using List.map and List.sum, or List.filter
// and List.length.  Do not use other List. functions.
// 
let countBetween A B L = 
    let L2 = List.filter(fun x -> ((A < x) && (x < B))) L
    let L3 = List.map(fun x -> 1) L2
    List.sum L3
