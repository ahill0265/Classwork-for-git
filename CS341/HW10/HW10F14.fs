#light

module hw10

//
// Rectangular integrate of F from start to stop with step
//
// Returns list as a result 
// 
// Examples: 
//          rectanglesIntegrate (fun x -> x) 0 1 0.5 => 0.25
//          rectanglesIntegrate (fun x -> x*x) 0 1 0.5 => 0.125
//          rectanglesIntegrate (fun x -> x*x) 0 0 0.5 => 0
//          
// NOTE: you can solve using tail-recursion, or using
// higher-order approach.  Whatever you prefer.
// 
// 
// 
let rectanglesIntegrate F start stop step =
    0.0

[<EntryPoint>]
let main argv =
    let s1 = rectanglesIntegrate (fun x -> x) 0 1 0.5
    if s1 = 0.25 then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let s2 = rectanglesIntegrate (fun x -> x*x) 0 1 0.5
    if s2 = 0.125 then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let s3 = rectanglesIntegrate (fun x -> x*x) 0 0 0.5 
    if s3 = 0 then
        printfn "Passed!"
    else
        printfn "Failed!"     
    0 // return an integer exit code