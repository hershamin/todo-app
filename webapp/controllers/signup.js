var app = angular.module('todo');

app.controller('signupController', function ($scope, $mdToast, $state, userService) {
    
    // Signup user
    $scope.signup = function() {
        var firstName = $scope.firstName;
        var lastName = $scope.lastName;
        var email = $scope.email;
        var password = $scope.password;
        userService.signup(firstName, lastName, email, password)
        .then(function(userInfo) {
            // Success, go to home page
            $state.go('home');
        }, function (errorMessage) {
            // Error, let user know
            $mdToast.showSimple(errorMessage);
        });
    };
    
});
