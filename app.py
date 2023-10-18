from flask import Flask,render_template

FAI=Flask(__name__)


@FAI.route('/wish')
def wish(name):
    return f'Hi {name} How are You'

@FAI.route('/first')
def first():
    return render_template('first.html',name='Shashi')
@FAI.route('/second')
def second():
    return render_template('second.html')
if __name__=='__main__':
    FAI.run(debug=True,host='192.168.0.106',port=5003)
