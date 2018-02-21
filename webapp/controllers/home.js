var app = angular.module('todo');

app.controller('homeController', function ($scope, $mdToast, $state, $mdDialog, userService, taskService) {
    
    // Vars
    $scope.priorityOptions = ['Low', 'Medium', 'High'];
    $scope.user = userService.getUserInfo();
    $scope.tasks = [];
    $scope.currentTask = {};
    
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
    
    // Show add task dialog
    $scope.addDialog = function() {
        // Show dialog for add task (pre-rendered)
        $scope.currentTask = {};
        $mdDialog.show({
            contentElement: '#addTaskDialog',
            parent: angular.element(document.body),
            clickOutsideToClose: true
        });
    }
    
    // Set taskbox css
    $scope.taskCss = function(task) {
        var styles = {}
        if (task.status == 'Done') {
            styles['text-decoration'] = 'line-through';
            styles['border-left'] = '15px solid black';
        } else {
            if (task.priority == 'Low') {
                styles['border-left'] = '15px solid #3f51b5';
            } else if (task.priority == 'Medium') {
                styles['border-left'] = '15px solid #4caf50';
            } else if (task.priority == 'High') {
                styles['border-left'] = '15px solid #ff5722';
            }
        }
        
        return styles;
    }
    
    // Reload page
    $scope.reloadPage = function() {
        // Reload state
        $state.reload('home');
    }
    
    // Get tasks
    $scope.getTasks = function() {
        taskService.getTasks()
        .then(function(tasks) {
            // Success, set tasks
            $scope.tasks = tasks;
        }, function(errorMessage) {
            // Error, let user know
            $mdToast.showSimple(errorMessage);
        });
    }
    $scope.getTasks(); // Initially get tasks
    
    // Save newly created task
    $scope.saveTask = function() {
        // Create new task
        taskService.createTask($scope.currentTask.title, $scope.currentTask.description, $scope.currentTask.priority)
        .then(function(success) {
            // Success, reload
            $scope.reloadPage();
        }, function(errorMessage) {
            // Error, let user know
            $mdToast.showSimple(errorMessage);
        });
    }
    
    // Complete task
    $scope.completeTask = function(taskId) {
        taskService.completeTask(taskId)
        .then(function(success) {
            // Success, reload
            $scope.reloadPage();
        }, function(errorMessage) {
            // Error, let user know
            $mdToast.showSimple(errorMessage);
        });
    }
    
    // Delete task
    $scope.deleteTask = function(taskId, taskTitle) {
        // Show warning, if yes, then do it.
        var confirm = $mdDialog.confirm()
            .title('Delete Task?')
            .textContent('This CANNOT be reversed, do you want to delete task ' + taskTitle + '?')
            .ariaLabel('Delete task')
            .ok('Yes')
            .cancel('No')
        $mdDialog.show(confirm)
        .then(function() {
            // YES
            taskService.deleteTask(taskId)
            .then(function(success) {
                // Success, reload
                $scope.reloadPage();
            }, function(errorMessage) {
                // Error, let user know
                $mdToast.showSimple(errorMessage);
            });
        }, function() {
            // NO
        });
    }
    
    // Set task prioirity
    $scope.setTaskPriority = function(taskId, priority) {
        taskService.setTaskPriority(taskId, priority)
        .then(function(success) {
            // Success, reload
            $scope.reloadPage();
        }, function(errorMessage) {
            // Error, let user know
            $mdToast.showSimple(errorMessage);
        });
    }
    
});
