function checkPhoneNumber(number) {
  let regex =
    /^((\+)?[1-9]{1,2})?([-\s\.])?((\(\d{1,4}\))|\d{1,4})(([-\s\.])?[0-9]{1,12}){1,2}$/;
  if (regex.test(number)) return "is a valid number.";
  return "is not a valid number.";
}

const numbers = [
  "2124567890",
  "212-456-7890",
  "(212)-456-7890",
  "212.456.7890",
  "212 456 7890",
  "+12124567890",
  "+12124567890",
  "+1 212.456.7890",
  "+212-456-7890",
  "1-212-456-7890",
];

numbers.map(function (number) {
  const result = checkPhoneNumber(number);
  console.log(number, result);
});
