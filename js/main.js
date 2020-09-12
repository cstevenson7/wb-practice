//syntax to Create new MAP-  new Map (Object.entries());
// let highs = new Map(Object.entries({
//     "Banff": [19.44, "clear sky"],    
//     "Nordegg": [18.04, "clear sky"],
//     "Calgary": [23.33, "few clouds"],
//     "Edmonton":[22.78, "overcast clouds"],
//     "Jasper" : [19.14, "clear sky"]
// }));

// var list = { "a":4, "b":0.5 , "c":0.35, "d":5 };
// var min = list[0]; // ignoring case of empty list for conciseness
// var max = list[0];
// var i;
// for (i = 1; i < list.length; i++) {
//     if (list[i] < min) min = list[i];
//     if (list[i] > max) max = list[i];
// }


// let highs1 =
//      {"Banff": [19.44, "clear sky"],    
//     "Nordegg": [18.04, "clear sky"],
//     "Calgary": [23.33, "few clouds"],
//     "Edmonton":[22.78, "overcast clouds"],
//     "Jasper" : [19.14, "clear sky"]}
// ;
//console.log(highs)
 
// high1_len = Object.keys(highs1).length
// console.log(high1_len)
// max_temp = highs1[0][0]

// // if(high1_len < 1){
// //     // middle index  should be two for alberta
// //     //lefthalf = hige
       
// // }
// // let mid = Math.floor(high1_len/2);
// // console.log(mid)
//  highs_arr = Object.entries(highs1)
// // console.log(highs_arr)
// max_temp = highs_arr[0][0]


// //*******************This works!!
let  homes = [
    {
        "h_id": "3",
        "city": "Dallas",
        "state": "TX",
        "zip": "75201",
        "price": "162500"
    }, {
        "h_id": "4",
        "city": "Bevery Hills",
        "state": "CA",
        "zip": "90210",
        "price": "319250"
    }, {
        "h_id": "5",
        "city": "New York",
        "state": "NY",
        "zip": "00010",
        "price": "962500"
    }
];

// homes.sort(function(a, b) {
//     return parseFloat(a.price) - parseFloat(b.price);
// });

// sortedList = homes.sort((a, b) => parseFloat(b.price) - parseFloat(a.price));
// console.log(sortedList)

let temps = [
{city: "Banff", current: -10.32, description: "rain"},
{city: "Calgary", current: 10.32, description: "sunny"},
{city: "Edmonton", current: 20.69, description: "cloudy"}];

// homes.sort(function(a, b) {
//     return parseFloat(a.price) - parseFloat(b.price);
// });

sortedTemps = temps.sort((a, b) => parseFloat(b.current) - parseFloat(a.current));
//console.log(sortedTemps)

let ab_city = [];
let ab_current = [];
let ab_description= [];
for (let i = 0; i < 4; i++){
    //let ab_city_ + i.toString() = sortedTemps.city[1]
    ab_city[i] = sortedTemps[i].city
    ab_current[i] = sortedTemps[i].current
    ab_description[i] = sortedTemps[i].description
    console.log(ab_city[i],ab_current[i],ab_description[i])
}

    // console.log(values1) 

    // let keys = ['city','current','description'];

    // let arrayOfObjects = [];
    // console.log('befor loop',values1) 
    // console.log('Value len',values1.length)

    // for(let i=0; i<values1.length; i++){        
    //     let obj = {};
    //     console.log('Inloop',values1) 
    //     for(let j=0; j<values1[i].length; j++){
    //          obj[keys[j]] = values1[i][j];  
    //       }
    //     arrayOfObjects.push(obj);
    // }
    // console.log('From JSON', arrayOfObjects)

//     ab_top4 = tempsArray()
//     console.log('abtop 4',ab_top4)
//     //sorted list of objects DESC
//     sorted_ab_top4 = ab_top4.sort((a, b) => parseFloat(b.current) - parseFloat(a.current));
//     console.log('Sorted', sorted_ab_top4)
    
//     return sorted_ab_top4

// var keys = ['key1', 'key2', 'key3'];
// var values = [
//             [12,112, 1112],
//             [31, 331, 3331],
//             [64, 65, 66]
//          ];

// var arrayOfObjects = [];
// for(var i=0; i<values.length; i++){
//     var obj = {};
//     for(var j=0; j<values[i].length; j++){
//          obj[keys[j]] = values[i][j];  
//       }
//     arrayOfObjects.push(obj);
// }
//  console.log(arrayOfObjects)

//let keys = ['key1', 'key2', 'key3'];
// let values = [
//             ["Banff",25.32, "rain"],
//             ["Calgary", 33.1, "sunny"],
//             ["Edmonton", 20.69, "cloudy"]
//          ];

// let keys = ['city','current','description']

// let arrayOfObjects = [];
// for(let i=0; i<values.length; i++){
//     let obj = {};
//     for(let j=0; j<values[i].length; j++){
//          obj[keys[j]] = values[i][j];  
//       }
//     arrayOfObjects.push(obj);
// }
//  console.log(arrayOfObjects)

