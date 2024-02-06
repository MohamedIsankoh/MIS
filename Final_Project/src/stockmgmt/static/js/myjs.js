$(document).ready(function(){
  
    // alert("We are all set!");

   

    
      // Enable datepicker for elements with class 'datetimeinput'
      $(".datetimeinput").datepicker({
        changeYear: true,
        changeMonth: true,
        dateFormat: 'yy-mm-dd'
      });
   

    $(".datetimeinput").datepicker({changeYear: true,changeMonth: true, dateFormat: 'yy-mm-dd'});


    $('#div_id_line_three, #div_id_line_three_quantity, #div_id_line_three_unit_price, #div_id_line_three_total_price,#div_id_line_four, #div_id_line_four_quantity, #div_id_line_four_unit_price, #div_id_line_four_total_price,#div_id_line_five, #div_id_line_five_quantity, #div_id_line_five_unit_price, #div_id_line_five_total_price,#div_id_line_six, #div_id_line_six_quantity, #div_id_line_six_unit_price, #div_id_line_six_total_price, #div_id_line_seven, #div_id_line_seven_quantity, #div_id_line_seven_unit_price, #div_id_line_seven_total_price, #div_id_line_eight, #div_id_line_eight_quantity, #div_id_line_eight_unit_price, #div_id_line_eight_total_price, #div_id_line_nine, #div_id_line_nine_quantity, #div_id_line_nine_unit_price, #div_id_line_nine_total_price, #div_id_line_ten, #div_id_line_ten_quantity, #div_id_line_ten_unit_price, #div_id_line_ten_total_price').hide()

    $('#more-line').click(function(){
        $('#div_id_line_two, #div_id_line_two_quantity, #div_id_line_two_unit_price, #div_id_line_two_total_price').slideToggle(200)
        $('#div_id_line_three, #div_id_line_three_quantity, #div_id_line_three_unit_price, #div_id_line_three_total_price').slideToggle(200)
        $('#div_id_line_four, #div_id_line_four_quantity, #div_id_line_four_unit_price, #div_id_line_four_total_price').slideToggle(200)
        $('#div_id_line_five, #div_id_line_five_quantity, #div_id_line_five_unit_price, #div_id_line_five_total_price').slideToggle(200)
        $('#div_id_line_six, #div_id_line_six_quantity, #div_id_line_six_unit_price, #div_id_line_six_total_price').slideToggle(200)
        $('#div_id_line_seven, #div_id_line_seven_quantity, #div_id_line_seven_unit_price, #div_id_line_seven_total_price').slideToggle(200)
        $('#div_id_line_eight, #div_id_line_eight_quantity, #div_id_line_eight_unit_price, #div_id_line_eight_total_price').slideToggle(200)
        $('#div_id_line_nine, #div_id_line_nine_quantity, #div_id_line_nine_unit_price, #div_id_line_nine_total_price').slideToggle(200)
        $('#div_id_line_ten, #div_id_line_ten_quantity, #div_id_line_ten_unit_price, #div_id_line_ten_total_price').slideToggle(200)
    });


   // Add event listener to line item quantity fields
$('#id_line_one_quantity, #id_line_two_quantity, #id_line_three_quantity, #id_line_four_quantity, #id_line_five_quantity, #id_line_six_quantity, #id_line_seven_quantity, #id_line_eight_quantity, #id_line_nine_quantity, #id_line_ten_quantity').on('input', function(){
    var lineOneQuantity = parseFloat($('#id_line_one_quantity').val()) || 0;
    var lineTwoQuantity = parseFloat($('#id_line_two_quantity').val()) || 0;
    var lineThreeQuantity = parseFloat($('#id_line_three_quantity').val()) || 0;
    var lineFourQuantity = parseFloat($('#id_line_four_quantity').val()) || 0;
    var lineFiveQuantity = parseFloat($('#id_line_five_quantity').val()) || 0;
    var lineSixQuantity = parseFloat($('#id_line_six_quantity').val()) || 0;
    var lineSevenQuantity = parseFloat($('#id_line_seven_quantity').val()) || 0;
    var lineEightQuantity = parseFloat($('#id_line_eight_quantity').val()) || 0;
    var lineNineQuantity = parseFloat($('#id_line_nine_quantity').val()) || 0;
    var lineTenQuantity = parseFloat($('#id_line_ten_quantity').val()) || 0;

    var totalQuantity = lineOneQuantity + lineTwoQuantity + lineThreeQuantity + lineFourQuantity + lineFiveQuantity + lineSixQuantity + lineSevenQuantity + lineEightQuantity + lineNineQuantity + lineTenQuantity;

    $('#id_total_quantity').val(totalQuantity);
});

    
$('.table').paging({limit:10});


// Scroll Top Script
   //Check to see if the window is top if not then display button
    $(window).scroll(function(){
      if ($(this).scrollTop() > 50) {
        $('.scrollToTop').fadeIn();
      } else {
        $('.scrollToTop').fadeOut();
      }
    });
  
   
    //Click event to scroll to top
    $('.scrollToTop').click(function(){
        $('html, body').animate({scrollTop : 0},800);
        return false;
      });
     //END Scroll Top Script

     $(".datetimeinput").datepicker({changeYear: true,changeMonth: true, dateFormat: 'yy-mm-dd'});
   
  });




  