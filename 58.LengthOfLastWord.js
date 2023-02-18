var lengthOfLastWord = function (s) {
  s = s.split(' ');
  let result = s.filter((el) => el !== '');
  return result[result.length - 1].length;
};
console.log(lengthOfLastWord('   fly me   to   the moon  '));
console.log(lengthOfLastWord('Hello World'));
console.log(lengthOfLastWord('luffy is still joyboy'));
