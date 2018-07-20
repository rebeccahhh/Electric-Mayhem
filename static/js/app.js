// home.html buttons

var showButton = document.getElementById('show');
    showButton.onclick = function () {
    window.open("./show.html", "_self");
    };
   
var issueNumbers = document.getElementsByName();
    
var pullButton = document.getElementById('pull');
    pullButton.onclick = function () {
    window.open("./pull.html", "_self");
    };

var editButton = document.getElementById('edit');
    editButton.onclick = function () {
    window.open("../documents/HackathonTemplate.docx");
    };

// var ourURL = "https://github.com/rebeccahhh/Electric-Mayhem/issues/5"
// var submitForm = document.getElementById('submit');
//     submitForm.onclick = function getIssue(ourUrl){
//     alert ("WORKING")};