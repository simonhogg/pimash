(function(){
	var app = angular.module('piMash', []);

	app.controller('TempController', ['$http', 
		function($http){
			var temp = this;

			update = function(){
				$http.get('/_temperature').success(function(data){
					temp.tempData = data;
				});
				setTimeout(update, 1000);
			};
			update();	

			temp.tempArray = ['104', '140', '153', '158', '170'];

			temp.updateSetPoint = function(sp) {
				$http.get('/_updateSetPoint/' + sp);
				temp.tempInput = sp;
			};

			temp.tempInput = "";
		}	
	]);
})();

