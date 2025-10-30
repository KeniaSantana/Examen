from flask import Flask, render_template, request

app=Flask(__name__)


@app.route("/inicio", methods=["POST"])
def inicio():
    if'alimentos'not in session:
        session['alimentos']=[]
    if request.methods=='POST':
        nombre = request.form("nombre")
grasas=float(request.form['grasas'])
proteinas=float(request.form['proteinas'])
carbohidratos=float(request.form['carbohidratos'])

g=grasas * 9
p=proteinas * 4 
c= carbohidratos * 4

if g>p and g>c:
    tipo="Fuente de grasa"
elif p>g and p>c:
    tipo="Fuente de proteina"
    else
    tipo="Fuente de carbohidratos"
    session['alimentos'].append({'nombre':nombre,'tipo'=tipo})
return render_template('inicio.html')


if __name__ == "__main__":
    app.run(debug=True)



