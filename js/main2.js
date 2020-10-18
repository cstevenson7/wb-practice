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





/*

        ALGO EXPERT QUESTIONS

**/ 

//Fibonachi
//************RECURSIVE 
// function getNthFib(n) {
//     if (n===2){
//         return 1;
//     }else if (n===1){
//         return 0
//     }else{
//         return getNthFib(n-1) + getNthFib(n-2)
//     }  
// }
// console.log('working??')
// console.log(getNthFib(6))

//***********Loop */
function getNthFib(n){
   
  if (n===2){
      return 1;
  }else if (n===1){
      return 0
  }else{
  fib_series = [0,1]
      if (n > 1){
          for(let i =2; i < n; i++){
              next_num = fib_series[i-1] + fib_series[i-2]
              fib_series.push(next_num)
          }
      return parseInt(fib_series.slice(n-1))
      }
  }
}


//my solution
//O(n^2) aka quardatic time | O(1) aka constant space
// function twoNumberSum(array, targetSum) {
   
//     for(let i = 0; i < array.length; i++){
//         for (let j = 0; j < array.length; j++){
//             if (i != j){
//                 if (array[i] + array[j] == targetSum){
//                     // results.push(array[i])
//                     // results.push(array[j])
//                     return [array[i],array[j]]               
//                 }
//             }
//         }
//     }
//     return [] 
//   }
  

// array =   [3, 5, -4, 8, 11, 1, -1, 6]
// target = 10
// console.log(twoNumberSum(array,target))

//AlgoExpert(AE) solution
//O(nlog(n)) aka linear Logarithmic time | O(1) aka constant space

function twoNumberSum(array, targetSum){
  array.sort((a,b) => a-b);
  let left = 0;
  let right = array.length-1;
  while (left < right){
      //start at the two ends and work your way in
      const currentSum = array[left] + array[right];
      if(currentSum === targetSum){
          return[array[left], array[right]];
      }else if(currentSum < targetSum){
          left++ ;    
      }else if(currentSum > targetSum){
          right--;
      }
  }
  return [];
}

array =   [ -5,3, 8, 1,11, -1] 
target = 7
console.log(twoNumberSum(array,target))

//******************************************** */
function isValidSubsequence(array, sequence) {
  // traverseing through both arrays at the same time with pointers keeping track of the indexes
  let arrIdx = 0;
  let seqIdx = 0;
  //traversing bothe arrays at the same time
  while (arrIdx < array.length && seqIdx < sequence.length){
      //if we find a match move to the next number in the sequence
      if (array[arrIdx] === sequence[seqIdx]){
          seqIdx++;
      }
      //look at the next number in the array
      arrIdx++;
  }
  // if the seqIdx == the length of the sequence that means we have
  //found all the number of the seqence in that array. Note: thatindex number is increased after we find a match so the index number wiil match the length of the sequence 
  return seqIdx == sequence.length;
} 

array =  [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 2,10]
console.log(isValidSubsequence(array,sequence))

//Need to check this in solution can't get it to pass
//Binary Search Tree aka BST 
function findClosestValueInBst(tree, target) {
  return findClosestValueInBstHelper(tree,target,tree.value)
}
function findClosestValueInBstHelper(tree, target, closest){
  let currentNode = tree;
  while (currentNode !== null){
      if (Math.abs(target-closest) > Math.abs(target - currentNode.value)){
          closest = currentNode.value;
      }
      if(target < currentNode.value){
          currentNode = currentNode.left;
      }else if (target > currentNode.value){
          currentNode = currentNode.right;
      }else{
          break;
      }
      
  }
  return closest;
}

//*****************InsertionSort */

//best O(n) time  | O(1)space
//time is O(n^2) aka O n squared quadratic when n is the length of our array, could be many comparissons and swaps )
// because the array is swapped inplace the space complexity is constant
//Avg  O(n^2)  | O(1)
//worst same as avg

function insertionSort(array) {
  for(let i = 1; i < array.length; i++){
      let j = i;
      while (j > 0 && array[j-1] >array[j]){
          swap(j-1,j,array)
          j--;
      }
  }
  return array
}

function swap(i,j,array){
  let temp = array[j];
  array[j] = array[i]
  array[i] = temp
}

array = [8, 5, 2, 9, 5, 6, 3]
console.log(insertionSort(array))

//*********Bubble sort
// Worst Case: O(n^2) Time - O(1) Space
// Best case time would be linear O(n) if the array is sorted- still have to go through the array  once to check.
//O(n^2) time depending on n the length of the array quadratiec -  looping through the array MULTIPLE times (not just once)  until the array is sorted
//O(1) space is constant doing swap in place - didn't allocate additional memmory

function swap(i,j,array){
  let temp = array[j];
  array[j] = array[i]
  array[i] = temp
}

function bubbleSort(array){
  let isSorted = false
  //so while the array is not sorted
  while(!isSorted){
      //set the isSorted flag true in case it is sorted
      isSorted = true
      for (let i = 0; i < array.length; i++){
          if (array[i] > array[i+1]){
              swap(i, i+1, array)
              isSorted = false
          }
      } 
  }
  return array
}

array = [8, 5, 2, 9, 5, 6, 3]
console.log(bubbleSort(array))

//*************************************#Product Sum
// # time complexity  - quadratic O(n^2) = with n the length of the array
// # space compexity - constant O(n) - only 1 extra variable 

function productSum(array, depth = 1){
  let total_sum = 0;  
  for (const element of array){
      if (Array.isArray(element)){         
          total_sum += productSum(element, depth +1);
      }else{
          total_sum += element;
      }
  }
  return total_sum  * depth;
}

array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
console.log(productSum(array))

//BST Branch Sum 

class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function branchSums(root) {
    const sums_list = []
    calculateBranch(root, 0, sums_list)
    return sums_list
}

function calculateBranch(node, branch_total, sums_list){
    const new_total = branch_total + node.value
    if (!node){
        return        
    }
    if(!node.left && !node.right){
        sums_list.push(new_total)
        return
    }
    calculateBranch(node.left, new_total, sums_list)
    calculateBranch(node.right,new_total,sums_list )
}

//Is Palindrome question
// #Best time and space
// O(n) time Go through string once but O(1) Constatn spave , only
// using the pointers, nothing depends on size of the string for space complexity
function isPalindrome(string){
  let left_idx = 0;
  let right_idx = string.length - 1;
  while (left_idx < right_idx){
      if (string[left_idx] !== string[right_idx]){
              return false
      }else{
          left_idx ++;
          right_idx--;
      }
  }
  return true
}

// #*************** Caesar cipher encryption
// # - non empty lowercase string and a non-neg integer (k) , returns new string by shifting " wrapping " alphabet by k letters

// # input - non-empty lowercase string IF NOT JUST LOWERCase do
//  #       -  a uppercase list as well
// # output - string lowercase - nonempty
// # edgecase - really large k numbers, use the modulo to get the reamonder
// # assumptions 

// # O(n) linear time = iterating through the input string  and O(1) constant space even if you use the alpa array the arrya is only 26 letters long Constant,  if the alphabet aray was "n" letters then it would not be constant
// # tests your use of the modulo operator

// # We can know that this works for loop-arounds by observing the following behavior:
//    1%26 = 1
// # 25%26=(0∗26+25)%26=25
// # 26%26=(1∗26+0)%26=0
// # 27%26=(1∗26+1)%26=1
// # 28%26=(1∗26+2)%26=2
// # and so on...

function caesarCipherEncryptor(string, key) {
  const alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 const new_letters = [];
 for (const letter of string){
      new_idx = (alpha.indexOf(letter) + key) % alpha.length
      new_letters.push(alpha[new_idx])
 }
 return new_letters.join('');
}


string = "xyz"
key = 1
console.log(caesarCipherEncryptor(string, key))





// # ThreeNumberSum
// # targetSum = find all triplets in the array that add up to the target sum
// # numbers in acscending order and triplets in ascending order
// # input = list and integer
// # output = list of sub-arrays
// # edgecase - if now numbers addup to target the return empty array
// # assumptions - can assume non empty array of distict integers and an
// #              integer representing the sum

// #0(n^2) quadratic time  where n is the length of the array, need to iterate thur the for loop a and then we have to iterate thru again in the while loop.  0(n) linear - ome space usage beause if the sort and the storing of the triplets 


//***********NOT WORKING FOR Some REASON??
function threeNumberSum(array, targetSum) {
  array.sort((a,b) => a - b);
  const results = [];
  for (let i = 0; i < array.length - 2; i++ ){
      let left = i+1;
      let right = array.length -1;
      while (left < right ){
        let current_sum = array[i] + array[left] + array[right];
          if (current_sum ===  targetSum){
              results.push([array[i], array[left] , array[right]]);
              left ++;
              right --;
          }else if (current_sum < targetSum){ 
              left++;
          }else if (current_sum > targetSum){
            right--;
          }
      }
  }
  return results;
}

array = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
console.log(threeNumberSum(array,target))

// # *********************smallest difference
// # input -  2 arrays - can be unequal length
// # output - 1 array with 2 numbers number for first array in front
// # edge case - 
// # assumptions - 2 non-empty interger arrays only one pair will be correct answer

// #O(n log(n) + m log(m)) when n = len of array1 and m = len of array2 - the arrays can be unequal in length - need to sort both arrays first and looping thru the first array  -linear quadratic time complexity 
// #Space = O(1) - sorting arrays in place and the varaible we are are storing are constant space and array of the results (pair) and a diff sum -  nothing we are storing depends on the length of the arrays

// # ask if you can sort the arrays in palce, if not you need to do do this:
// #  a1_sorted = sorted(arrayOne)
// #  a2_sorted = sorted(arayTwo) - this would take more space

function smallestDifference(arrayOne, arrayTwo){
  arrayOne.sort((a,b) => a - b);
  arrayTwo.sort((a,b) => a - b);
  let a1_left = 0;
  let a2_left = 0;
  let results = [];
  let smallest_diff = Infinity;
  let temp_diff = Infinity;

  while (a1_left < arrayOne.length && a2_left < arrayTwo.length){
      let num1 = arrayOne[a1_left];
      let num2 = arrayTwo[a2_left];
      if (num1 < num2){
          temp_diff = num2 - num1
          a1_left++;
      }else if (num2 < num1){
          temp_diff = num1 - num2
          a2_left++;
      }else{
          return [num1, num2]
      }

      if (temp_diff < smallest_diff){
          smallest_diff = temp_diff
          results= [num1, num2]
      }

  }
  return results
}

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
console.log(smallestDifference(arrayOne, arrayTwo))

//stack LAST IN FIRST OUT -  LIFO
function nodeDepths(root){
  let depth_sum = 0;
  //need to store all of the nodes and their depths,
  //could use array, but this is easier to read 
  //the first entry is the root and the root node depth = 0
  const stack = [{node:root, depth:0}];
  //looping through the BT getting the node value and the depth
  while (stack.length > 0){ 
      //pop a node off the stack (LIFO)
      //start at the top of the stack
      const {node,depth}= stack.pop();
      //check if the node value is null/none, if it is that means
      // the tree is empty and we are dine
      if (node ===null) {
          continue;
      }       
      depth_sum += depth;
      //now append the children nodes on both sides
      stack.push({node: node.left, depth:depth + 1});
      stack.push({node: node.right, depth:depth + 1});
      
  }
  return depth_sum; 
}

// #Depth first searchNode class with name and an array of optional children nodes.Implement the dpethfirstSearch method on the node class, which takes in an empty array , traverses the tree using the depth firs search (navigating from left to right)
// #stores all of the nodes names in an input array and returns it

// # graphs a collection of nodes that may or maynot be connected. the nodes are called vertices and the branches(connections) are called edges
// #  Explore first left branch, as far down (deep as we can ), then go to the next branch to the right.

//  #111 vertices in this graph and 10 edges
// #  time complexity = O(v + e) - add every nodes name(v) we iterate throught the for loop for as may childresas the tree has so that is how many edges there are as well.
// #Space- complexity is O(v) - length of the return array
class Node {
  constructor(name) {
    this.name = name;
    this.children = [];
  }

  addChild(name) {
    this.children.push(new Node(name));
    return this;
  }

  depthFirstSearch(array) {
    array.append(this.name)
    for(let child of children){
        child.depthFirstSearch(array)
    }
    return array
  }
}


//************Find three largest numbers
//Find the three largest numbers in an unsorted array
// Input - integer array of at least three values
// output - array of three sorted integers
// edgecase - non
// assumptions - can't sort array and array has at least three integers

function findThreeLargest(array){
  let largest = [null, null, null];
  for (const num of array){
      updateLargest(largest, num)
  }
  return largest
}

function updateLargest(largest,num){
  if (largest[2]===null || num > largest[2]){
      moveNums(largest,num,2)
  } else if (largest[1] === null || num > largest[1]){
      moveNums(largest,num,1)
  } else if (largest[0] === null || num > largest[0]){
      moveNums(largest, num, 0)
  }
}

function moveNums(array, num, idx){
  for(let i =0; i <= idx; i++){
      if (i === idx){
          array[i] = num
      }else{
          array[i] = array[i + 1]        
      }
  }
}

array = [10,5,9,10,12]
console.log(findThreeLargest(array))

// #Std practice is to define a helper function

// # input - sorted integer array and target integer
// # output - return the index of the target, or -1 if not found
// # edgcases -
// # assumptions - the array will not be empty?

function binarySearch(array, target){
  return binarySearchHelper(array, target, 0, array.length - 1)
}

function binarySearchHelper(array, target, left, right){
  while (left <= right){
      let middle = Math.floor((left + right)/2)
      let potential = array[middle]

      if (target === potential){
          return middle
      }else if (target < potential) {
          right = middle - 1
      }else{
          //target > potential
          left = middle + 1
      }
  }
  return -1
}

array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
console.log(binarySearch(array,target))

// #*************************Selection sort
// #
// # interate through list find the smallest number 
// # and swap it with the current index pointer
// # input - unsorted integer array
// # output - sorted array
// # edgecase
// # assumptions

// # time complexity = O(n^2)quardratic - where n is the
// # length of the array need to traverse array multiple times
// # to find the smallest number, the longer the array the longer it would take

// # space complexity = O(1) constant - the swaps are in place and the solution
// #  does not need additional storage or space is not dependent the length of the aray

function selectionSort(array){
  //current_idx is our sorted pointer
  let current_idx = 0;
  while (current_idx < array.length -1){
       let smallest_idx = current_idx;
       //for loop finds the next smallest number
       for (let i = current_idx + 1; i < array.length; i++){
          if(array[smallest_idx] > array[i]){
               smallest_idx = i;
          }      
      }
      swap( current_idx, smallest_idx, array)
      current_idx ++;
  }
  return array
}

function swap(i, j, array){
  let temp = array[i];
  array[i] = array[j];
  array[j] = temp
}

array = [8, 5, 2, 9, 5, 6, 3]
console.log(selectionSort(array))