// var pivotIndex = function (nums) {
//   let l = 0;
//   let r = nums[nums.length - 1];

//   let result = -1;

//   for (let i = 0; i < nums.length - 1; i++) {
//     let backwardCount = nums.length - 2;

//     if (i === 0) {
//       l = 0;
//     } else {
//       l += nums[i - 1];
//     }

//     while (backwardCount > i) {
//       r += nums[backwardCount];
//       backwardCount--;
//     }
//     if (l === r) {
//       return i;
//     }
//     r = nums[nums.length - 1];
//   }
//   return result;
// };

function pivotIndex(nums) {
  let leftSum = 0;
  let rightSum = nums.reduce((acc, num) => acc + num, 0);

  for (let i = 0; i < nums.length; i++) {
    rightSum -= nums[i];
    if (leftSum === rightSum) {
      return i;
    }
    leftSum += nums[i];
  }

  return -1;
}

console.log(pivotIndex([1, 7, 3, 6, 5, 6]));
