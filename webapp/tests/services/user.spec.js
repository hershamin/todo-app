var apiUrl = 'http://example.com/api/v1/';

describe('User Service', function () {
    
    var userService, httpBackend, cookies;
    
    beforeEach(function () {
        module('todo');

        inject(function ($httpBackend, _userService_, $cookies) {
            userService = _userService_;
            httpBackend = $httpBackend;
            cookies = $cookies;
            cookies.remove('todo-user-login');
        });
    });
    

    afterEach(function () {
        httpBackend.verifyNoOutstandingExpectation();
        httpBackend.verifyNoOutstandingRequest();
    });
    
    
    it('Login with right user', function (done) {
        
        var returnData = {
            'first_name': 'first',
            'last_name': 'last',
            'login_token': 'logintoken',
            'email': 'email@email.com'
        }
        
        httpBackend.expectPOST('http://example.com/api/v1/user/login').respond(200, returnData);
        
        userService.login('email@email.com', 'password')
        .then(function() {
            // Success
            expect(userService.isLoggedIn()).toBe(true);
            expect(userService.getUserInfo().first_name).toBe(returnData.first_name);
            expect(userService.getUserInfo().last_name).toBe(returnData.last_name);
            expect(userService.getUserInfo().email).toBe(returnData.email);
            expect(cookies.get('todo-user-login')).toBe(returnData.login_token);
        }, function() {
            // Error
        })
        .finally(done());
        
        httpBackend.flush();
        
    });
    
    
    it('Login with wrong user', function (done) {
        
        var returnData = {
            error: 'error'
        }
        
        httpBackend.expectPOST('http://example.com/api/v1/user/login').respond(404, returnData);
        
        userService.login('email@email.com', 'password')
        .then(function() {
            // Success
        }, function() {
            // Error
            expect(userService.isLoggedIn()).toBe(false);
            expect(cookies.get('todo-user-login')).toBe(undefined);
        })
        .finally(done());
        
        httpBackend.flush();
        
    });
    
    
    it('Logout user succeed', function (done) {
        
        var returnData = {
            logout: 'true'
        }
        
        cookies.put('todo-user-login', 'logintoken');
        expect(cookies.get('todo-user-login')).toBe('logintoken');
        
        httpBackend.expectPOST('http://example.com/api/v1/user/logout').respond(200, returnData);
        
        userService.logout()
        .then(function() {
            // Success
            expect(userService.isLoggedIn()).toBe(false);
            expect(cookies.get('todo-user-login')).toBe(undefined);
        }, function() {
            // Error
        })
        .finally(done());
        
        httpBackend.flush();
        
    });
    
    
    it('Logout user fail', function (done) {
        
        var returnData = {
            error: 'err'
        }
        
        cookies.put('todo-user-login', 'logintoken');
        expect(cookies.get('todo-user-login')).toBe('logintoken');
        
        httpBackend.expectPOST('http://example.com/api/v1/user/logout').respond(404, returnData);
        
        userService.logout()
        .then(function() {
            // Success
        }, function() {
            // Error
            expect(userService.isLoggedIn()).toBe(false);
            expect(cookies.get('todo-user-login')).toBe(undefined);
        })
        .finally(done());
        
        httpBackend.flush();
        
    });
    
    
    it('Signup user succeed', function (done) {
        
        var returnData = {
            'first_name': 'first',
            'last_name': 'last',
            'login_token': 'logintoken',
            'email': 'email@email.com'
        }
        
        cookies.put('todo-user-login', 'logintoken');
        expect(cookies.get('todo-user-login')).toBe('logintoken');
        
        httpBackend.expectPOST('http://example.com/api/v1/user/signup').respond(200, returnData);
        
        userService.signup(returnData.first_name, returnData.last_name, returnData.email, 'password')
        .then(function() {
            // Success
            expect(userService.isLoggedIn()).toBe(true);
            expect(userService.getUserInfo().first_name).toBe(returnData.first_name);
            expect(userService.getUserInfo().last_name).toBe(returnData.last_name);
            expect(userService.getUserInfo().email).toBe(returnData.email);
            expect(cookies.get('todo-user-login')).toBe(returnData.login_token);
        }, function() {
            // Error
        })
        .finally(done());
        
        httpBackend.flush();
        
    });
    
    
    it('Signup user fail', function (done) {
        
        var returnData = {
            error: 'err'
        }
        
        httpBackend.expectPOST('http://example.com/api/v1/user/signup').respond(404, returnData);
        
        userService.signup(returnData.first_name, returnData.last_name, returnData.email, 'password')
        .then(function() {
            // Success
        }, function() {
            // Error
            expect(userService.isLoggedIn()).toBe(false);
            expect(cookies.get('todo-user-login')).toBe(undefined);
        })
        .finally(done());
        
        httpBackend.flush();
        
    });
    
    
});
