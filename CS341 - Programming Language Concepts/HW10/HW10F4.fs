#light

module hw10

//
// nth n L
//
// Returns nth element of L
// 
// Examples: nth 0  []          => raises an exception
//           nth 2  [94]        => raises an exception
//           nth 1  [94]        => 94
//           nth -1 [94]        => raises an exception 
//           nth 2  [1; 45; 6]  => 45
// NOTE: you can solve using tail-recursion, or using
// higher-order approach.  Whatever you prefer.
// You may not call List.nth, List.Item, .[], etc directly in your solution.
// 
// 
// 
let nth n L =
    let rec _nth n L count = 
        match L with
        | hd::_ when (n = count) -> hd
        | _::tl -> _nth n tl (count + 1)
    match L with
    | [] -> raise (new System.ArgumentException "Don't do that")
    | _::_ when (n <= 0) -> raise (new System.ArgumentException "Don't do that")
    | _ -> _nth n L 1

let nth2 = nth 1 [94]

[<EntryPoint>]
let main argv =
    let nth2 = nth 1 [94]
    if nth2 = 94 then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let nth3 = nth 2 [1; 45; 6]
    if nth3 = 45 then
        printfn "Passed!"
    else
        printfn "Failed!"
      
    0 // return an integer exit code