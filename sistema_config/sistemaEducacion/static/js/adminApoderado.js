const targetDiv = document.getElementById("third");
const btn = document.getElementById("esconder");

btn.onclick = function(){
    if (targetDiv.style.display = "none"){
    targetDiv.style.display = "none";
    } else {
    targetDiv.style.display = "block";
    }
};
/* BOTON ELIMINAR */

function confirmarEliminar(p_run){ 
    swal.fire({
        title: '¿Estás seguro?',
        text: "El apoderado será eliminado de la base de datos",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#4CAF50',
        cancelButtonColor: '#f44336' ,
        confirmButtonText: 'Sí',
        cancelButtonText: 'No',
        reverseButtons: true,
        allowOutsideClick: false
    }).then((result) => {
        if (result.isConfirmed) {
        swal.fire({
            title: '¡Eliminado!',
            text: 'El apoderado ha sido eliminado de la base de datos',
            icon: 'success',
            allowOutsideClick: false,
            confirmButtonColor: '#4CAF50'
          }).then(function() {
              window.location.href = "/delete_apoderado/"+p_run+"/";
          })
  
        } else if (
        /* Read more about handling dismissals below */
        result.dismiss === Swal.DismissReason.cancel
        ) {
        swal.fire({
            title: 'Cancelado',
            text: 'El apoderado no ha sido eliminado',
            icon: 'error',
            confirmButtonColor: '#4CAF50'
        })
        }
    })

    
  }