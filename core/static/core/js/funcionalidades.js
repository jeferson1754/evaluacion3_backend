function Confirm_Delete(id) {
    Swal.fire({
        title: "Desea eliminar?",
        text: "Desea eliminarlo!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, eliminar!"
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Deleted!",
                text: "Se ha eliminado.",
                icon: "success"
            }).then(() => {
                window.location.href = "eliminar/" + id;
            });

        }
    });
}