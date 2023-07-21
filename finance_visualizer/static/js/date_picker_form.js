$(document).ready(function () {
    $("#dateForm").submit(function (e) {
        e.preventDefault();
        let submitForm = $(this).serializeArray()
        $.ajax({
            type: "POST",
            url: "/reports/",
            data: submitForm,
            success: function (html_data) {
                $('body').html(html_data);
            },
            error: function () {
                console.log('error')
            }
        });
    });
});