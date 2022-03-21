#light

module hw10

//
// slope of F at point
//
// slope of function F at a point with the
// second parameter used as the computational delta.
// Use the difference between F(x) and F(x+delta) to
// compute the slope - Returns a value
// 
// Examples: 
//          slope (fun x -> x) 0 0.001 => 1
//          slope (fun x -> x*x) 0 0.5 => 0
//          slope (fun x -> x*x) 2 1 => 5
//          
// NOTE: you can solve using tail-recursion, or using
// higher-order approach.  Whatever you prefer.
// 
// 
// 
let slope F point delta = 
    0.0

[<EntryPoint>]
let main argv =
    let s1 = slope (fun x -> x) 0 0.001
    if s1 = 1 then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let s2 = slope (fun x -> x*x) 0 0.5
    if s2 = 0 then
        printfn "Passed!"
    else
        printfn "Failed!"
        
    let s3 = slope (fun x -> x*x) 2 1
    if s3 = 5 then
        printfn "Passed!"
    else
        printfn "Failed!"     
    0 // return an integer exit code