var robot=require("robotjs");
var i=4001
    robot.moveMouse(807,754);
    robot.mouseClick();
    robot.moveMouse(664,454);
while(i<=4500){
    robot.mouseClick();
    robot.typeString(`tesseract ${i}.jpeg ${i}.txt`);
    robot.keyTap("enter");
    i++;
}