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
