const btn = document.getElementById('btn_login');
const iUserName = document.getElementById('user_name');
const iPassword = document.getElementById('pass');

let strPassword;
let strUsername;

let givenUsername;
let givenPassword;

const success = 1;
const failed = 0;

console.log("this is new change");

$.ajax({
    type: 'GET',
    url: 'posts/2',
    success: function (response) {
        const data = response.data;
        givenPassword = data.password;
        givenUsername = data.user_name;

    },
    error: function (response) {
//        console.log(error)
    }
})


console.log("newwww")

btn.addEventListener("click", function () {
    strPassword = iPassword.value;
    strUsername = iUserName.value;
    let result;
    if (strUsername === givenUsername && strPassword === givenPassword) {
        console.log("Verification successful");
        result = success
    } else {
//        console.log("Verification failed")
        swal("Opps!", "Invalid Username or Password!", "error");
        result = failed
    }

    if (result === success) {
        $.ajax({
            type: 'GET',
            url: 'posts/' + result,
            success: function (response) {
                window.location.href = '/admin_panel/dashboard';
            },
        })
    }

});

