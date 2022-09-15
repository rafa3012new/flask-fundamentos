
window.onload = function(){
    
    var tabla_frutas_main = document.getElementsByClassName("tabla_frutas")[0]
    var tabla_frutas_cuerpo = tabla_frutas_main.getElementsByTagName("tbody")[0]
    var tabla_frutas_fila;
    var tabla_frutas_celda3;
    var tabla_frutas_celda3_select;

    for(var i=1;i<=tabla_frutas_cuerpo.rows.length;i++){
        tabla_frutas_fila = tabla_frutas_cuerpo.getElementsByTagName("tr")[i];
        tabla_frutas_celda3 = tabla_frutas_fila.getElementsByTagName("td")[2];        
        tabla_frutas_celda3_select = tabla_frutas_celda3.getElementsByTagName("select")[0];
        tabla_frutas_celda3_select.addEventListener("change",cambiovalor,false)
    }
  
  }
  
  function cambiovalor(){
     this.parentNode.parentNode.getElementsByTagName("td")[3].innerText = parseFloat(this.parentNode.parentNode.getElementsByTagName("td")[1].innerText * parseFloat(this.value));    
  }