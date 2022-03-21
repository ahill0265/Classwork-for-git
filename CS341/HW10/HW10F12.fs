#light

module hw10

//
// derive F start stop step
//
// derive function F from start to stop, with step - Returns list as a result 
// 
// Examples: 
//          derive (fun x -> x) 0 2 1 => [1; 1]
//          derive (fun x -> x*x) -1 2 0.5 => [-.75, -.25, .25, .75, 1.25, 2.75 ] 
//          derive (fun x -> 3*x+1) 0 0 2 => []
//          
// NOTE: you can solve using tail-recursion, or using
// higher-order approach.  Whatever you prefer.
// 
// 
// 
let derive F start stop step =
    []

[<EntryPoint>]
let main argv =
    let d1 = derive (fun x -> x) 0 2 1
    if d1 = [1; 1] then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let d2 = derive (fun x -> x*x) -1 2 0.5
    if d2 = [-.75; -.25; .25; .75; 1.25; 2.75]  then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let d3 = derive (fun x -> 3*x+1) 0 0 2
    if d3 = [] then
        printfn "Passed!"
    else
        printfn "Failed!"     
    0 // return an integer exit code