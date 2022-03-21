#light

module hw10

//
// map F L
//
// Maps function F to L - Returns list as a result of mapping function F on L
// 
// Examples: (fun x -> x + 1) []                  => []
//           (fun x -> x + 1) [23]                => [24]
//           (fun x -> x - 1) [23; 43]            => [22; 42]
// 
// NOTE: you can solve using tail-recursion, or using
// higher-order approach.  Whatever you prefer.
// You may not call List.map directly in your solution.
// 
// 
// 
let map F L =
    let rec _map F L newL =
        match L with
        | [] -> List.rev newL
        | hd::tl -> _map F tl ((F hd)::newL)
    _map F L []

[<EntryPoint>]
let main argv =
    let map1 = map (fun x -> x + 1) []
    if map1 = [] then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let map2 = map (fun x -> x + 1) [23]
    if map2 = [24] then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let map3 = map (fun x -> x - 1) [23; 43]
    if map3 = [22; 42] then
        printfn "Passed!"
    else
        printfn "Failed!"     
    0 // return an integer exit code