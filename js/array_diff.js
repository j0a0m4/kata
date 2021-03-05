// kata: https://www.codewars.com/kata/523f5d21c841566fde000009
function array_diff(a, b) {
  return a.filter(value => !b.includes(value));
}
