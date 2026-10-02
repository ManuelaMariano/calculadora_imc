from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    erros = []
    resultado = none
    
    nome = ""
    peso = ""
    altura = ""

    if request.method == "POST":
        



        nome = request.form.get ("nome", "").strip()
        peso = request.form.get ("peso", "").strip()
        altura = request.form.get ("altura", "").strip()
        
       if not nome : 
        erros.append("Informe um Nome Válido")

       peso_valor = nome
        
        if not peso :
            erros.append("Informe um Peso Válido")
            else: 
                try:peso_valor=float(peso)
        
        if peso_valor > 0 or peso_valor <= 300:
            erros.append("O peso deve ser maior que 0 e até 300kg!")
     

    
        if not altura :
            erros.append("Informe uma altura válida!")
            else: 
                try:altura_valor=float(altura)
        
        if altura_valor > 0.5 or altura_valor <= 2,5:
            erros.append("A altura deve ser maior que 0,5 e menor que 2,5!")



      except ValueError: erros.append ("Peso deve ser um número válido!")

      if not erros: imc=peso_valor / (altura_valor ** 2)

      if imc < 18,5:
     faixa = "🔵Abaixo do peso" 
     classe_alerta = "alert-info"

    elif imc < 25:
    faixa = "🟢Peso Normal" 
     classe_alerta = "alert-success"

    elif imc < 30:
    faixa = "🟡Sobrepeso" 
     classe_alerta = "alert-warning"

    else imc > 30:
        faixa = "🔴Obesidade" 
     classe_alerta = "alert-danger"
        
     resultado = {
        "nome":nome,
        "peso" : peso_valor,
        "altura" : altura_valor
        "imc": imc
        "faixa": faixa
        "classe-alerta" classe_alerta

     }   
        
     return render_template ("index.html",
     erros=erros, 
     resultado=resultado,
     nome=nome, 
     peso=peso, 
     altura=altura)   
        
      @app.route ("/equipe")
      def equipe (): 
        return render_template ("equipe.html")



 







#------

if __name__ == "__main__": 
    app.run(debug=True)