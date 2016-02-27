"""
  Provides info about planets next to pretty pictures.
  @author Josh Snider
"""

from flask import Flask
from flask import render_template
import os
app = Flask(__name__)

@app.route('/api/tagline/')
def get_tagline():
  return "An attempt at a blog by someone who thinks Haskell is cool."

@app.errorhandler(404)
def page_not_found(e):
  """Custom 404 error."""
  return render_template('404.html')

@app.errorhandler(500)
def application_error(e):
  """Custom 500 error."""
  return 'Sorry, unexpected error: {}'.format(e), 500

