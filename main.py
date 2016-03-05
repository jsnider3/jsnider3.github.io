"""
  Provides info about planets next to pretty pictures.
  @author Josh Snider
"""

from flask import Flask
from flask import render_template
from flask import request
import os
app = Flask(__name__)

@app.route('/api/tagline/')
def get_tagline():
  taglines = [
    "An attempt at a blog by someone who thinks Haskell is cool.",
    "Contains 20% of your daily recommended dose of HTML.",
    "Powered by the cloud."
  ]
  ind = hash(request.args.get('page', '')) - hash('')
  return taglines[ind % len(taglines)]

@app.route('/.well-known/acme-challenge/CLubHhYvkZj2ndjHNsETwDNvj6KriherBtAPhDNUTqw')
def letsencrypt_challenge():
  return "CLubHhYvkZj2ndjHNsETwDNvj6KriherBtAPhDNUTqw.RJszauNUxRavajsIJkOIl7hqRX-t5gk6J0vd7-RyIf8"

@app.route('/.well-known/acme-challenge/gqfq8DC9iaLftcGGyMr4k0xExSWMmZKs5Gyg3wPm0HA')
def letsencrypt_challenge2():
  return "gqfq8DC9iaLftcGGyMr4k0xExSWMmZKs5Gyg3wPm0HA.RJszauNUxRavajsIJkOIl7hqRX-t5gk6J0vd7-RyIf8"

@app.errorhandler(404)
def page_not_found(e):
  """Custom 404 error."""
  return render_template('404.html')

@app.errorhandler(500)
def application_error(e):
  """Custom 500 error."""
  return 'Sorry, unexpected error: {}'.format(e), 500

