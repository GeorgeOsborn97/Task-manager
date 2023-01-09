$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.datepicker').datepicker({
      format: "dd mmmm, yyyy",
      i18n: {done: 'Select'}
    });
    $('select').formSelect();
    $('.collapsible').collapsible();
  });

  /*$(document).ready(function(){
    $('.datepicker').datepicker({
      format: "dd mmmm, yyyy"
    });
  });*/
            