from flask import Flask, render_template, redirect, url_for, request
from models import Student

app = Flask(__name__)


@app.route('/')
@app.route('/showstudents')
def index():
    students = Student.select()
    return render_template('index.html', students=students)


@app.route('/details/<int:id>')
def details(id):
    students = Student.get_by_id(id)
    return render_template('details.html', student=students)


@app.route('/delete/<int:id>')
def delete(id):
    student = Student.get_by_id(id)
    student.delete_instance()
    return redirect(url_for('index'))


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        name = request.form['n']
        family = request.form.get('f')
        # sol1
        # Student.create(name=name, family=family)
        # sol2
        # st1 = Student(name=name, family=family)
        # st1.save()
        # sol3
        q = Student.insert(name=name, family=family)
        q.execute()
        return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    st = Student.get_by_id(id)
    if request.method == 'POST':
        name = request.form['n']
        family = request.form.get('f')
        st.name = name
        st.family = family
        st.save()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        return render_template('update.html', st=st)


@app.route('/hello')
def hello():
    return 'hello'


if __name__ == "__main__":
    app.run(debug=True)
