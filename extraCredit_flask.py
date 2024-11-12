# DATA602 FALL 2024
# Stephanie Chiang

from flask import Flask, request

main_page = '''
<html>
    <head>
    <title></title>
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.min.css">
    </head>
<body>
<form class="form-horizontal" method="post" action="/calc">
<fieldset>
<!-- Form Name -->
<legend>Multiplier</legend>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="textinput">Number</label>
  <div class="col-md-4">
  <input id="textinput" type="number" name='number' placeholder="Enter a number" class="form-control input-md">
  </div>
</div>
<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="singlebutton"></label>
  <div class="col-md-4">
    <button id="singlebutton" name="singlebutton" class="btn btn-primary">Calculate</button>
  </div>
</div>
</fieldset>
</form>
<script src="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
</body>
</html>
'''
    # ------ Place code below here \/ \/ \/ ------

app = Flask(__name__)

@app.route('/')
def index():
  return main_page

@app.post('/calc')
def calculate():
  n = request.form['number']
  result = f'<center>5 x {n} = {str(int(n) * 5)}</center>'
  return main_page + result

if __name__ == '__main__':
  app.run(debug=True)

    # ------ Place code above here /\ /\ /\ ------
