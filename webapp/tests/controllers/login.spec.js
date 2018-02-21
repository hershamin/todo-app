describe('Login Controller', function () {
    
    var taskService, userService, loginController, scope;
    var tasks = [{'task':1}];
    
    beforeEach(function () {
        module('todo');
        
        module(function($provide) {
            // Fake user service
            $provide.value('userService', {
                login: function() { return { then: function(callback) { return callback({}); } } }
            });
        });
        
        // Dependency injection
        inject(function($controller, $rootScope, _userService_) {
            scope = $rootScope.$new();
            userService = _userService_;
            loginController = function(params) {
                return $controller('loginController', {
                    $scope: scope,
                    $stateParams: params || {}
                });
            }
        });
    });
    
    
    it('Should login user', function() {
        spyOn(userService, 'login').and.callThrough();
        loginController();
        scope.email = 'email';
        scope.password = 'password';
        scope.login();
        expect(userService.login).toHaveBeenCalledWith('email', 'password');
    });
    
});
