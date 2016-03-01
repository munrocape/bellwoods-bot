var bottleshopApp = angular.module('bottleshopApp', []);

bottleshopApp.controller('BottleshopController', ['$scope', '$http', '$compile', function ($scope, $http, $compile) {
	$scope.listings = [];
	$scope.recent = [];
	$scope.refreshing = true;
    $scope.headerMessage = 'Fetching the list - coming in hot off the presses ...';
    $scope.init = function () {
    	// Simple GET request example:
    	$http.get('/api/listings').then(
    		function success(rep) {
    			$scope.listings = rep.data['beers'];
    			$scope.refreshing = false;
    		}, 
    		function error(rep) {
                $scope.headerMessage = 'Beer listings are unavailable :(';
    		}
    	);
    }

    $scope.displayError = function(msg) {
    	$scope.error = msg;
    }

    $scope.init();
}]);