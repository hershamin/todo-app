var app = angular.module('todo');

app.service('userService', function ($http, $q, $cookies, $window) {
    
    // Constants
    var loginCookie = 'todo-user-login';
    var userInfo = 'todo-user-info';
    
    // Check if user is logged in
    this.isLoggedIn = function() {
        // Check cookie
        var token = $cookies.get(loginCookie);
        if (token) {
            return true;
        } else {
            return false;
        }
    }
    
    // Get stored user info
    this.getUserInfo = function () {
        var user = $window.localStorage[userInfo];
        if (user) {
            try {
                return JSON.parse(user);
            } catch (err) {
                return {};
            }
        } else {
            return {};
        }
    }
    var storeUserInfo = function (user) {
        $window.localStorage[userInfo] = JSON.stringify(user);
    }
    
    // Login user
    this.login = function (email, password) {
        var defer = $q.defer();
        
        var req = {
            method: 'POST',
            url: apiUrl + 'user/login',
            headers: {
                'Content-Type': 'application/json',
            },
            data: {
                email: email,
                password: password
            }
        };
        
        $http(req).then(function success(response) {
            // Success
            var token = response.data.login_token;
            $cookies.put(loginCookie, token);
            storeUserInfo(response.data);
            defer.resolve(response.data);
        }, function error(response) {
            // Error
            defer.reject(response.data.error);
        });
        
        return defer.promise;
    };
    
    // Logout user
    this.logout = function () {
        var defer = $q.defer();
        
        var req = {
            method: 'POST',
            url: apiUrl + 'user/logout',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + $cookies.get(loginCookie)
            }
        };
        $http(req).then(function success(response) {
            // Success
            $cookies.remove(loginCookie);
            defer.resolve("");
        }, function error(response) {
            // Error
            $cookies.remove(loginCookie);
            defer.reject("");
        });
        
        return defer.promise;
    };
    
    // Signup user
    this.signup = function(firstName, lastName, email, password) {
        var defer = $q.defer();
        
        var req = {
            method: 'POST',
            url: apiUrl + 'user/signup',
            headers: {
                'Content-Type' : 'application/json'
            },
            data: {
                first_name: firstName,
                last_name: lastName,
                email: email,
                password: password
            }
        };
        
        $http(req).then(function success(response) {
            // Success
            var token = response.data.login_token;
            $cookies.put(loginCookie, token);
            storeUserInfo(response.data);
            defer.resolve(response.data);
        }, function error(response) {
            // Error
            defer.reject(response.data.error);
        });
        
        return defer.promise;
    };
    
});
