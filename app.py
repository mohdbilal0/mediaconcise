from flask import Flask,render_template,request,send_from_directory
import itranscript as it
import extractive as ex
import ytranscript as yt
import vtranscript as vt
import abstractive as ab
import os
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('yta.html')

# @app.errorhandler(Exception)
# def handle_error(error):
#     return render_template('error.html', summary="error occured"), 500

@app.errorhandler(IndexError)
def handle_custom_exception(error):
    return render_template('error.html', summary="empty field"), 500

@app.errorhandler(FileNotFoundError)
def handle_custom_exception(error):
    return render_template('error.html', summary="empty file"), 500

@app.errorhandler(OSError)
def handle_custom_exception(error):
    return render_template('error.html', summary="empty file"), 500
    
@app.errorhandler(KeyError)
def handle_custom_exception(error):
    return render_template('error.html', summary="cannot recognize character"), 500

# video summary ---------------------------------------------->
# video summarry extract method start ------------------------>
@app.route('/vde',methods=['GET','POST'])
def vde():
    if request.method=='POST':
        return render_template('vde.html')

@app.route('/vdesubmit',methods=['GET','POST'])
def vdesubmit():
    if request.method=='POST':
        file=request.files['file']
        file.save(os.path.join('uploads', "video.mp4"))
        vid='uploads/'+"video.mp4"
        text=vt.extract_vid(vid)
        summary=ex.extract(text)
        return render_template('vde.html',summary=summary)
# video summarry extract method end ------------------------->
# video summarry abstract method start ------------------------->
@app.route('/vda',methods=['GET','POST'])
def vda():
    if request.method=='POST':
        return render_template('vda.html')

@app.route('/vdasubmit',methods=['GET','POST'])
def vdasubmit():
    if request.method=='POST':
        file=request.files['file']
        file.save(os.path.join('uploads', "video.mp4"))
        vid='uploads/'+"video.mp4"
        text=vt.extract_vid(vid)
        summary=ab.abstract(text)
        return render_template('vda.html',summary=summary,f=vid)
# video summarry abstract method end ------------------------->

# image summary abstract method start ------------------------->
@app.route('/ima',methods=['GET','POST'])
def ima():
    if request.method=='POST':
        return render_template('ima.html')

@app.route('/imasubmit',methods=['GET','POST'])
def imasubmit():
    if request.method=='POST':
        file=request.files['file']
        file.save(os.path.join('uploads', file.filename))
        text=it.extract_img(file)
        summary=ab.abstract(text)
        return render_template('ima.html',summary=summary)
# image summary abstract method end ------------------------->

# image summary extract method start ------------------------->
@app.route('/ime',methods=['GET','POST'])
def ime():
    if request.method=='POST':
        return render_template('ime.html')

@app.route('/imesubmit',methods=['GET','POST'])
def imesubmit():
    if request.method=='POST':
        file=request.files['file']
        file.save(os.path.join('uploads', file.filename))
        text=it.extract_img(file)
        summary=ex.extract(text)
        return render_template('ime.html',summary=summary)
# image summary extract method end ------------------------->


# youtube summary extract method start ------------------------->
@app.route('/yte',methods=['GET','POST'])
def yte():
    if request.method=='POST':
        return render_template('yte.html')

@app.route('/ytesubmit',methods=['GET','POST'])
def ytesubmit():
    if request.method=='POST':
        link=request.form['link']
        text=yt.extract_ytube(link)
        summary=ex.extract(text)
        return render_template('yte.html',summary=summary)
# youtube summary extract method end ------------------------->

# youtube summary abstract method start ------------------------->
@app.route('/yta',methods=['GET','POST'])
def yta():
    if request.method=='POST':
        return render_template('yta.html')

@app.route('/ytasubmit',methods=['GET','POST'])
def ytasubmit():
    if request.method=='POST':
        link=request.form['link']
        text=yt.extract_ytube(link)
        summary=ab.abstract(text)
        return render_template('yta.html',summary=summary)
# youtube summary abstract method end ------------------------->
# text summary extract method start ------------------------->
@app.route('/txe',methods=['GET','POST'])
def txe():
    if request.method=='POST':
        return render_template('txe.html')

@app.route('/txesubmit',methods=['GET','POST'])
def txesubmit():
    if request.method=='POST':
        text=request.form['text']
        summary=ex.extract(text)
        return render_template('txe.html',summary=summary)
# text summary extract method end ------------------------->

# text summary abstract method start ------------------------->
@app.route('/txa',methods=['GET','POST'])
def txa():
    if request.method=='POST':
        return render_template('txa.html')

@app.route('/txasubmit',methods=['GET','POST'])
def txasubmit():
    if request.method=='POST':
        text=request.form['text']
        summary=ab.abstract(text)
        return render_template('txa.html',summary=summary)
# text summary abstract method end ------------------------->





if __name__=='__main__':
    app.run(debug=True)