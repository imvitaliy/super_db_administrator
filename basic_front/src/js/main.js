'use strict';

// var angular = require('angular');
console.log('Angular cargado');

// Carga de controladores
// var TestCtrl = require('./controllers/TestCtrl');

// var app = angular.module('app', []);

// app.controller('TestCtrl', ['$scope', TestCtrl]);

var tootleMenuElement = document.getElementById('toogleMenu');
var navMenu = document.getElementById('navMenu');


function tootleMenu () {

  if (navMenu.className == 'MainNav hide'){
    navMenu.className = 'MainNav';
  }else {
    navMenu.className = 'MainNav hide';
  }

}


window.onload = function()
{
  tootleMenuElement.addEventListener( 'click' , tootleMenu );
}
