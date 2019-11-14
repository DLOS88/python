from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/upload')#nombre de la paguina
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      lista = [x.split(';') for x in open(f.filename).readlines()]
      print (lista)
      listatotal=[]
      for i in lista:
         lista2=[]
         lista2.append(int(i[0]))
         lista2.append(str(i[2][0]))
         lista2.append(int(i[1]))
         if i[2][0]=='+':
            lista2.append(lista2[0]+lista2[2])
         elif i[2][0]=='-':
            lista2.append(lista2[0]-lista2[2])
         elif i[2][0]=='*':
            lista2.append(lista2[0]*lista2[2])
         elif i[2][0]=='/':
            lista2.append(lista2[0]/lista2[2])
         listatotal.append(lista2)
      print (listatotal)

      return render_template('showall.html', msg = "file loaded successfully", rows = listatotal)

if __name__ == '__main__':
   app.run(debug = True)
