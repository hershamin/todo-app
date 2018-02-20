var app = angular.module('todo');

app.controller('homeController', function ($scope, $mdToast, $state, $mdDialog, userService) {
    
    // Vars
    $scope.user = userService.getUserInfo();
    
    // If not logged in, go to login page
    if (!userService.isLoggedIn()) {
        $state.go('login');
    }
    
    // Logout user
    $scope.logout = function() {
        userService.logout()
        .then(function(success) {
            // Success, go to login page
            $state.go('login');
        }, function(errorMessage) {
            // Error, let user know, & go to login page
            $mdToast.showSimple(errorMessage);
            $state.go('login');
        });
    }
    
});
