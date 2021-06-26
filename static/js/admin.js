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
        ' <button type="button" class="btn btn-danger" >Remove</button>' +
        ' </div>' +
        ' </td>' +
        '  </tr>' +
        ' </tbody>' +
        ' </table>';
}


const liTotalUsers = document.getElementById('total_users');
const liReportedAccounts = document.getElementById('reported_accounts');
const title = document.getElementById('title_report');
const userCount = document.getElementById('users_count');

let reportedAccounts;
let paidUsers;


title.innerHTML = "Reported Accounts";

$.ajax({
    type: 'GET',
    url: 'js/5',
    success: function (response) {
        const data = response.data;
        console.log(response.report);
        reportedAccounts = response.report;
        paidUsers = response.paid_users;
        console.log('updated');
        const authStatus = data.status;
        if (authStatus !== 1)
            window.location.href = '/admin_panel';

        console.log(paidUsers);

        userCount.innerHTML = response.total_users;

        reportedAccounts.forEach(reportedAccount =>
            $("#report_accounts").append(
                reportAccount(reportedAccount.user_image, reportedAccount.user_email,
                    reportedAccount.user_name))
        );

    },
});


liTotalUsers.addEventListener("click", function () {
    title.innerHTML = "Paid Users";

    $("#paid_users").empty();
    paidUsers.forEach(reportedAccount =>
        $("#paid_users").append(
            paidUser(reportedAccount.user_image, reportedAccount.user_email,
                reportedAccount.user_name))
    );

    $("#report_accounts").empty();
});

liReportedAccounts.addEventListener("click", function () {
    title.innerHTML = "Reported Accounts";
    $("#report_accounts").empty();
    reportedAccounts.forEach(reportedAccount =>
        $("#report_accounts").append(
            reportAccount(reportedAccount.user_image, reportedAccount.user_email,
                reportedAccount.user_name))
    );

    $("#paid_users").empty();

});
