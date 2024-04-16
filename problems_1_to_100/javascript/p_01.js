function multiplesOf3Or5(number) {
  /*
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below the provided parameter value number
    */
  let sumOfMultiples = 0;

  for (let num = 1; num < number; num++) {
    if (num % 3 === 0 || num % 5 === 0) {
      sumOfMultiples += num;
    }
  }
  return sumOfMultiples;
}

console.log(multiplesOf3Or5(9)); // Output: 23
console.log(multiplesOf3Or5(49)); // Output: 543
console.log(multiplesOf3Or5(1000)); // Output: 233168
console.log(multiplesOf3Or5(8456)); // Output: 16687353
console.log(multiplesOf3Or5(19564)); // Output: 89301183
