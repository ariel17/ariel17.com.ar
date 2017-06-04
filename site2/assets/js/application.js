/**
 * Copyright 2017 (C) - Ariel Gerardo Ríos
 *
 * Project: My own personal site.
 * Content: Dinamic behavior.
 */

$(function(){       
   var scroll_start = 0;
   var startchange = $('#about');
   var offset = startchange.offset();

   $(document).scroll(function() { 
      scroll_start = $(this).scrollTop();
      if(scroll_start > offset.top) {
          $(".navbar-fixed-top").switchClass("transparent", "solid");
       } else {
          $('.navbar-fixed-top').switchClass("solid", "transparent");
       }
   });
});

// vim:ft=javascript ts=2 ss=2 tw=80 cc=+1: 
