var app = angular.module('todo');

app.service('taskService', function ($http, $q, $cookies) {
    
    // Constants
    var loginCookie = 'todo-user-login';
    
    // Get tasks
    this.getTasks = function () {
        var defer = $q.defer();
        
        var req = {
            method: 'GET',
            url: apiUrl + 'task',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + $cookies.get(loginCookie)
            }
        };
        
        $http(req).then(function success(response) {
            // Success
            defer.resolve(response.data);
        }, function error(response) {
            // Error
            defer.reject(response.data.error);
        });
        
        return defer.promise;
    }
    
    // Create task
    this.createTask = function (title, description, priority) {
        var defer = $q.defer();
        
        var req = {
            method: 'POST',
            url: apiUrl + 'task/create',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + $cookies.get(loginCookie)
            },
            data: {
                title: title,
                description: description,
                priority: priority
            }
        };
        
        $http(req).then(function success(response) {
            // Success
            defer.resolve("");
        }, function error(response) {
            // Error
            defer.reject(response.data.error);
        });
        
        return defer.promise;
    }
    
    // Set task priority
    this.setTaskPriority = function (taskId, priority) {
        var defer = $q.defer();
        
        var req = {
            method: 'PUT',
            url: apiUrl + 'task/priority/' + taskId + '/' + priority,
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + $cookies.get(loginCookie)
            }
        };
        
        $http(req).then(function success(response) {
            // Success
            defer.resolve("");
        }, function error(response) {
            // Error
            defer.reject(response.data.error);
        });
        
        return defer.promise;
    }
    
    // Complete task
    this.completeTask = function (taskId) {
        var defer = $q.defer();
        
        var req = {
            method: 'PUT',
            url: apiUrl + 'task/complete/' + taskId,
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + $cookies.get(loginCookie)
            }
        };
        
        $http(req).then(function success(response) {
            // Success
            defer.resolve("");
        }, function error(response) {
            // Error
            defer.reject(response.data.error);
        });
        
        return defer.promise;
    }
    
    // Delete task
    this.deleteTask = function (taskId) {
        var defer = $q.defer();
        
        var req = {
            method: 'DELETE',
            url: apiUrl + 'task/delete/' + taskId,
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + $cookies.get(loginCookie)
            }
        };
        
        $http(req).then(function success(response) {
            // Success
            defer.resolve("");
        }, function error(response) {
            // Error
            defer.reject(response.data.error);
        });
        
        return defer.promise;
    }
    
});
