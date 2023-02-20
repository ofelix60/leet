var runningSum = function (nums) {
  let result = [];

  for (let i = 0; i < nums.length; i++) {
    let temp = 0;
    for (let j = i; j >= 0; j--) {
      temp += nums[j];
    }
    result.push(temp);
  }
  return result;
};

runningSum([3, 1, 2, 10, 1]);
