var bottleshopApp = angular.module('bottleshopApp', []);

bottleshopApp.controller('BottleshopController', ['$scope', '$http', '$compile', function ($scope, $http, $compile) {
	$scope.listings = [];
	$scope.recent = [];
	$scope.refreshing = true;
    $scope.beerRange = [];
    $scope.headerMessage = 'Fetching the list - coming in hot off the presses . . .';
    $scope.init = function () {
        beerInterval = setInterval($scope.addEmoji, 550);
        $http.get('/api/listings').then(
            function success(rep) {
                $scope.listings = rep.data['beers'];
                var i;
                for(i = 0; i < $scope.listings.length; i++){
                    recent = $scope.listings[i].beers.filter($scope.recentBeerFilter);
                    if (recent.length) {
                        $scope.recent.push({'brewery': $scope.listings[i].brewery, 'beers': recent});
                    }
                }
                $scope.refreshing = false;
                clearInterval(beerInterval);
            }, 
            function error(rep) {
                $scope.headerMessage = 'Beer listings are unavailable :(';
                $scope.beerRange = [];
                $scope.$apply();
            }
        );
    };

    $scope.addEmoji = function () {
        $scope.beerRange.push($scope.beerRange.length);
        // need to use $apply to get angular to update DOM
        $scope.$apply();
    }

    $scope.recentBeerFilter = function (beer) {
        return beer.recently_added;
    }

    $scope.init();
}]);