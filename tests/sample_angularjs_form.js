angular.module('demoApp', [])
  .controller('DemoCtrl', function($scope) {
    $scope.user = { name: '', email: '' };
  });
