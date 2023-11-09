def importeTotalCarro(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total + float(value["precio"])

    else:
        total = "Debes iniciar sesión."
    return {"importeTotalCarro": total}