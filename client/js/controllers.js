angular.module('starter.controllers', [])

.controller('MainCtrl', function($scope, User) {
  $("#slize").show();

  $scope.createUser = function() {
    var data = $.param({
      email: 'foo@bar.com', 
      password: 'bar'
    });

    User.login({"email":$scope.username,"password":$scope.password}, function(user) {
      console.log(user['user'].status);
      localStorage.setItem('user_id', user.id);
      localStorage.setItem('status', user['user'].status);
      $("#modal_login").modal('hide');
      //console.log(localStorage.getItem('user_id'));
    });
  };

})

.controller('HomeCtrl', function($scope) {
  $("#slize").show();


})

.controller('ClassesCtrl', function($scope, Class) {
  $("#slize").show();

  function getTodos() {
    Class
      .find()
      .$promise
      .then(function(results) {
        console.log(results);
        $scope.listClass = results;

        console.log($scope.listClass);
      });
  }
  getTodos();

})

.controller('ClassCtrl', function($scope, $route, Questions) {
  $("#slize").hide();
  $scope.class_id = $route.current.params.class_id;

  if (localStorage.getItem('status' != 0)) {
    $scope.status = true;
  }else{
    $scope.status = false;
  }

  function getTodos() {
    Questions
    .find()
    .$promise
    .then(function(results) {
      console.log(results);
      $scope.listQuestions = results;

      console.log($scope.listQuestions);
    });

  }
  getTodos();
})

.controller('LectureCtrl', function($scope, $route, Resources) {
  $("#slize").show();

  function getTodos() {
    Resources
      .find()
      .$promise
      .then(function(results) {
        console.log(results);
        $scope.listResources = results;

        console.log($scope.listResources);
      });

      Questions
      .find()
      .$promise
      .then(function(results) {
        console.log(results);
        $scope.listQuestions = results;

        console.log($scope.listQuestions);
      });

  }
  getTodos();  
})

.controller('EventsCtrl', function($scope) {
  $("#slize").show();
})

.controller('HomeWorkCtrl', function($scope) {
  $("#slize").hide();
})

.controller('ChatsCtrl', function($scope, Chats) {
  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //
  //$scope.$on('$ionicView.enter', function(e) {
  //});

  $scope.chats = Chats.all();
  $scope.remove = function(chat) {
    Chats.remove(chat);
  };
})

.controller('ChatDetailCtrl', function($scope, $stateParams, Chats) {
  $scope.chat = Chats.get($stateParams.chatId);
})

.controller('AccountCtrl', function($scope) {
  $scope.settings = {
    enableFriends: true
  };
});
