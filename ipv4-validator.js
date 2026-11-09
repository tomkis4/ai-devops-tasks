
function isValidIPv4(ip) {
    const regex = /^(?:(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(?:25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$/;
  
    return regex.test(ip);
  }
  
  module.exports = isValidIPv4;
  
  // Przykłady
  console.log(isValidIPv4("192.168.1.1")); // true
  console.log(isValidIPv4("256.1.1.1"));   // false
  console.log(isValidIPv4("127.0.0.1"));   // true
  