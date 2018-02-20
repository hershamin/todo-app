var app = angular.module('todo');

app.controller('loginController', function ($scope, $mdToast, $state, userService) {
    
    // Login user
    $scope.login = function() {
        userService.login($scope.email, $scope.password)
        .then(function(userInfo) {
            // Success, go to home page
            $state.go('home');
        }, function(errorMessage) {
            // Error, let user know
            $mdToast.showSimple(errorMessage);
        });
    }
    
});
