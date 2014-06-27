(function(){
	var app = angular.module('piMash', []);

	app.controller('TempController', ['$http', function($http){
		var temp = this;

		$http.get('/_temperature').success(function(data){
			temp.tempData = data;
		});
	}]);

	var td = {
		temp :  111.1,
        setpoint : 123,
        element : 'Static'
    };
})();

