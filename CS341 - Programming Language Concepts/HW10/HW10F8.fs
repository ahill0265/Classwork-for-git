#light

module hw10

//
// Applies a function f to each element of the collection, threading an accumulator argument through the computation.
//
// Returns a value 
// 
// Examples: 
//          fold (fun x y -> x&&y) true [] => true
//          fold (fun x y -> x+(string y)) "Hello " ['W';'o';'r';'l';'d'] => "Hello World"
//          fold (fun x y -> x+y) -60 [23; 43; 6] => 12
//          
// NOTE: you can solve using tail-recursion, or using
// higher-order approach.  Whatever you prefer.
// You may not call List.fold directly in your solution.
// 
// 
// 
let fold F start L = 
    match L with
    | [] -> start
    | hd::tl -> let result = (F start hd)
                fold F result tl

[<EntryPoint>]
let main argv =
    let f1 = fold (fun x y -> x&&y) true []
    if f1 = true then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let f2 = fold (fun x y -> x+(string y)) "Hello " ['W';'o';'r';'l';'d']
    if f2 = "Hello World" then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let f3 = fold (fun x y -> x+y) -60 [23; 43; 6]
    if f3 = 12 then
        printfn "Passed!"
    else
        printfn "Failed!"
    0 // return an integer exit code