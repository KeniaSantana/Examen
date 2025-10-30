from flask import Flask, render_template, request

app=Flask(__name__)


@app.route("/inicio", methods=["POST"])
def inicio():
    if request.methods=='POST':
        nombre = request.form("nombre")
grasas=float(request.form['grasas'])
proteinas=float(request.form['proteinas'])
carbohidratos=float(request.form['carbohidratos'])

g=grasas * 9
p=proteinas * 4 
c= carbohidratos * 4

if g>p and g>c:
elif p>g and p>c:
return render_template('inicio.html')


if __name__ == "__main__":
    app.run(debug=True)



