
    var chat = (function(){

        var 
        templateUno = '<table class="invoice-template"> ' +
        '<tbody>' +
        '<tr>' +
          '<td>[[name]]</td>' +
          '<td>[[cantidad]]</td>' +
          '<td>[[fecha]]</td>' +
          '<td>$64.50</td>' +
        '</tr>' +
        '</tbody>'+
        '</table>' ,

        rowinvoice = function(name, date, message) {
          var contenedor = document.querySelector(".invoice-template");
          contenedor.innerHTML += templateUno.replace("[[name]]", name).replace("[[cantidad]]", date).replace("[[fecha]]", message); 
        },
  
    
        init = function() {};
  
        return {
          init: init,
          rowinvoice: rowinvoice,
        }
  
      })();