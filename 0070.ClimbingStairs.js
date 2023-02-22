var climbStairs = function (n) {
  let b = 1;
  let a = b;
  while (n--) {
    a = (b += a) - a;
  }
  return a;
};

console.log(climbStairs(3));
