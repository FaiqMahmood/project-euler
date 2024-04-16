function generateFibonacci(n) {
  let fibSequence = [1, 2];
  let a = 1;
  let b = 2;
  while (true) {
    let c = a + b;
    if (c > n) {
      break;
    }
    fibSequence.push(c);
    a = b;
    b = c;
  }
  return fibSequence;
}

function fiboEvenSum(n) {
  let fibSequence = generateFibonacci(n);
  let evenSum = 0;
  for (let num of fibSequence) {
    if (num % 2 === 0) {
      evenSum += num;
    }
  }
  console.log("Fibonacci sequence:", fibSequence);
  console.log("Sum of even numbers:", evenSum);
}

fiboEvenSum(8);
fiboEvenSum(10);
fiboEvenSum(34);
fiboEvenSum(60);
