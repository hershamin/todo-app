describe('Home Controller', function () {
    
    var taskService, userService, homeController, scope;
    var tasks = [{'task':1}];
    
    beforeEach(function () {
        module('todo');
        
        module(function($provide) {
            // Fake user service
            $provide.value('userService', {
                isLoggedIn: function() { return true; },
                getUserInfo: function() { return {user: 'info'}; },
                logout: function() { return { then: function(callback) { return callback(""); } } }
            });
            // Fake task service
            $provide.value('taskService', {
                getTasks: function() { return { then: function(callback) { return callback(tasks); } } },
                createTask: function(title, description, priority) { return { then: function(callback) { return callback(""); } } },
                setTaskPriority: function(taskId, priority) { return { then: function(callback) { return callback(""); } } },
                completeTask: function(taskId) { return { then: function(callback) { return callback(""); } } },
                deleteTask: function(taskId) { return { then: function(callback) { return callback(""); } } }
            });
            // Fake mdDialog service
            $provide.value('$mdDialog', {
                confirm: function() { return this; },
                title: function() { return this; },
                textContent: function() { return this; },
                ariaLabel: function() { return this; },
                ok: function() { return this; },
                cancel: function() { return this; },
                show: function(options) { return { then: function(callback) { return callback(""); } } }
            });
        });
        
        // Dependency injection
        inject(function($controller, $rootScope, _userService_, _taskService_) {
            scope = $rootScope.$new();
            userService = _userService_;
            taskService = _taskService_;
            homeController = function(params) {
                return $controller('homeController', {
                    $scope: scope,
                    $stateParams: params || {}
                });
            }
        });
    });
    
    
    it('Should get tasks and user info upon initial load', function() {
        spyOn(taskService, 'getTasks').and.callThrough();
        spyOn(userService, 'getUserInfo').and.callThrough();
        homeController();
        expect(userService.getUserInfo).toHaveBeenCalled();
        expect(scope.user.user).toBe('info');
        expect(taskService.getTasks).toHaveBeenCalled();
        expect(scope.tasks.length).toBe(1);
        expect(scope.tasks[0].task).toBe(tasks[0].task);
    });
    
    
    it('Should create task', function() {
        spyOn(taskService, 'getTasks').and.callThrough();
        spyOn(taskService, 'createTask').and.callThrough();
        homeController();
        scope.currentTask = {
            title: 'title',
            description: 'desc',
            priority: 'low'
        }
        scope.saveTask();
        expect(taskService.createTask).toHaveBeenCalledWith('title', 'desc', 'low');
        expect(taskService.getTasks).toHaveBeenCalled();
    });
    
    
    it('Should complete task', function() {
        spyOn(taskService, 'getTasks').and.callThrough();
        spyOn(taskService, 'completeTask').and.callThrough();
        homeController();
        scope.completeTask(5);
        expect(taskService.completeTask).toHaveBeenCalledWith(5);
        expect(taskService.getTasks).toHaveBeenCalled();
    });
    
    
    it('Should delete task', function() {
        spyOn(taskService, 'getTasks').and.callThrough();
        spyOn(taskService, 'deleteTask').and.callThrough();
        homeController();
        scope.deleteTask(5);
        expect(taskService.deleteTask).toHaveBeenCalledWith(5);
        expect(taskService.getTasks).toHaveBeenCalled();
    });
    
    
    it('Should set task priority', function() {
        spyOn(taskService, 'getTasks').and.callThrough();
        spyOn(taskService, 'setTaskPriority').and.callThrough();
        homeController();
        scope.setTaskPriority(5, 'low');
        expect(taskService.setTaskPriority).toHaveBeenCalledWith(5, 'low');
        expect(taskService.getTasks).toHaveBeenCalled();
    });
    
});
