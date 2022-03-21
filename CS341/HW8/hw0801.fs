#light

module hw08

//
// sum5xplus3 L
//
// Given a list L of integers, computes sum (5*x+3) for over all x in L.
// Example: sum5xplus3 [3; 1; 2] => 39
// 
// NOTE: write a tail-recursive version using a helper function;
// do not change the API of the original sum5xplus3 function.
// 
let sum5xplus3 L =
  let rec _sum5xplus3 L sum =
    match L with
    | [] -> sum
    | hd::tl -> _sum5xplus3 tl (sum+((hd*5)+3))
  _sum5xplus3 L 0
