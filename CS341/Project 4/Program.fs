//
// F# program to analyze Divvy daily ride data.
//
// Adam Hill
// U. of Illinois, Chicago
// CS 341, Fall 2019
// Project #04
//

#light

module project04

//
// ParseLine and ParseInput
//
// Given a sequence of strings representing Divvy data, 
// parses the strings and returns a list of lists.  Each
// sub-list denotes one bike ride.  Example:
//
//   [ [15,22,141,17,5,1124]; ... ]
//
// The values are station id (from), station id (to), bike
// id, starting hour (0..23), starting day of week (0 Sunday-6 Saturday)
// and trip duration (secs), 
//
let ParseLine (line:string) = 
  let tokens = line.Split(',')
  let ints = Array.map System.Int32.Parse tokens
  Array.toList ints

let rec ParseInput lines = 
  let rides = Seq.map ParseLine lines
  Seq.toList rides

//count occurances of x in a list
let count L x =
    let rec _count L x acc =
        match L with
        | [] -> acc
        | hd::tl when (hd = x) -> _count tl x (acc+1)
        | _::tl -> _count tl x acc
    _count L x 0

let count2 L1 L2 =
    let rec _count2 L1 L2 newL =
        match L1 with
        | [] -> List.rev newL
        | hd::tl -> _count2 tl L2 ((count L2 hd)::newL)
    _count2 L1 L2 []

//finding totaling the contents of L2 based on L1 when value in L1 = x
let sum2 L1 L2 x =
    let rec _sum2 L1 L2 x total = 
        match L1, L2 with
        | [], [] -> total
        | hd1::tl1, hd2::tl2 when (hd1 = x) -> _sum2 tl1 tl2 x (total + hd2)
        | _::tl1, _::tl2 -> _sum2 tl1 tl2 x total
    _sum2 L1 L2 x 0

//printing out the first ten values in the list
let printTopTen L =
    let rec _printTopTen L count =
        match count, L with
        | 10, _ -> ()
        | count, hd::tl -> printfn "# of rides to station %A: %A" (fst hd) (snd hd)
                           _printTopTen tl (count+1)
        //| count, hd::tl -> printf "# of rides to station %A: %A" (fst hd) (snd hd)
        //                   _printTopTen tl (count+1)
    _printTopTen L 0

//
//Functions printing a histogram
//
//Printing the stars
let rec printStars n =
  match n with
  | 0 -> ()
  | 1 -> printf "*"
  | _ -> printf "*"
         printStars (n-1)


//Making a list with just depature station ids
let ParseStationFrom L = 
    List.map(fun [x;_;_;_;_;_] -> x) L


//Making a list with just arrival station ids
let ParseStationTo L =
    List.map(fun [_;x;_;_;_;_] -> x) L
    
//
//Functions to work with bike IDs
//
//Making a list with just bike IDs
let ParseBikeID L =
    List.map(fun [_;_;x;_;_;_] -> x) L

//Making a list that only has unique bike IDs
let uniqueIDs L =
    let rec _uniqueIDs L newL =
        match L with
        | [] -> newL
        | hd::tl when (List.contains hd newL) -> _uniqueIDs tl newL
        | hd::tl -> _uniqueIDs tl (hd::newL)
    _uniqueIDs L []

//Making a list with just starting hours
let ParseStartingHour L =
    List.map(fun [_;_;_;x;_;_] -> x) L


//Making a list with just starting days of week
let ParseDayOfWeek L =
    List.map(fun [_;_;_;_;x;_] -> x) L


//Making a list with just trip durations
let ParseTripDuration L =
    List.map(fun [_;_;_;_;_;x] -> x) L

[<EntryPoint>]
let main argv =
  //
  // input file name, then input divvy ride data and build
  // a list of lists:
  //
  printf "filename> "
  let filename = System.Console.ReadLine()
  let contents = System.IO.File.ReadLines(filename)
  let ridedata = ParseInput contents
  let stationFrom = ParseStationFrom ridedata
  let stationTo = ParseStationTo ridedata
  let bikeIDs = ParseBikeID ridedata
  let startingHour = ParseStartingHour ridedata
  let dayOfWeek = ParseDayOfWeek ridedata
  let tripDuration = ParseTripDuration ridedata


  //printfn "%A" ridedata
  let N = List.length ridedata
  printfn ""
  printfn "# of rides: %A" N
  printfn ""

  let numBikes = uniqueIDs bikeIDs
  printfn "# of bikes: %A" (List.length numBikes)
  printfn ""

  printf "BikeID> "
  let inputID = System.Console.ReadLine()
  let intID = inputID |> int
  let numIDs = count bikeIDs intID
  let rawTime = sum2 bikeIDs tripDuration intID
  let minutes = rawTime/60
  let seconds = rawTime%60
  let averageTime = (rawTime |> double) / (numIDs |> double)
  printfn ""
  printfn "# of rides for BikeID %A: %i" intID numIDs
  printfn ""
  printfn "Total time spent riding BikeID %A: %A minutes %A seconds" intID minutes seconds
  printfn ""
  printfn "Average time spent riding BikeID %A: %.2f seconds" intID averageTime
  printfn ""

  printf "StationID> "
  let inputStationID = System.Console.ReadLine()
  let stationID = inputStationID |> int
  let numStationID = count stationTo stationID
  let rawTime = sum2 stationTo tripDuration stationID
  let averageTime = (rawTime |> double) / ((count stationTo stationID) |> double)

  printfn ""
  printfn "# of rides to StationID %A: %A" stationID numStationID
  printfn ""
  printfn "Average time spent on trips leading to StationID %A: %.2f seconds" stationID averageTime
  printfn ""

  printfn "Number of Trips on Sunday: %A" (count dayOfWeek 0)
  printfn "Number of Trips on Monday: %A" (count dayOfWeek 1)
  printfn "Number of Trips on Tuesday: %A" (count dayOfWeek 2)
  printfn "Number of Trips on Wednesday: %A" (count dayOfWeek 3)
  printfn "Number of Trips on Thursday: %A" (count dayOfWeek 4)
  printfn "Number of Trips on Friday: %A" (count dayOfWeek 5)
  printfn "Number of Trips on Saturday: %A" (count dayOfWeek 6)
  printfn ""

  printf "0: "
  printStars ((count dayOfWeek 0)/10)
  printfn " %A" (count dayOfWeek 0)

  printf "1: "
  printStars ((count dayOfWeek 1)/10)
  printfn " %A" (count dayOfWeek 1)

  printf "2: "
  printStars ((count dayOfWeek 2)/10)
  printfn " %A" (count dayOfWeek 2)

  printf "3: "
  printStars ((count dayOfWeek 3)/10)
  printfn " %A" (count dayOfWeek 3)

  printf "4: "
  printStars ((count dayOfWeek 4)/10)
  printfn " %A" (count dayOfWeek 4)

  printf "5: "
  printStars ((count dayOfWeek 5)/10)
  printfn " %A" (count dayOfWeek 5)

  printf "6: "
  printStars ((count dayOfWeek 6)/10)
  printfn " %A" (count dayOfWeek 6)
  printfn ""


  let uniqueStationIDs = uniqueIDs stationTo
  let countStationIDs = count2 uniqueStationIDs stationTo

  let stationIDCountPair = List.map2(fun x y -> (x,y)) uniqueStationIDs countStationIDs
  let sortedList = List.rev (List.sortBy (fun (_,y) -> y) (List.rev (List.sortBy (fun(x,_) -> x) stationIDCountPair)))

  printTopTen sortedList
  printfn ""

  0 
