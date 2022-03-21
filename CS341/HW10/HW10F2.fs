#light

module hw10

//
// max L
//
// Returns maximum element of L
// 
// Examples: max []          => raises an exception (Unhandled Exception: System.ArgumentException: The input sequence was empty.)
//           max [-2; 4]     => 4
//           max [34]        => 34
//           max [10; 10; 9] => 10
// 
// NOTE: you can solve using tail-recursion, or using
// higher-order approach.  Whatever you prefer.
// You may not call List.max directly in your solution.
// 
// 
// 
let max L =
    let rec _max L result =
        match L with
        | [] -> result
        | hd::tl when (hd > result) -> _max tl hd
        | _::tl -> _max tl result
    match L with
    | [] -> raise (new System.ArgumentException("The input sequence was empty."))
    | _ -> _max L (List.head L)

[<EntryPoint>]
let main argv =
    let max2 = max [-2; 4]
    if max2 = 4 then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let max3 = max [34]
    if max3 = 34 then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let max4 = max [10; 10; 9]
    if max4 = 10 then
        printfn "Passed!"
    else
        printfn "Failed!"     
    0 // return an integer exit code