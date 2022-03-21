#light

module hw10

//
// iter F L
//
// Applies function F to L (NOTE: its behaviour is similar to built in List.iter)
// 
// Examples: iter (fun x -> printfn "%A squared is %A" x*x ) [1; 2] => 1 squared is 1
//                                                                     2 squared is 4
//           iter (fun x -> printf "%A" x) ['t'; 'r'; 'u'; 'e']     => true
//           iter (fun x -> printfn "Iterating...") []              => 
// 
// NOTE: you can solve using tail-recursion, or using
// higher-order approach.  Whatever you prefer.
// You may not call List.iter directly in your solution.
// 
// 
// 
let iter F L =
    match L with
    | [] -> F 
    | hd::[] -> (F hd) 
    | hd::tl -> (F hd)
                iter F tl

[<EntryPoint>]
let main argv =
    0 // return an integer exit code