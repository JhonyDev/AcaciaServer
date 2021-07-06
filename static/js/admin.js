function dashboard(total, paid, unpaid, verified, unverified, reported) {
    return '<div class="container mt-4">' +
        '             <div class="row">' +
        '' +
        '                    <div class="col-md-4">' +
        '                        <div class="card-counter info">' +
        '                            <i class="fa fa-users"></i>' +
        '                            <span class="count-numbers">' + total + '</span>' +
        '                            <span class="count-name">Total Users</span>' +
        '                        </div>' +
        '                    </div>' +
        '' +
        '                    <div class="col-md-4">' +
        '                        <div class="card-counter primary">' +
        '                            <i class="fa fa-user-plus"></i>' +
        '                            <span class="count-numbers">' + paid + '</span>' +
        '                            <span class="count-name">Paid Users</span>' +
        '                        </div>' +
        '                    </div>' +
        '' +
        '                    <div class="col-md-4">' +
        '                        <div class="card-counter danger">' +
        '                            <i class="fa fa-user-times"></i>' +
        '                            <span class="count-numbers">' + unpaid + '</span>' +
        '                            <span class="count-name">Un-Paid Users</span>' +
        '                        </div>' +
        '                    </div>' +
        '' +
        '                    <div class="col-md-4">' +
        '                        <div class="card-counter success">' +
        '                            <i class="fa fa-check-circle"></i>' +
        '                            <span class="count-numbers">' + verified + '</span>' +
        '                            <span class="count-name">Verified Account</span>' +
        '                        </div>' +
        '                    </div>' +
        '' +
        '                    <div class="col-md-4">' +
        '                        <div class="card-counter success">' +
        '                            <i class="fa fa-times-circle"></i>' +
        '                            <span class="count-numbers">' + unverified + '</span>' +
        '                            <span class="count-name">Un-Verified Account</span>' +
        '                        </div>' +
        '                    </div>' +
        '' +
        '                    <div class="col-md-4">' +
        '                        <div class="card-counter success">' +
        '                            <i class="fa fa-exclamation-triangle"></i>' +
        '                            <span class="count-numbers">' + reported + '</span>' +
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

let mainResponse;

title.innerHTML = "Dashboard";

$.ajax({
    type: 'GET',
    url: 'js/5',
    success: function (response) {
        const data = response.data;
        console.log(response);
        mainResponse = response;

        console.log('updated');


        $("#dash").empty();
        $("#dash").append(
            dashboard(mainResponse.total_users, mainResponse.paid_users.length, mainResponse.unpaid_users.length,
                mainResponse.verified_users.length, mainResponse.unverified_users.length, mainResponse.report.length));


        const authStatus = data.status;
        if (authStatus !== 1)
            window.location.href = '/admin_panel';


        // userCount.innerHTML = mainResponse.total_users;


    },
});

liDash_Board.addEventListener("click", function () {
    console.log("Dash");

    title.innerHTML = "Dashboard";

    $("#dash").empty();
    $("#dash").append(
        dashboard(mainResponse.total_users, mainResponse.paid_users.length, mainResponse.unpaid_users.length,
            mainResponse.verified_users.length, mainResponse.unverified_users.length, mainResponse.report.length));

    $("#paid_users").empty();
    $("#unpaid").empty();
    $("#verified").empty();
    $("#unverified").empty();
    $("#report_accounts").empty();
});


liTotalUsers.addEventListener("click", function () {

    title.innerHTML = "Paid Users";

    $("#dash").empty();
    $("#unpaid").empty();
    $("#verified").empty();
    $("#unverified").empty();
    $("#report_accounts").empty();

    $("#paid_users").empty();
    mainResponse.paid_users.forEach(a =>
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
    mainResponse.unpaid_users.forEach(unpaid =>
        $("#unpaid").append(
            unpaidUser(unpaid.user_image, unpaid.user_email,
                unpaid.user_name))
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
    mainResponse.verified_users.forEach(verified =>
        $("#verified").append(
            verifys(verified.user_image, verified.user_email,
                verified.name))
    );


});

liUnVerify.addEventListener("click", function () {
    console.log("unverify clicked");
    title.innerHTML = "Unverified User";
    $("#unverified").empty();
    $("#dash").empty();
    $("#paid_users").empty();
    $("#unpaid").empty();
    $("#verified").empty();
    $("#report_accounts").empty();-

    mainResponse.unverified_users.forEach(b =>
        $("#unverified").append(
            Un_verified(b.user_image, b.user_email,
                b.name))
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
    mainResponse.report.forEach(reportedAccount =>
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
    console.log(screen.width);
    if (screen.width > 1028)
        return;

    console.log("BTN _CLOSE");
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
});
