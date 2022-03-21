// Learn more about F# at http://fsharp.org

open System
    
//module hw07 
    
//
//explode:
//
// Given a string s, explods the string into a list of characters.
// Example: explode "apple" => ['a'; 'p'; 'p'; 'l'; 'e']
//
let explode s = 
    Seq.toList s
      
//
//implode:
//
// The opposite of explode --- given a list of characters, returns 
// the list as a string. Example: implode ['t; 'h; 'e] => "the"
//
let implode L = 
    let sb = System.Text.StringBuilder()
    L |> List.iter (fun c -> ignore (sb.Append (c:char)))
    sb.ToString()
      
// YOUR FUNCTIONS HERE

let rec length L =
    match L with
    | [] -> 0
    | hd::tl -> 1 + length tl

let rec vowels L x =
    match L with
    | [] -> 0
    | hd::tl when hd = x -> 1 + vowels tl x
    | hd::tl -> vowels tl x

let rec capitalize L =
    match L with
    | [] -> []
    | hd::tl when hd = 'a' -> 'A'::capitalize tl
    | hd::tl when hd = 'e' -> 'E'::capitalize tl
    | hd::tl when hd = 'i' -> 'I'::capitalize tl
    | hd::tl when hd = 'o' -> 'O'::capitalize tl
    | hd::tl when hd = 'u' -> 'U'::capitalize tl
    | hd::tl -> hd::capitalize tl



      
      
[<EntryPoint>] 
let main argv = 
    printf "input> " 
    let input   = System.Console.ReadLine() 

    let L = explode input
    let L2 = capitalize L
    let s = implode L2


    let inputLength = length L
    let numA = vowels L 'a'
    let numE = vowels L 'e'
    let numI = vowels L 'i'
    let numO = vowels L 'o'
    let numU = vowels L 'u'
    let numVowels = numA + numE + numI + numO + numU


    printf "length: %A\n" inputLength
    printf "vowels: %A\n" numVowels
    printf "a: %A\n" numA
    printf "e: %A\n" numE
    printf "i: %A\n" numI
    printf "o: %A\n" numO
    printf "u: %A\n" numU
    printf "Capitalized: %A\n" s

    //
    0
