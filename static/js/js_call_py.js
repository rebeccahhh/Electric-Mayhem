<body>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="jquery.js"></script>
<script>
function processSayingHi() {          
   
   
   $.ajax({
       url: '/api/your_controller_name/SayHi/',
       type: 'GET',
       success: function (response) {
           console.log(response);
       },
       error: function (error) {
           console.log(error);
       }
    })
}
</script>
</body>
