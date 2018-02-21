var apiUrl = 'http://example.com/api/v1/';

describe('Task Service', function () {
    
    var taskService, httpBackend, cookies;
    
    beforeEach(function () {
        module('todo');

        inject(function ($httpBackend, _taskService_, $cookies) {
            taskService = _taskService_;
            httpBackend = $httpBackend;
            cookies = $cookies;
            cookies.put('todo-user-login', 'logincookie');
        });
    });
    

    afterEach(function () {
        httpBackend.verifyNoOutstandingExpectation();
        httpBackend.verifyNoOutstandingRequest();
    });
    
    
    it('Get tasks logged in', function (done) {
        
        var returnData = [
            {'task': 1}
        ]
        var headers = function(headers) {
            return headers.Authorization == 'Token logincookie';
        }
        
        httpBackend.expectGET('http://example.com/api/v1/task', headers).respond(200, returnData);
        
        taskService.getTasks()
        .then(function(tasks) {
            // Success
            expect(tasks.length).toBe(1);
            expect(tasks[0].task).toBe(returnData[0].task);
        }, function() {
            // Error
        })
        .finally(done());
        
        httpBackend.flush();
        
    });
    
    
    it('Get tasks w/o logged in', function (done) {
        
        var returnData = {
            'error': 'err'
        }
        cookies.put('todo-user-login', '');
        var headers = function(headers) {
            return headers.Authorization == 'Token ';
        }
        
        httpBackend.expectGET('http://example.com/api/v1/task', headers).respond(404, returnData);
        
        taskService.getTasks()
        .then(function(tasks) {
            // Success
        }, function(error) {
            // Error
            expect(error).toBe(returnData.error);
        })
        .finally(done());
        
        httpBackend.flush();
        
    });
    
    
    it('Create task logged in', function (done) {
        
        var returnData = [
            {'task': 1}
        ]
        var headers = function(headers) {
            return headers.Authorization == 'Token logincookie';
        }
        var postData = {
            title: 'title',
            description: 'desc',
            priority: 'low'
        }
        
        httpBackend.expectPOST('http://example.com/api/v1/task/create', postData, headers).respond(200, returnData);
        
        taskService.createTask('title', 'desc', 'low')
        .then(function(tasks) {
            // Success
        }, function() {
            // Error
        })
        .finally(done());
        
        httpBackend.flush();
        
    });
    
    
    it('Create task w/o logged in', function (done) {
        
        var returnData = {
            'error': 'err'
        }
        cookies.put('todo-user-login', '');
        var headers = function(headers) {
            return headers.Authorization == 'Token ';
        }
        var postData = {
            title: 'title',
            description: 'desc',
            priority: 'low'
        }
        
        httpBackend.expectPOST('http://example.com/api/v1/task/create', postData, headers).respond(404, returnData);
        
        taskService.createTask('title', 'desc', 'low')
        .then(function(tasks) {
            // Success
        }, function(error) {
            // Error
        })
        .finally(done());
        
        httpBackend.flush();
        
    });
    
    
    it('Set task priority logged in', function (done) {
        
        var returnData = [
            {'task': 1}
        ]
        var headers = function(headers) {
            return headers.Authorization == 'Token logincookie';
        }
        
        httpBackend.expectPUT('http://example.com/api/v1/task/priority/5/low', undefined, headers).respond(200, returnData);
        
        taskService.setTaskPriority(5, 'low')
        .then(function(tasks) {
            // Success
        }, function() {
            // Error
        })
        .finally(done());
        
        httpBackend.flush();
        
    });
    
    
    it('Set task priority w/o logged in', function (done) {
        
        var returnData = [
            {'error': 'err'}
        ]
        cookies.put('todo-user-login', '');
        var headers = function(headers) {
            return headers.Authorization == 'Token ';
        }
        
        httpBackend.expectPUT('http://example.com/api/v1/task/priority/5/low', undefined, headers).respond(404, returnData);
        
        taskService.setTaskPriority(5, 'low')
        .then(function(tasks) {
            // Success
        }, function() {
            // Error
        })
        .finally(done());
        
        httpBackend.flush();
        
    });
    
    
    it('Complete task logged in', function (done) {
        
        var returnData = [
            {'task': 1}
        ]
        var headers = function(headers) {
            return headers.Authorization == 'Token logincookie';
        }
        
        httpBackend.expectPUT('http://example.com/api/v1/task/complete/5', undefined, headers).respond(200, returnData);
        
        taskService.completeTask(5)
        .then(function(tasks) {
            // Success
        }, function() {
            // Error
        })
        .finally(done());
        
        httpBackend.flush();
        
    });
    
    
    it('Complete task w/o logged in', function (done) {
        
        var returnData = [
            {'task': 1}
        ]
        cookies.put('todo-user-login', '');
        var headers = function(headers) {
            return headers.Authorization == 'Token ';
        }
        
        httpBackend.expectPUT('http://example.com/api/v1/task/complete/5', undefined, headers).respond(404, returnData);
        
        taskService.completeTask(5)
        .then(function(tasks) {
            // Success
        }, function() {
            // Error
        })
        .finally(done());
        
        httpBackend.flush();
        
    });
    
    
    it('Delete task logged in', function (done) {
        
        var returnData = [
            {'task': 1}
        ]
        var headers = function(headers) {
            return headers.Authorization == 'Token logincookie';
        }
        
        httpBackend.expectDELETE('http://example.com/api/v1/task/delete/5', headers).respond(200, returnData);
        
        taskService.deleteTask(5)
        .then(function(tasks) {
            // Success
        }, function() {
            // Error
        })
        .finally(done());
        
        httpBackend.flush();
        
    });
    
    
    it('Delete task w/o logged in', function (done) {
        
        var returnData = [
            {'error':'err'}
        ]
        cookies.put('todo-user-login', '');
        var headers = function(headers) {
            return headers.Authorization == 'Token ';
        }
        
        httpBackend.expectDELETE('http://example.com/api/v1/task/delete/5', headers).respond(404, returnData);
        
        taskService.deleteTask(5)
        .then(function(tasks) {
            // Success
        }, function() {
            // Error
        })
        .finally(done());
        
        httpBackend.flush();
        
    });
    
});
