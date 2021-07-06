

function dashboard() {
    return '<div class="container mt-4">' +
        '             <div class="row">' +
        '' +
        '                    <div class="col-md-3">' +
        '                        <div class="card-counter info">' +
        '                            <i class="fa fa-users"></i>' +
        '                            <span class="count-numbers">35</span>' +
        '                            <span class="count-name">Total User</span>' +
        '                        </div>' +
        '                    </div>' +
        '' +
        '                    <div class="col-md-3">' +
        '                        <div class="card-counter primary">' +
        '                            <i class="fa fa-user"></i>' +
        '                            <span class="count-numbers">12</span>' +
        '                            <span class="count-name">Paid User</span>' +
        '                        </div>' +
        '                    </div>' +
        '' +
        '                    <div class="col-md-3">' +
        '                        <div class="card-counter danger">' +
        '                            <i class="fa fa-user"></i>' +
        '                            <span class="count-numbers">599</span>' +
        '                            <span class="count-name">Un-Paid User</span>' +
        '                        </div>' +
        '                    </div>' +
        '' +
        '                    <div class="col-md-3">' +
        '                        <div class="card-counter success">' +
        '                            <i class="fa fa-database"></i>' +
        '                            <span class="count-numbers">6875</span>' +
        '                            <span class="count-name">Verified Account</span>' +
        '                        </div>' +
        '                    </div>' +
        '' +
        '                    <div class="col-md-3">' +
        '                        <div class="card-counter success">' +
        '                            <i class="fa fa-database"></i>' +
        '                            <span class="count-numbers">6875</span>' +
        '                            <span class="count-name">Un-Verified Account</span>' +
        '                        </div>' +
        '                    </div>' +
        '' +
        '                    <div class="col-md-3">' +
        '                        <div class="card-counter success">' +
        '                            <i class="fa fa-database"></i>' +
        '                            <span class="count-numbers">6875</span>' +
        '                            <span class="count-name">Reported Account</span>' +
        '                        </div>' +
        '                    </div>' +
        '' +
        '' +
        '                </div>' +
        '            </div>';
}

function paidUser(pic, mail, name) {
    return '<table class="table" style="width:100%;">' +
        '<tbody>' +
        '<tr>' +
        '<td style="width:15%;">' +
        '<div class="icon-circle bg-primary">' +
        '<img class="img-profile rounded-circle" src="' + pic + '" height="45px" width="45px">' +
        '</div>' +
        '</td>' +
        '<td style="width:85%;">' +
        '<div>' +
        '<div class="small text-gray-500">' + name + '</div>' + '' +
        '<span class="font-weight-bold">' + mail + '</span>' +
        '</div>' +
        ' </td>' +
        '  </tr>' +
        ' </tbody>' +
        ' </table>';
}

function unpaidUser(pic, mail, name) {
    return '<table class="table" style="width:100%;">' +
        '<tbody>' +
        '<tr>' +
        '<td style="width:15%;">' +
        '<div class="icon-circle bg-primary">' +
        '<img class="img-profile rounded-circle" src="' + pic + '" height="45px" width="45px">' +
        '</div>' +
        '</td>' +
        '<td style="width:85%;">' +
        '<div>' +
        '<div class="small text-gray-500">' + name + '</div>' + '' +
        '<span class="font-weight-bold">' + mail + '</span>' +
        '</div>' +
        ' </td>' +
        '  </tr>' +
        ' </tbody>' +
        ' </table>';
}

function verifys(pic, mail, name) {
    return '<table class="table" style="width:100%;">' +
        '<tbody>' +
        '<tr>' +
        '<td style="width:15%;">' +
        '<div class="icon-circle bg-primary">' +
        '<img class="img-profile rounded-circle" src="' + pic + '" height="45px" width="45px">' +
        '</div>' +
        '</td>' +
        '<td style="width:85%;">' +
        '<div>' +
        '<div class="small text-gray-500">' + name + '</div>' + '' +
        '<span class="font-weight-bold">' + mail + '</span>' +
        '</div>' +
        ' </td>' +
        '  </tr>' +
        ' </tbody>' +
        ' </table>';
}


function Un_verified(pic, mail, name) {
    return '<table class="table" style="width:100%;">' +
        '<tbody>' +
        '<tr>' +
        '<td style="width:15%;">' +
        '<div class="icon-circle bg-primary">' +
        '<img class="img-profile rounded-circle" src="' + pic + '" height="45px" width="45px">' +
        '</div>' +
        '</td>' +
        '<td style="width:85%;">' +
        '<div>' +
        '<div class="small text-gray-500">' + name + '</div>' + '' +
        '<span class="font-weight-bold">' + mail + '</span>' +
        '</div>' +
        ' </td>' +
        '  </tr>' +
        ' </tbody>' +
        ' </table>';
}



function reportAccount(pic, mail, name) {
    return '<table class="table" style="width:100%;">' +
        '<tbody>' +
        '<tr>' +
        '<td style="width:15%;">' +
        '<div class="icon-circle bg-primary">' +
        '<img class="img-profile rounded-circle" src="' + pic + '" height="45px" width="45px">' +
        '</div>' +
        '</td>' +
        '<td style="width:47%;">' +
        '<div>' +
        '<div class="small text-gray-500">' + name + '</div>' + '' +
        '<span class="font-weight-bold">' + mail + '</span>' +
        '</div>' +
        ' </td>' +
        '<td style="width:47%;>"' +
        '<div>' +
        ' <a href="button_click/' + mail + '" type="button" class="btn btn-danger" >Remove</a>' +
        ' </div>' +
        ' </td>' +
        '  </tr>' +
        ' </tbody>' +
        ' </table>';
}


const liDash_Board = document.getElementById('Dashboard');
const liTotalUsers = document.getElementById('total_users');
const liUnpaidUser = document.getElementById('unpaid_user');
const liVerify = document.getElementById('verified_accounts');
const liUnVerify = document.getElementById('unverified_accounts');
const liReportedAccounts = document.getElementById('reported_accounts');
const title = document.getElementById('title_report');
const userCount = document.getElementById('users_count');

let dash_board;
let reportedAccounts;
let paidUsers;
let unpaidUsers;
let verifies;
let un_verified;


title.innerHTML = "Dashboard";
$("#dash").empty();
$("#dash").append(
    dashboard());

$.ajax({
    type: 'GET',
    url: 'js/5',
    success: function (response) {
        const data = response.data;
        console.log(response);

        reportedAccounts = response.report;
        paidUsers = response.paid_users;
//        unpaidUsers = response.unpaid_users;
//        verifies = response.verified_users;
//        unverified = response.unverified_users;

        console.log('updated');
        const authStatus = data.status;
        if (authStatus !== 1)
            window.location.href = '/admin_panel';

        console.log(paidUsers);

        userCount.innerHTML = response.total_users;


    },
});

liDash_Board.addEventListener("click", function () {
    console.log("Dash");

    title.innerHTML = "Dashboard";

    $("#dash").empty();
    $("#dash").append(
        dashboard());

    $("#paid_users").empty();
    $("#unpaid").empty();
    $("#verified").empty();
    $("#unverified").empty();
    $("#report_accounts").empty();
});


liTotalUsers.addEventListener("click", function () {
    console.log("total clicked  " + typeof (paidUsers));

    title.innerHTML = "Paid Users";

    $("#dash").empty();
    $("#unpaid").empty();
    $("#verified").empty();
    $("#unverified").empty();
    $("#report_accounts").empty();

    $("#paid_users").empty();
    paidUsers.forEach(a =>
        $("#paid_users").append(
            paidUser(a.user_image, a.user_email,
                a.user_name))
    );

});


liUnpaidUser.addEventListener("click", function () {
    console.log("unpaid");
    title.innerHTML = "Unpaid User";
    $("#unpaid").empty();
    $("#dash").empty();
    $("#paid_users").empty();
    $("#verified").empty();
    $("#unverified").empty();
    $("#report_accounts").empty();
    reportedAccounts.forEach(reportedAccount =>
        $("#unpaid").append(
            unpaidUser(unpaidUsers.user_image, unpaidUsers.user_email,
                unpaidUsers.user_name))
    );


});

liVerify.addEventListener("click", function () {
    console.log("Verify");
    title.innerHTML = "Verify User";
    $("#verified").empty();

    $("#dash").empty();
    $("#paid_users").empty();
    $("#unpaid").empty();
    $("#unverified").empty();
    $("#report_accounts").empty();
    reportedAccounts.forEach(reportedAccount =>
        $("#verified").append(
            verifys(verifies.user_image, verifies.user_email,
                verifies.user_name))
    );


});

liUnVerify.addEventListener("click", function () {
    console.log("unverify clicked");
    title.innerHTML = "Unverified User";
    $("unverified").empty();
    $("#dash").empty();
    $("#paid_users").empty();
    $("#unpaid").empty();
    $("#verified").empty();
    $("#report_accounts").empty();

    un_verified.forEach(b =>
        $("#unverified").append(
            Un_verified(b.user_image, b.user_email,
                b.user_name))
    );

});


liReportedAccounts.addEventListener("click", function () {
    console.log("report clicked");
    title.innerHTML = "Reported Accounts";
    $("#report_accounts").empty();
    $("#dash").empty();
    $("#paid_users").empty();
    $("#unpaid").empty();
    $("#verified").empty();
    $("#unverified").empty();
    reportedAccounts.forEach(reportedAccount =>
        $("#report_accounts").append(
            reportAccount(reportedAccount.user_image, reportedAccount.user_email,
                reportedAccount.user_name))
    );

});



document.getElementById("btn_open").addEventListener("click", function () {
    console.log("BTN _OPEN");
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";

});


document.getElementById("btn_close").addEventListener("click", function () {
    console.log("BTN _CLOSE");
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
});
