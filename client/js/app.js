angular.module('starter', ['ngRoute','lbServices','starter.controllers', 'starter.services'])

.config(function($routeProvider, $locationProvider, LoopBackResourceProvider){
  
  // Use a custom auth header instead of the default 'Authorization'
  LoopBackResourceProvider.setAuthHeader('X-Access-Token');

  // Change the URL where to access the LoopBack REST API server
  LoopBackResourceProvider.setUrlBase('http://192.168.10.113:3000/api');

  $routeProvider
    .when('/',{
      templateUrl: "templates/main_page.html",
      controller: "HomeCtrl",
    })
    .when('/events',{
      templateUrl: "templates/list_event.html",
      controller: "EventsCtrl"
    })
    .when('/classes',{
      templateUrl: "templates/list_class.html",
      controller: "ClassesCtrl"
    })
    .when('/:class_id',{
      templateUrl: "templates/single_class.html",
      controller: "ClassCtrl",
    })
    .when('/:class_id/lectures',{
      templateUrl: "templates/list_lecture.html",
      controller: "LectureCtrl"
    })
    .when('/:class_id/homework',{
      templateUrl: "templates/homework.html",
      controller: "HomeWorkCtrl"
    })
    .otherwise({ 
      redirect: '/404' 
    });
})