#light

module hw10

//
// min L
//
// Returns minimum element of L
// 
// Examples: min []          => raises an exception (Unhandled Exception: System.ArgumentException: The input sequence was empty.)
//           min [-2; 4]     => -2
//           min [34]        => 34
//           min [10; 10; 9] => 9 
// 
// NOTE: you can solve using tail-recursion, or using
// higher-order approach.  Whatever you prefer.
// You may not call List.min directly in your solution.
// 
// 
// 
let min L =
    let rec _min L result = 
        match L with
        | [] -> result
        | hd::tl when (hd < result) -> _min tl hd
        | _::tl -> _min tl result
    match L with
    | [] -> raise (new System.ArgumentException("The input sequence was empty."))
    | _ -> _min L (List.head L)

[<EntryPoint>]
let main argv =
    let min2 = min [-2; 4]
    if min2 = -2 then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let min3 = min [34]
    if min3 = 34 then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let min4 = min [10; 10; 9]
    if min4 = 9 then
        printfn "Passed!"
    else
        printfn "Failed!"     
    0 // return an integer exit code