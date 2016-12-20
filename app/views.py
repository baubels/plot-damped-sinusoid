from flask import Flask,render_template, request
from app import model
from app import app
from app import compute
from model import InputForm

@app.route('/', methods=['GET','POST'])
@app.route('/main', methods=['GET','POST'])

def main():
    form = InputForm()
    if form.validate_on_submit():
        for field in form:
            exec('%s = %s'%(field.name,field.data))

        #Deprecated - writes file to disk
        #val=compute.compute(A,b,w,T)
        #val='/'+val
        if SVG:
            val=compute.compute_svg(A, b, w, T)
        else:
            val=compute.compute_nofile(A,b,w,T)
        return render_template('result.html', form=form, val=val)
    else:
        val = None
        return render_template('main.html', form=form, val=val)

# @app.route('/result', methods=['GET','POST'])
# def result():
# 	val = None
#  	return render_template('result.html',val=val)
