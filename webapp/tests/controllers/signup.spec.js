describe('Signup Controller', function () {
    
    var taskService, userService, signupController, scope;
    var tasks = [{'task':1}];
    
    beforeEach(function () {
        module('todo');
        
        module(function($provide) {
            // Fake user service
            $provide.value('userService', {
                signup: function() { return { then: function(callback) { return callback({}); } } }
            });
        });
        
        // Dependency injection
        inject(function($controller, $rootScope, _userService_) {
            scope = $rootScope.$new();
            userService = _userService_;
            signupController = function(params) {
                return $controller('signupController', {
                    $scope: scope,
                    $stateParams: params || {}
                });
            }
        });
    });
    
    
    it('Should signup user', function() {
        spyOn(userService, 'signup').and.callThrough();
        signupController();
        scope.email = 'email';
        scope.password = 'password';
        scope.firstName = 'first';
        scope.lastName = 'last';
        scope.signup();
        expect(userService.signup).toHaveBeenCalledWith('first', 'last', 'email', 'password');
    });
    
});
