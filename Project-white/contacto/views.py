from django.shortcuts import redirect, render
from .forms import Formcontacto
from django.core.mail import EmailMessage

def store(request):
    formulario_contacto=Formcontacto

    if request.method=="POST":
        formulario_contacto=Formcontacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            Email = request.POST.get("Email")
            contenido = request.POST.get("contenido")

            email=EmailMessage("mensaje desde App Django", "El usuario con nombre {} y {} te esccribe lo siguiente: \n\n{}".format(nombre,Email,contenido),
            "",["manuelacostafaerman@gmail.com"],reply_to=[Email])

            email.send()
            try:
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?invalido")

    return render(request,"contacto/contacto.html",{'formcontacto':formulario_contacto})
