(function () {
  const btnEliminacion = document.querySelectorAll(".btnEliminacion");

  btnEliminacion.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      const confirmacion = confirm("¿Esta seguro de eliminar el Vehiculo?");
      if (!confirmacion) {
        e.preventDefault();
      }
    });
  });
})();
