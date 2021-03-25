// kata: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

const makeDictionary = (dict, letter) => ({
  ...dict,
  [letter]: letter in dict ? dict[letter] + 1 : 1,
});

const compose = (...functions) => args =>
  functions.reduceRight((arg, fn) => fn(arg), args);

const duplicateCount = compose(
  xs => xs.reduce((acc, x) => (x > 1 ? acc + 1 : acc), 0),
  xs => Object.values(xs),
  xs => xs.reduce(makeDictionary, {}),
  x => x.split(''),
  x => x.toLowerCase()
);
