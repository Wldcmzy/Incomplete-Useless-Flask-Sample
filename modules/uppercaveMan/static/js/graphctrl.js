//window.graphCtrl01鍒�13涓�13澶勬暟鎹偣闆嗙殑鍊艰缃ぇ灏�
window.graphCtrl01 = ['$scope', function($scope) {
  $scope.sampleData = [20, 20, 30, 30, 40, 40, 50];//鏁扮粍榛樿鍊硷紝鏁版嵁鍜屾姌绾挎樉绀虹殑鍊煎ぇ灏忕浉鍙�
  
  $scope.sample = function() {
     for (var i=0, len=$scope.sampleData.length; i < len; i++) {
      //$scope.sampleData[i] = (Math.random() * 90) + 5;
	  $scope.sampleData[i] = arrlastData01[i]+80;//鍏ㄥ眬鏁扮粍鍙橀噺璧嬪€肩粰鐩爣鏁扮粍
    } 
  };
  
  $scope.sample();
  $scope.sampler = setInterval(function() {
    $scope.$apply($scope.sample);
  }, 2000);
  //姣�2000姣鏁版嵁鏀瑰彉涓€娆�
}];

window.graphCtrl02 = ['$scope', function($scope) {
  $scope.sampleData = [10, 10, 10, 10, 10, 10, 10];  //瀹氫箟鏁扮粍閲屽厓绱犵殑涓暟
  
  $scope.sample = function() {
    for (var i=0, len=$scope.sampleData.length; i < len; i++) {
      //$scope.sampleData[i] = (Math.random() * 90) + 5;
	  $scope.sampleData[i] = arrlastData02[i];   //缁欐暟缁勮祴鍊�
    }
  };
  
  $scope.sample();
  $scope.sampler = setInterval(function() {
    $scope.$apply($scope.sample);
  }, 2000);
  //姣�2000姣鏁版嵁鏀瑰彉涓€娆�
}];

window.graphCtrl03 = ['$scope', function($scope) {
  $scope.sampleData = [10, 10, 10, 10, 10, 10, 10];  //瀹氫箟鏁扮粍閲屽厓绱犵殑涓暟
  
  $scope.sample = function() {
    for (var i=0, len=$scope.sampleData.length; i < len; i++) {
      //$scope.sampleData[i] = (Math.random() * 90) + 5;
	  $scope.sampleData[i] = arrlastData03[i]-80;   //缁欐暟缁勮祴鍊�
    }
  };
  
  $scope.sample();
  $scope.sampler = setInterval(function() {
    $scope.$apply($scope.sample);
  }, 2000);
  //姣�2000姣鏁版嵁鏀瑰彉涓€娆�
}];

window.graphCtrl04 = ['$scope', function($scope) {
  $scope.sampleData = [10, 10, 10, 10, 10, 10, 10];  //瀹氫箟鏁扮粍閲屽厓绱犵殑涓暟
  
  $scope.sample = function() {
    for (var i=0, len=$scope.sampleData.length; i < len; i++) {
      //$scope.sampleData[i] = (Math.random() * 30) + 5;
	  $scope.sampleData[i] = arrlastData04[i]+80;   //缁欐暟缁勮祴鍊�
    }
  };
  
  $scope.sample();
  $scope.sampler = setInterval(function() {
    $scope.$apply($scope.sample);
  }, 2000);
  //姣�2000姣鏁版嵁鏀瑰彉涓€娆�
}];

window.graphCtrl05 = ['$scope', function($scope) {
  $scope.sampleData = [10, 10, 10, 10, 10, 10, 10];  //瀹氫箟鏁扮粍閲屽厓绱犵殑涓暟
  
  $scope.sample = function() {
    for (var i=0, len=$scope.sampleData.length; i < len; i++) {
      //$scope.sampleData[i] = (Math.random() * 90) + 5;
	  $scope.sampleData[i] = arrlastData05[i]+80;   //缁欐暟缁勮祴鍊�
    }
  };
  
  $scope.sample();
  $scope.sampler = setInterval(function() {
    $scope.$apply($scope.sample);
  }, 2000);
  //姣�2000姣鏁版嵁鏀瑰彉涓€娆�
}];

window.graphCtrl06 = ['$scope', function($scope) {
  $scope.sampleData = [10, 10, 10, 10, 10, 10, 10];  //瀹氫箟鏁扮粍閲屽厓绱犵殑涓暟
  
  $scope.sample = function() {
    for (var i=0, len=$scope.sampleData.length; i < len; i++) {
      //$scope.sampleData[i] = (Math.random() * 90) + 5;
	  $scope.sampleData[i] = arrlastData06[i]-600;   //缁欐暟缁勮祴鍊�
    }
  };
  
  $scope.sample();
  $scope.sampler = setInterval(function() {
    $scope.$apply($scope.sample);
  }, 2000);
  //姣�2000姣鏁版嵁鏀瑰彉涓€娆�
}];

window.graphCtrl07 = ['$scope', function($scope) {
  $scope.sampleData = [10, 10, 10, 10, 10, 10, 10];  //瀹氫箟鏁扮粍閲屽厓绱犵殑涓暟
  
  $scope.sample = function() {
    for (var i=0, len=$scope.sampleData.length; i < len; i++) {
      //$scope.sampleData[i] = (Math.random() * 20) + 5;
	  $scope.sampleData[i] = arrlastData07[i];   //缁欐暟缁勮祴鍊�
    }
  };
  
  $scope.sample();
  $scope.sampler = setInterval(function() {
    $scope.$apply($scope.sample);
  }, 2000);
  //姣�2000姣鏁版嵁鏀瑰彉涓€娆�
}];

window.graphCtrl08 = ['$scope', function($scope) {
  $scope.sampleData = [10, 10, 10, 10, 10, 10, 10];  //瀹氫箟鏁扮粍閲屽厓绱犵殑涓暟
  
  $scope.sample = function() {
    for (var i=0, len=$scope.sampleData.length; i < len; i++) {
      //$scope.sampleData[i] = (Math.random() * 90) + 5;
	  $scope.sampleData[i] = arrlastData08[i]-250;   //缁欐暟缁勮祴鍊�
    }
  };
  
  $scope.sample();
  $scope.sampler = setInterval(function() {
    $scope.$apply($scope.sample);
  }, 2000);
  //姣�2000姣鏁版嵁鏀瑰彉涓€娆�
}];

window.graphCtrl09 = ['$scope', function($scope) {
  $scope.sampleData = [10, 10, 10, 10, 10, 10, 10];  //瀹氫箟鏁扮粍閲屽厓绱犵殑涓暟
  
  $scope.sample = function() {
    for (var i=0, len=$scope.sampleData.length; i < len; i++) {
      //$scope.sampleData[i] = (Math.random() * 60) + 5;
	  $scope.sampleData[i] = arrlastData09[i];   //缁欐暟缁勮祴鍊�
    }
  };
  
  $scope.sample();
  $scope.sampler = setInterval(function() {
    $scope.$apply($scope.sample);
  }, 2000);
  //姣�2000姣鏁版嵁鏀瑰彉涓€娆�
}];

window.graphCtrl10 = ['$scope', function($scope) {
  $scope.sampleData = [10, 10, 10, 10, 10, 10, 10];  //瀹氫箟鏁扮粍閲屽厓绱犵殑涓暟
  
  $scope.sample = function() {
    for (var i=0, len=$scope.sampleData.length; i < len; i++) {
      //$scope.sampleData[i] = (Math.random() * 90) + 5;
	  $scope.sampleData[i] = arrlastData10[i];   //缁欐暟缁勮祴鍊�
    }
  };
  
  $scope.sample();
  $scope.sampler = setInterval(function() {
    $scope.$apply($scope.sample);
  }, 2000);
  //姣�2000姣鏁版嵁鏀瑰彉涓€娆�
}];

window.graphCtrl11 = ['$scope', function($scope) {
  $scope.sampleData = [10, 10, 10, 10, 10, 10, 10];  //瀹氫箟鏁扮粍閲屽厓绱犵殑涓暟
  
  $scope.sample = function() {
    for (var i=0, len=$scope.sampleData.length; i < len; i++) {
      //$scope.sampleData[i] = (Math.random() * 40) + 5;
	  $scope.sampleData[i] = arrlastData11[i]+40;   //缁欐暟缁勮祴鍊�
    }
  };
  
  $scope.sample();
  $scope.sampler = setInterval(function() {
    $scope.$apply($scope.sample);
  }, 2000);
  //姣�2000姣鏁版嵁鏀瑰彉涓€娆�
}];

window.graphCtrl12 = ['$scope', function($scope) {
  $scope.sampleData = [10, 10, 10, 10, 10, 10, 10];  //瀹氫箟鏁扮粍閲屽厓绱犵殑涓暟
  
  $scope.sample = function() {
    for (var i=0, len=$scope.sampleData.length; i < len; i++) {
      //$scope.sampleData[i] = (Math.random() * 90) + 5;
	  $scope.sampleData[i] = arrlastData12[i]-200;   //缁欐暟缁勮祴鍊�
    }
  };
  
  $scope.sample();
  $scope.sampler = setInterval(function() {
    $scope.$apply($scope.sample);
  }, 2000);
  //姣�2000姣鏁版嵁鏀瑰彉涓€娆�
}];

window.graphCtrl13 = ['$scope', function($scope) {
  $scope.sampleData = [10, 10, 10, 10, 10, 10, 10];  //瀹氫箟鏁扮粍閲屽厓绱犵殑涓暟
  
  $scope.sample = function() {
    for (var i=0, len=$scope.sampleData.length; i < len; i++) {
      //$scope.sampleData[i] = (Math.random() * 90) + 5;
	  $scope.sampleData[i] = arrlastData13[i];   //缁欐暟缁勮祴鍊�
    }
  };
  
  $scope.sample();
  $scope.sampler = setInterval(function() {
    $scope.$apply($scope.sample);
  }, 2000);
  //姣�2000姣鏁版嵁鏀瑰彉涓€娆�
}];

var app1 = angular.module('myApp', []); // angular鏂板缓涓€涓ā鍧梞odule妯″潡鍚嶄负myApp 鍙湁绗竴涓彲浠ヨ嚜鍔ㄥ惎鍔紝鍏跺畠鐨勫氨闇€瑕佹墜鍔ㄩ€氳繃angular.bootstrap鏉ュ惎鍔�
app1.directive('graph', function() {
  return {
    restrict: 'A',
    link: function(scope, elm, attr) {
      var points = elm[0].querySelectorAll('[data-point]');
      
      // graph data provided by the "data" attribute.
      // NB: data is interpreted as percentages
      scope.$watch(attr.data, function(data) {
        angular.forEach(data, function(val, i) {
          var pt = points[i]
            , psty = pt && pt.style;
          
          if (psty) {
            var sect = pt.parentNode
              , sectWidth = sect.offsetWidth
              , sectHeight = sect.offsetHeight;
          
            sect.title = Math.round(100 - val) + '%';
            psty.top = (val * sectHeight / 100) + 'px';
            
            var next = data[i + 1];
            if (typeof next === 'number') {
              var delta = (next - val) * sectHeight / 100;
              
              psty.height = Math.sqrt(Math.pow(sectWidth, 2) + Math.pow(delta, 2)) + 'px';//鏁版嵁鐐硅繛绾跨殑闀垮害
              psty.webkitTransform =
                psty.msTransform =
                psty.transform =
                  'rotate('+(-Math.PI / 2 + Math.atan2(delta, sectWidth))+'rad)';
            }
          }
        });
      }, /* deep */ true);
        
    }
  };
});

//绗竴涓ā鍧楃粨鏉�