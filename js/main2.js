//Codewars level 8
//Test.assertEquals(numberToString(67), '67'

// function numberToString(num) {  
//   let n = num.toString();
//   return n
// }

// num = 67
// console.log(num)


//While making a game, your partner, Greg, decided to create a function to check if the user is still alive called checkAlive/CheckAlive/check_alive.
// Unfortunately, Greg made some errors while creating the function.//checkAlive/CheckAlive/check_alive should return true if the player's 
// health is greater than 0 or false if it is 0 or below.//The function receives one parameter health which will always be a whole number between -10 and 10.

// function checkAlive(health) {
//   if (health <= 0){    
//     return false
//   } else {
//     return true
//   }
// }

//Level 7
// The of incredible dull things
// The museum of incredible dull things wants to get rid of some exhibitions. Miriam, the interior architect, comes up with a plan to remove the most boring exhibitions. She gives them a rating, and then removes the one with the lowest rating.// However, just as she finished rating all exhibitions, she's off to an important fair, so she asks you to write a program that tells her the ratings of the items after one removed the lowest one. Fair enough.
// Task
// Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.// Don't 
//change the order of the elements that are left.

//SPLICE removes elements from an array and inserts

//*(***SEEMS TO WORK CANT FIND QUESTION AGAIN)

// function removeSmallest(numbers) {
//     if (numbers.length > 0){
//         copy_nums = Array.from(numbers);
//         copy_nums.sort()
//         for(i = 0; i < numbers.length; i++){
//           if (numbers[i] == copy_nums[0]){
//             //This removes the value, but leave a space in the list
//              // delete numbers[i];            
//               numbers.splice([i],1);
//               return numbers
//           }
//         }
//     }
// }

// console.log(removeSmallest([2,2,1,2,1]))      //= [2,3,4,5]
//removeSmallest([5,3,2,1,4])      //= [5,3,2,4]
//removeSmallest([2,2,1,2,1])      //= [2,2,2,1]

 //Sort Numbers 7

//  Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

// For example:

// solution([1, 2, 10, 50, 5]); // should return [1,2,5,10,50]
// solution(null); // should return []


//*****************TO CHECK FOR NULL or EMPTY arrays

// if (!Array.isArray(array) || !array.length) {

// }

// To break it down:

// Array.isArray(), unsurprisingly, checks whether its argument is an array. This weeds out values like null, undefined and anything else that is not an array.
// Note that this will also eliminate array-like objects, such as the arguments object and DOM NodeList objects. Depending on your situation, this might not be the behavior you're after.

// The array.length condition checks whether the variable's length property evaluates to a truthy value. Because the previous condition already established that we are indeed dealing with an array, more strict comparisons like array.length != 0 or array.length !== 0 are not required here.

// function solution(nums){
//   if (!Array.isArray(array) || !array.length) {
//     nums.sort()
//     return nums
//   }
// // }
// **************Isograms 7
// An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

// Test.assertSimilar( isIsogram("Dermatoglyphics"), true );
// Test.assertSimilar( isIsogram("isogram"), true );
// Test.assertSimilar( isIsogram("aba"), false, "same chars may not be adjacent" );
// Test.assertSimilar( isIsogram("moOse"), false, "same chars may not be same case" );
// Test.assertSimilar( isIsogram("isIsogram"), false );
// Test.assertSimilar( isIsogram(""), true, "an empty string is a valid isogram" );

  function isIsogram(str){
    let i, j;
    str = str.toLowerCase();
    for(i = 0; i < str.length; ++i)
      for(j = i + 1; j < str.length; ++j)
        if(str[i] === str[j])
          return false;
    return true;
  }
str = "moOse"
console.log(isIsogram(str))

// *******************Complementary DNA 7

// Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

// If you want to know more http://en.wikipedia.org/wiki/DNA

// In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
// Test.assertEquals(DNAStrand("AAAA"),"TTTT","String AAAA is");
// Test.assertEquals(DNAStrand("ATTGC"),"TAACG","String ATTGC is");
// Test.assertEquals(DNAStrand("GTAT"),"CATA","String GTAT is");

function DNAStrand(dna){
    comp_dna = " "
    for (i = 0; i < dna.length; i++){
      switch(dna[i]){
        case "A":
          comp_dna = comp_dna + "T";
          continue
        case "T":
          comp_dna = comp_dna + "A";
          continue
        case "C":
          comp_dna = comp_dna + "G";
          continue
        case "G":
          comp_dna = comp_dna + "C";
          continue
    }
   
  }
  return comp_dna
}

dna = "AAAA"
console.log(DNAStrand(dna))


//*****************Find the middle element 7


// As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements.
// The input to the function will be an array of three distinct numbers (Haskell: a tuple).
// For example:
// gimme([2, 3, 1]) => 0
// 2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.

// Another example (just to make sure it is clear):
// gimme([5, 10, 14]) => 1
// 10 is the number that fits between 5 and 14 and the index of 10 in the input array is 1.


function gimmie(inputArray) {
    arr_s = Array.from(inputArray);
    arr_s.sort(((a,b)=>a-b));
    console.log(arr_s)
    mid_index = 0;
    for( i = 0; i < inputArray.length; i++){
        if(inputArray[i] == arr_s[1]){
          mid_index = i;
          return mid_index
        }        
      }    
}

inputArray = [5,10,14]
console.log(gimmie(inputArray))


// **************Shortest Word 7
// Simple, given a string of words, return the length of the shortest word(s).

// String will never be empty and you do not need to account for different data types.

// Test.describe("Example tests",_=>{
//   Test.assertEquals(findShort("bitcoin take over the world maybe who knows perhaps"), 3);
//   Test.assertEquals(findShort("turns out random test cases are easier than writing out basic ones"), 3); 
//   });

function findShort(s){
    let s_list = s.split(' ');
    let s_dict = {}
    for(i =0; i < s_list.length; i++){
      s_dict[s_list[i]] = s_list[i].length;
    }  
    let arr = Object.values(s_dict)
    let min = Math.min(...arr);
    return min
  }
  
  s = "turns out random test cases are easier than writing out basic a ones"
  console.log(findShort(s))
  

  //***************Summing a number's digits 7
// Write a function named sumDigits which takes a number as input and returns the sum of the absolute
 //value of each of the number's decimal digits. For example:

//   sumDigits(10);  // Returns 1
//   sumDigits(99);  // Returns 18
//   sumDigits(-32); // Returns 5
// Let's assume that all numbers in the input will be integer values.


function sumDigits(number) {    
  let total = 0;
  let num_str = ''; 

  if (number < 0){
    number = number * -1
  }
  num_str = number.toString();
     
  for (let i =0; i < num_str.length; i++){
    total += parseInt(num_str[i])
  }
  return total
}

number = 99
console.log(sumDigits(number))


//****************Simple Fun #176: Reverse Letter
// Task
// Given a string str, reverse it omitting all non-alphabetic characters.
// Example
// For str = "krishan", the output should be "nahsirk".

// For str = "ultr53o?n", the output should be "nortlu".

// Input/Output // [output] a string
// [input] string str // A string consists of lowercase latin letters, digits and symbols.
// Test.assertEquals(reverseLetter("krishan"),"nahsirk")
// Test.assertEquals(reverseLetter("ultr53o?n"),"nortlu")
// Test.assertEquals(reverseLetter("ab23c"),"cba")

function reverseLetter(str) {
  //coding and coding..
    let str_array = str.split('')
    return str_array
  
}
str = "krishan"
console.log(reverseLetter(str))

//****************Simple Fun #176: Reverse Letter
// Task
// Given a string str, reverse it omitting all non-alphabetic characters.
// Example
// For str = "krishan", the output should be "nahsirk".

// For str = "ultr53o?n", the output should be "nortlu".

// Input/Output // [output] a string
// [input] string str // A string consists of lowercase latin letters, digits and symbols.
// Test.assertEquals(reverseLetter("krishan"),"nahsirk")
// Test.assertEquals(reverseLetter("ultr53o?n"),"nortlu")
// Test.assertEquals(reverseLetter("ab23c"),"cba")

//With /^[a-zA-Z]/ you only check the first character - 
//this you checK if all are letters/^[a-zA-Z]+$/.test(str);

// The following is the/a correct regex to strip non-alphanumeric chars from an input string:

// input.replace(/\W/g, '')
// Note that \W is the equivalent of [^0-9a-zA-Z_] - it includes the underscore character.
//To also remove underscores use e.g.: input.replace(/[^0-9a-z]/gi, '')

//MINE DID NOT PASS  IN CODEWARS HERE IT RETURNS A STRING   THERE A LIST WTF

function reverseLetter(str) {
  result = "";      
    for (let i = 0; i < str.length; i++) {
      if (str[i].match("^[a-zA-Z ]+$")) {
        result += str[i]
      }
  }
  //return result;
  let str_array= result.split('');
  str_array.reverse()
  let new_str = str_array.toString()
  return new_str
}
 

str = "ab23c"
console.log(reverseLetter(str))

//  Solution
function reverseLetter(str) {
let a = ''
for (let i = 0; i < str.length; i++) {
  if (str[i].match("^[a-zA-Z ]+$")) {
    a += str[i]
  }
}
return a.split('').reverse().join('').split(' ').join('')
}




// # **************************  Two Sum

// # Solution
// # Given an array of integers, return indices of the two numbers such that they add up to a specific target.

// # You may assume that each input would have exactly one solution, and you may not use the same element twice.

// # Example:

// # Given nums = [2, 7, 11, 15], target = 9,

// # Because nums[0] + nums[1] = 2 + 7 = 9,
// # return [0, 1].

// # Test.assert_equals(sorted(two_sum([1,2,3], 4)), [0,2])
// # Test.assert_equals(sorted(two_sum([1234,5678,9012], 14690)), [1,2])
// # Test.assert_equals(sorted(two_sum([2,2,3], 4)), [0,1])

// total += parseInt(num_str[i])
// num_str = number.toString();
  

// function two_sum(nums, target){
//   let results = [];

//   for(let i = 0; i < nums.length; i++){
//     for(let j = 1; j < nums.length; j++ ){
//         if (nums[1] + nums[j] == target){
//           results.push(i)
//           results.push(j)
//           return results
//         }
//       }
//   }
// }
// nums = [2,2,3]
// target = 4

// console.log(two_sum(nums,target))

//Count the Characters_7

// The goal of this kata is to write a function that takes two inputs: a string and a character. The function will count the number of times that character appears in the string. The count is case insensitive.

// For example:

// countChar("fizzbuzz","z") => 4
// countChar("Fancy fifth fly aloof","f") => 5
// The character can be any alphanumeric character.

function countChar(str1, char) {
  counter = 0
  for(let i = 0; i < str1.length; i++){
      if (str1[i].toLowerCase() == char.toLowerCase()){
        counter+=1
      }
  }
  return counter
}

str1 = "Fancy fifth fly aloof"
char = "f"
console.log(countChar(str1, char))

//*******floor */
find_floor = Math.floor(25.2)
console.log(find_floor) //=>25

find_floor2 = Math.floor(25/3)
console.log(find_floor2) //=>8

//finding the ceiling rounding up
find_ceiling = Math.ceil(25.5)
console.log(find_ceiling) //=> 26


remainder = 93 % 10
console.log(remainder) //=>3

// Find the stray number _1

//You are given an odd-length array of integers, in which all of them are the same, except for one single number.

// Complete the method which accepts such an array, and returns that single different number.

// The input array will always be valid! (odd-length >= 3)

// Examples
// [1, 1, 2] ==> 2
// [17, 17, 3, 17, 17, 17, 17] ==> 3
//

// function stray(numbers) {
//   strayNum = 0
//   for(let i = 1; i < numbers.length; i++){
//     if (numbers[i-1] == numbers[i]){
//       //we have a consec number
//     }else{
//       if (i == 1){
//         strayNum = numbers[i-1]
//         return stray  
//       }else{
//         strayNum = numbers[i]
//         return strayNum
//       }
//     }
//   } 
//  }
//  numbers = [8, 17, 17]
//  console.log(stray(numbers))

//Mr Martingale 7 

// You're in the casino, playing Roulette, going for the "1-18" bets only and desperate to beat the house and so you want to test how effective the Martingale strategy is.

// You will be given a starting cash balance and an array of binary digits to represent a win or a loss as you play: 0 for loss and 1 for win.

// You should create a function martingale to return the balance after playing all rounds.

// You start with a stake of 100 dollars(unit of cash). If you lose a round, you lose the stake placed on that round and double the stake for your next bet. When you win, you win 100% of the stake and revert back to staking 100 dollars on your next bet.

// Example

// martingale(1000, [1, 1, 0, 0, 1]) === 1300
// you win your 1st round: gain $100, balance = 1100
// win 2nd round: gain $100, balance = 1200
// lose 3rd round: lose $100 dollars, balance = 1100
// double stake for 4th round and lost: staked $200, lose $200, balance = 900
// double stake for 5th round and won: staked $400 won $400, balance = 1300

// NOTE: Your balance is allowed to go below 0 (debt) :(

//   function martingale(bank, outcomes)
//   { if (outcomes.length == 0) {
//       return bank
//   }else{
//     bet = 100;
//     bet_multi = 2
//     for(let i = 0; i < outcomes.length; i++){
//       if (outcomes[i] == 0 ){
//         bank = bank - bet;
//         bet = bet + bet;      
//       }else{
//         bank = bank + bet;
//         bet = 100;
//       }    
//     }
//     return bank 
//   }   
// }


// bank = 5100
// outcomes = [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0]
// console.log(martingale(bank, outcomes))


// # *************** CW Character with longest consecutive repetition -6
// # For a given string s find the character c (or C) with longest consecutive repetition and return:

// # # [input, expected],
// #     ["aaaabb", ('a', 4)],
// #     ["bbbaaabaaaa", ('a', 4)],
// #     ["cbdeuuu900", ('u', 3)],
// #     ["abbbbb", ('b', 5)],
// #     ["aabb", ('a', 2)],
// #     ["ba", ('b', 1)],
// #     ["", ('', 0)],


//Binary Search IN JAvascript


// function findTarget(nums,target){
//     for (let i = 1; i< nums.length; i++){
//         if (nums[i-1] == target){
//             return i-1
//         }
//     }
//     return -1
// }

// nums = [-1,0,3,5,9,12]
// target = -1
// console.log(findTarget(nums,target))

// function binarySearchHelper(array, target, left, right){

//     while(left <= right){
//         middle = Math.floor(left + right);
//         potential_match = array[middle];
//         if (target == potential_match){
//             return middle
//         }else if (target < potential_match){
//                 right = middle - 1
//         }else{
//             left = middle + 1
//         }
//     }
//     return -1
// }

// function binarySearch(array, target){
//     return binarySearchHelper( array, target, 0, array.length -1)
// }

// array = [-1,0,3,5,9,12]
// target = -1
// console.log(binarySearch(array,target))

function fizz_buzz(){
  for (let i = 1; i < 101 ; i++){
      if (i % 3 == 0 && i % 5 ==0){
          console.log(i + ' is a multiple of 3 and 5');
      } else if (i % 3 == 0) {
          console.log(i + ' is a multiple of 3') 
      }else if (i % 5 == 0){
          console.log(i + ' is a multiple of 5')
      }
      else{
          console.log(i)
      }        
  }
}

fizz_buzz()

//  palindrome#Question - can we have capital letters yes ?
// #          - can I assume there are no special characters or number in the string?

// #slicing is start, stop(exclusive), step 

let palindrome = (str1) =>{
  rev_str1 = str1.split("").reverse().join("");
  if (str1.toLowerCase() === rev_str1.toLowerCase()){       
      return true
  }else{        
      return false
  }
}

str1 = 'volvo'
console.log(palindrome(str1))


// returns list #Week2 day4*******#Find all the even numbers for a list and put them in a new list
// #Questions - the lists just have numbers, and all integers, and no zero

function evens(nums){
  let results = []
  for(let i =0; i < nums.length; i++){
      if (nums[i] % 2 ==0){
          results.push(nums[i])
      }
  }

  return results
}

nums = [6,45,77,3,88]
console.log(evens(nums))

// #**********Week3 Day1 # Remove Element
// # Given a list of numbers and a value as input to a function, remove all instances of that value "in-place" and return the new length of the list
// # Input: nums = [3,2,2,3] value = 3
// # Output: return a length == 2


// The second parameter of splice is the number of elements to remove. Note that splice modifies the array in place and returns a new array containing the elements that have been remove
function remove(nums, target){
  i = 0
  while (i < nums.length) {
      if (nums[i]== target){
          nums.splice(i,1);
      }else{
          i++;
      }
  }
  return nums.length
}

target = 8
nums = [3,7,8,5,8,2] //4
console.log(remove(nums,target))

// # #******************week3 day2 - Length of Last word
// # Create a function that given a string as a parameter of upper/lower case letters and empty space characters (“ “),
// # return the length of the last word. Meaning, the word that appears far most to the right if we loop through the words.

// # Example Input: “Hello World”
// # Example Output: 5
// # Example Input 2: “The brown loud cow plowed”group
// # Example Output 2: 6

// let groupOfNames= ['Terry', 'Ben', 'Ash', 'Brock','Misty']
// console.log(groupOfNames.slice(groupOfNames.length -1))

function lastWord(str1){
  words = str1.split(" ")  
  last_word = words.slice(words.length-1)
  return last_word.toString().length
}
s = "The brown loud cow plowed"
console.log(lastWord(s))


// find the lowest number in the list and return it. Can't use sort
// # Example Input: [50,30,4,2,11,0]
// # Example Output: 0
// # Example Input 2: [40,3,4,2]
// # Example Output 2: 2

function findSmallest(nums){
    //using the spread operator
    min_num = Math.min(...nums); 
    return min_num
}

function findSmallest(nums){
    //sorted_nums = nums.sort()
    nums.sort(function(a, b){return a - b});
    min_num = nums[0]
    return min_num
}
// # Given a string, find the first non-repeating character in it and return its index. 
// # If it doesn't exist, return -1.
// # Examples:
// # Input - s = "leetcode"
// # Output - return 0
// # Input - s = "loveleetcode"
// # Output - return 2
// #  'aaa' return  -1

function non_repeat(s){
  s_dict = {}
  for(let i = 0; i < s.length; i++){
      //if it is in object
      if(s_dict[s[i]]){
          s_dict[s[i]] = 2;
      }else{
          s_dict[s[i]] = 1
      }
  }
  for (let i = 0; i < s.length; i++){
      if (s_dict[s[i]]=== 1){
          return i
      }
  }
  return -1
}

s = "loveleetcode"
console.log(non_repeat(s))

function non_repeat(s){
  s_dict = {}
  for(let i = 0; i < s.length; i++){
      //if it is in object
      if(s_dict[s[i]]){
          s_dict[s[i]] = 2;
      }else{
          s_dict[s[i]] = 1
      }
  }
  for (let i = 0; i < s.length; i++){
      if (s_dict[s[i]]=== 1){
          return i
      }
  }
  return -1
}

s = "loveleetcode"
console.log(non_repeat(s))

// # Sample Problem for Two Pointers: Pair with the target sum
// # Problem Statement: Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
// # Write a function to return the indices of the two numbers (i.e., the pair) such that they add up to the given target.
// # Example: # Example: Input: [1, 2, 3, 4, 6], target = 6, Output: [1, 3] (The numbers at index 1 and 3 add up to 6: 2+4=6), Output: [1, 3] (The numbers at index 1 and 3 add up to 6: 2+4=6)

function findSum(arr, target){
  let left = 0
  let right = arr.length-1
  results = []

  while( left < right){
      if(arr[left] + arr[right] > target){
          right = right - 1
      }else if(arr[left] + arr[right] < target){
          left++
      }else{
          results.push(left)
          results.push(right)
          return results
      }
  }
}

arr = [1, 2, 3, 4, 6]
target = 6
console.log(findSum(arr, target))


