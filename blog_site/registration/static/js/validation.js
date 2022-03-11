function validate(){
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const phone = document.getElementById("phone").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const c_password = document.getElementById("c_password").value;
    var submition = 1;


    // if((name == "") && (age == "") && (phone == "") && (email == "") && (password == "") && (c_password == "")){
    //     document.getElementById("error_form").innerHTML = "Enter your details."
    //     return false
    //     submition = 0;
    // }
    // else{
    //     document.getElementById("error_form").innerHTML = "";
    //     submition = 1;
    // }

    // Start Name validation
    if(name == ""){
        document.getElementById("error_name").innerHTML = "Enter youre name.";
        // return false
        submition = 0;
    }

    else if(!isNaN(name) || (!isNaN(name[0]))){
        document.getElementById("error_name").innerHTML = "First latter must be alphabet."
        // return false
        submition = 0;
    }

    else{
        document.getElementById("error_name").innerHTML = "";
        submition = 1;
    }
    // End Name validation

    // Start Age validation
    if(age == ""){
        document.getElementById("error_age").innerHTML = "Enter youre age.";
        // return false
        submition = 0;
    }

    else if(isNaN(age)){
        document.getElementById("error_age").innerHTML = "Alphabets are not allowed.";
        // return false
        submition = 0;
    }

    else if(age<13){
        document.getElementById("error_age").innerHTML = "You're not alligible. Age must be above 13.";
        // return false
        submition = 0;
    }

    else{
        document.getElementById("error_age").innerHTML = "";
        submition = 1;
    }
    // End Age validation

    // Start Phone validation
    if(phone == ""){
        document.getElementById("error_phone").innerHTML = "Enter your phone number.";
        // return false
        submition = 0;
    }

    else if(isNaN(phone)){
        document.getElementById("error_phone").innerHTML = "Enter a valid phone number.";
        // return false
        submition = 0;
    }

    else if(phone.length != 10){
        document.getElementById("error_phone").innerHTML = "Phone number's lenght must be 10.";
        // return false
        submition = 0;
    }

    else{
        document.getElementById("error_phone").innerHTML = "";
        submition = 1;
    }
    // End Phone validation

    // Start Email validation
    if(email == ""){
        document.getElementById("error_email").innerHTML = "Enter your Mail ID";
        // return false
        submition = 0;
    }

    else if(email[0] == "@"){
        document.getElementById("error_email").innerHTML = "Enter a valid Mail Id.";
        // return false
        submition = 0;
    }

    else if((email[-4] != ".") || (email[-3] != ".")){
        document.getElementById("error_email").innerHTML = "Enter a valid Mail Id.";
        // return false
        submition = 0;
    }

    else if(!isNaN(email)){
        document.getElementById("error_email").innerHTML = "Alphabests are not allowed";
        // return false
        submition = 0;
    }

    else if(!email.includes("@") || (!email.includes("."))){
        document.getElementById("error_email").innerHTML = "Enter a valid Mail ID."
        // return false
        submition = 0;
    }

    else{
        document.getElementById("error_email").innerHTML = "";
        submition = 1;
    }
    // End Email validation

    // Start Password validation
    if(password == ""){
        document.getElementById("error_password").innerHTML = "Enter your password.";
        // return false
        submition = 0;
    }

    else if((password.length <= 6) || (password.length >= 13)){
        document.getElementById("error_password").innerHTML = "Password must be in 6 to 13 charactors.";
        // return false
        submition = 0;
    }

    else{
        document.getElementById("error_password").innerHTML = "";
        submition = 1;
    }
    // End Password validation

    // Start Confirm Password validation
    if(c_password == ""){
        document.getElementById("error_c_password").innerHTML = "Confirm your password."
        // return false
        submition = 0;
    }

    else if(password != c_password){
        document.getElementById("error_c_password").innerHTML = "Your password doesn't match."
        submition = 0;
    }

    else{
        document.getElementById("error_c_password").innerHTML = "";
        submition = 1;
    }

    // if (name_ == true, age == true, phone == true, email == true, password == true, c_password == true) {
    //     submition = 1;
    // }else{
    //     submition = 0;
    // }

    // Submition
    if(submition===1){
        return true;
    }
    else{
        return false;
    }
}

// return validate()

// document.getElementById("submit").innerHTML = "Submited";


    // if(age<=0){
    //     document.getElementById("error_age").innerHTML = "Enter valid age."
    //     return false
    // }

    // if((name == "") && (age == "") && (phone == "") && (email == "") && (password == "")){
    //     document.getElementById("error_form") = innerHeight = `Enter details.`
    //     return false
    // }