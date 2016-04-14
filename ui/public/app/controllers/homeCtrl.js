angular.module('app')
    .controller('homeCtrl', function($scope, $http) {


        $scope.setup = function() {        	
        	$http.get('/?name=3')
                .then(function(response) {
                   console.log(response)
                }, function(err) {
                    console.log(err)
                });
            

        }

        $scope.setup();



    })
