var robot=require("robotjs");
var fs=require("fs")
write()
function write(){
    robot.moveMouse(809,744);
    robot.mouseClick();
    robot.moveMouse(40,95);
    var str=fs.readFileSync("./4002.txt");
    robot.typeString(str);
}