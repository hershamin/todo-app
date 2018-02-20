var app = angular.module('todo', [
    'ui.router',
    'ngMaterial',
    'ngCookies'
]); // App dependencies

app.config(function($stateProvider, $urlRouterProvider, $sceDelegateProvider) {
    
    // Url whitelist
    $sceDelegateProvider.resourceUrlWhitelist([
        'self'
    ]);
    
    // Router
    $stateProvider
    .state('login', {
        url: '/login',
        templateUrl: 'partials/login.html',
        controller: 'loginController'
    })
    .state('signup', {
        url: '/signup',
        templateUrl: 'partials/signup.html',
        controller: 'signupController'
    })
    .state('home', {
        url: '/home',
        templateUrl: 'partials/home.html',
        controller: 'homeController'
    });
    
    // Default Route
    $urlRouterProvider.otherwise('/home');
    
});
