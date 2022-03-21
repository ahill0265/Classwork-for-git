#light

module hw10

//
// Trapezoid integrate of F from start to stop with step
//
// Returns list as a result 
// 
// Examples: 
//          trapezoidIntegrate (fun x -> x) 0 1 0.5 => 0.5
//          trapezoidIntegrate (fun x -> x*x) 0 1 0.5 => 0.375
//          trapezoidIntegrate (fun x -> x*x) 0 0 0.5 => 0
//          
// NOTE: you can solve using tail-recursion, or using
// higher-order approach.  Whatever you prefer.
// 
// 
// 
let trapezoidIntegrate F start stop step =
    0.0

[<EntryPoint>]
let main argv =
    let t1 = trapezoidIntegrate (fun x -> x) 0 1 0.5
    if t1 = 0.5 then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let t2 = trapezoidIntegrate (fun x -> x*x) 0 1 0.5
    if t2 = 0.375 then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let t3 = trapezoidIntegrate (fun x -> x*x) 0 0 0.5 
    if t3 = 0 then
        printfn "Passed!"
    else
        printfn "Failed!"     
    0 // return an integer exit code