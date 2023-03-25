let age = 0
msg=" "
function add_numbers(num1,num2)
{
    return num1 + num2
}
console.log("javascript console testing")

document.getElementById("confirm_btn").click= check_age;{
    age = document.getElementById("age").innerHTML.valueOf()
    if(age<= 18){
        msg="You are not allowed"
        document.getElementById("get_in").innerHTML=msg
    }else{
        msg="Welcome to the club"
        document.getElementById("get_in").innerHTML=msg
    }    
}
