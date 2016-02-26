"""
  Provides info about planets next to pretty pictures.
  @author Josh Snider
"""

from flask import Flask
from flask import render_template
import os
app = Flask(__name__,
  static_url_path=os.path.join(os.path.dirname(__file__),'/src/_site'))

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_page(path):
  print("trying to get " + path)
  return app.send_static_file(path)

@app.errorhandler(404)
def page_not_found(e):
  """Custom 404 error."""
  return app.send_static_file('404.html')

@app.errorhandler(500)
def application_error(e):
  """TODO custom 500 error."""
  return 'Sorry, unexpected error: {}'.format(e), 500

