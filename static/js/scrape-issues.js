// pull specific issues button back end:

$(function(){
    function storeIssue(issue){
        var info = new Array();
        info.push({"number": issue.number});
        info.push({"title": issue.title});
        info.push({"body": issue.body});
        info.push({"html_url": issue.html_url});
        alert("info stored");
        var blob = new Blob([JSON.stringify(info)], {type: "text/plain;charset=utf-8"});
        saveAs(blob, "hello world.txt");
    }

function getIssue(ourUrl){
  $.ajax ({	 
      url: "https://api.github.com/repos" + ourUrl.replace(/^.*\/\/[^\/]+/, ''),
      type: "GET",
      headers: {'Authorization': 'd4cfa9c6bc4353c3767c9dd1a2d3628d8f8f0d5a'}
   }) .done(function(issue){
	    storeIssue(issue);
   });
}

$("#submit").onClick(getIssue($("#url").value));
  
});

