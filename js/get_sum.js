// kata: https://www.codewars.com/kata/55f2b110f61eb01779000053/
const compose = (...functions) => args =>
  functions.reduceRight((arg, fn) => fn(arg), args);

const fun = compose(
  xs => xs.reduce((x, y) => x + y),
  ([xs, fn]) => xs.map(fn),
  ([min, length]) => [Array.from({ length }), (x, y) => min + y],
  ([min, max]) => [min, -min + max + 1],
  ([x, y]) => [Math.min(x, y), Math.max(x, y)]
);

const GetSum = (x, y) => fun([x, y]);
