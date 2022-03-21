#light

module hw08

//
// countBetween A B L
//
// Given a list L of integers, counts A < x < B : x in L.
// Example: countBetween 20 60 [100; 19; 90; 50; 60; 45] => 2
// 
// NOTE: write a tail-recursive version using a helper function;
// do not change the API of the original countBetween function.
// 
let countBetween A B L = 
    let rec _countBetween A B L count =
        match L with
        | [] -> count
        | hd::tl when ((A < hd) && (hd < B)) -> _countBetween A B tl (count + 1)
        | hd::tl -> _countBetween A B tl count
    _countBetween A B L 0
