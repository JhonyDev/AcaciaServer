const inCurrentPass = document.getElementById("in_current_pass");
const inNewPass = document.getElementById("in_new_pass");
const inConfirmPass = document.getElementById("in_confirm_pass");

const btnConfirm = document.getElementById("btn_confirm");


let strCurrentPass;
let strNewPass;
let strConfirmPass;

let prevPassword;

function isCurrentPassValid(strCurrentPassword) {
    return prevPassword === strCurrentPassword;
}

function isNewPassValid(strNewPass, strConfirmPass) {
    return strNewPass === strConfirmPass;
}


console.log("in pass js");

$.ajax({
    type: 'GET',
    url: 'js/',
    success: function (response) {
        console.log(response.data);
        prevPassword = response.data.password;
    },
});


btnConfirm.addEventListener("click", function () {
    console.log("btn clicked");
    strCurrentPass = inCurrentPass.value;
    if (isCurrentPassValid(strConfirmPass)) {
        console.log("Password in valid");
        return;
    }

    strNewPass = inNewPass.value;
    strConfirmPass = inCurrentPass.value;

    if (isNewPassValid(strNewPass, strConfirmPass)) {
        console.log("Passwords don't match");
        return;
    }

    window.location.href = 'new_pass/' + strNewPass;

});


