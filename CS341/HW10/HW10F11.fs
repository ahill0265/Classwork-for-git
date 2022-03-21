#light

module hw10

//
// Unzip a list of pairs to a pair of lists
//
// Returns tuple of lists
// 
// Examples: 
//          unzip [] => ([], [])
//          unzip [(1, 3); (2, 56); (40, 6)] => ([1; 2; 40], [3; 56; 6])
//          
// NOTE: you can solve using tail-recursion, or using
// higher-order approach.  Whatever you prefer.
// You may not call List.unzip directly in your solution.
// 
// 
// 
let unzip L = 
    let rec _unzip L newL1 newL2 =
        match L with
        | [] -> newL1 newL2
        | (x,y)::tl -> _unzip tl (x::newL1) (y::newL2)
    _unzip L [] []

[<EntryPoint>]
let main argv =
    let u11,u12 = unzip []
    if (u11 = []) && (u12 = []) then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let u21,u22 = unzip [(1, 3); (2, 56); (40, 6)]
    if (u21 = [1; 2; 40]) && (u22 = [3; 56; 6]) then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    0 // return an integer exit code