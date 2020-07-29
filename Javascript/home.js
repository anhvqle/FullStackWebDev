angular.module('ionicApp', ['ionic'])

.config(function($stateProvider, $urlRouterProvider) {

  $stateProvider

    .state('main', {
      url: "/main",
      abstract: true,
      templateUrl: "menu.html"
    })

    .state('main.tabs', {
      url: "/tab",
      abstract: true,
      views: {
        'menu-content': {
          templateUrl: "tabs.html",
        }
      }
    })
    .state('main.tabs.home', {
      url: "/home",
      views: {
        'home-tab': {
          templateUrl: "home.html",
          controller: 'HomeTabCtrl'
        }
      }
    })
    .state('main.tabs.facts', {
      url: "/facts",
      views: {
        'home-tab': {
          templateUrl: "facts.html"
        }
      }
    })
    .state('main.tabs.facts2', {
      url: "/facts2",
      views: {
        'home-tab': {
          templateUrl: "facts2.html"
        }
      }
    })
    .state('main.tabs.about', {
      url: "/about",
      views: {
        'about-tab': {
          templateUrl: "about.html"
        }
      }
    })

    .state('main.tabs.feature', {
      url: "/feature",
      views: {
        'feature-tab': {
          templateUrl: "feature.html"
        }
      }
    })

  .state('main.tabs.navstack', {
      url: "/navstack",
      views: {
        'about-tab': {
          templateUrl: "nav-stack.html"
        }
      }
    })
    .state('main.tabs.contact', {
      url: "/contact",
      views: {
        'contact-tab': {
          templateUrl: "contact.html"
        }
      }
    })
    .state('main.feature', {
      url: "/feature",
      views: {
        'menu-content': {
          templateUrl: "feature.html"
        }
      }
    });


   $urlRouterProvider.otherwise("/main/tab/home");

})

.controller('HomeTabCtrl', function($scope) {
  console.log('HomeTabCtrl');
})

.controller('MainCtrl', function($scope, $ionicSideMenuDelegate) {

  $scope.mainCtrl = {};
  $scope.leftButtons = [{
    type: 'button-icon button-clear ion-navicon',
    tap: function(e) {
      $ionicSideMenuDelegate.toggleLeft($scope.$$childHead);
    }
  }];

  $scope.mainCtrl.showFeature = false;

});
