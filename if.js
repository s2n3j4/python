let b = (input("What is your age?"));
b = Number.parseInt(b)
console.log(typeof b)
if (b<=8){
  alert("below 8 - You cannot participate")
}
else if(b>8 && b<=18){
  alert("above 8 and below 18 - You can participate in one game")
}
else if(b>18 && b<=90){
  alert("Above 18 and below 90 you can participate in all games")
}
console.log(b)