#light

module hw10

//
// length L
//
// Returns length of L
// 
// Examples: length []  => 0
//           length [1] => 1
//           length [1; 3; 98] => 3
// 
// NOTE: you can solve using tail-recursion, or using
// higher-order approach.  Whatever you prefer.
// You may not call List.length directly in your solution.
// 
// 
let length L = 
    List.sum (List.map(fun x -> 1) L)


[<EntryPoint>]
let main argv =
    let len1 = length []
    if len1 = 0 then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let len2 = length [1]
    if len2 = 1 then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let len3 = length [1; 3; 98]
    if len3 = 3 then
        printfn "Passed!"
    else
        printfn "Failed!"
    0 // return an integer exit code