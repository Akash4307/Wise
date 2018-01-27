
        window.fbAsyncInit = function () {
            FB.init({
                appId: '1896187067075958',
                cookie: true,
                xfbml: true,
                version: 'v2.11'
            });



            FB.getLoginStatus(function (response) {
                statusChangeCallback(response);
            });



        };



        (function (d, s, id) {
            var js, fjs = d.getElementsByTagName(s)[0];
            if (d.getElementById(id)) {
                return;
            }
            js = d.createElement(s);
            js.id = id;
            js.src = "https://connect.facebook.net/en_US/sdk.js";
            fjs.parentNode.insertBefore(js, fjs);
        }(document, 'script', 'facebook-jssdk'));


        function statusChangeCallback(response) {

            if (response.status === 'connected') {
                console.log('logged in');
                document.location.href = '/buy'

                setElements(true);

                testAPI();
            } else {
                console.log('not logged in');
                setElements(false);
            }
        }

        function checkLoginState() {
            FB.getLoginStatus(function (response) {
                statusChangeCallback(response);
            });
        }

        function testAPI() {

            FB.api('/me?fields=id,name,location,email,birthday,picture,friendlists,link', function (response) {
                if (response && !response.error); {

                                       

                }
            });

        }


        

        function logout() {
            FB.logout(function (response) {
                document.location.href = '/'

                setElements(false);

            });

        }



        function setElements(isLoggedIn) {
            if (isLoggedIn) {
                document.getElementById('fb-btn').style.display = 'none';
                document.getElementById('logout').style.display = 'block';

                
                

            } else {
                document.getElementById('fb-btn').style.display = 'block';
                document.getElementById('logout').style.display = 'none';


            }
        }


        (function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = 'https://connect.facebook.net/en_GB/sdk.js#xfbml=1&version=v2.11&appId=784826381719895';
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));



