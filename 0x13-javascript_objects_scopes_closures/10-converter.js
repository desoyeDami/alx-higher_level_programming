exports.converter = function (base) {
  function convertToBase (number) {
    if (number < base) {
      return '' + number;
    }
    return convertToBase(Math.floor(number / base)) + (number % base);
  }

  return convertToBase;
};
