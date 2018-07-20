function postData(input) {
    $.ajax({
        type: "POST",
        url: "/gitAcces.py",
        data: { param: issues },
        success: callbackFunc
    });
}

function callbackFunc(response) {
    // do something with the response
    console.log(response);
}