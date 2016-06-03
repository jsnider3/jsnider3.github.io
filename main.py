"""
  Provides info about planets next to pretty pictures.
  @author Josh Snider
"""

import datetime
from flask import Flask
from flask import render_template
from flask import request
import os
app = Flask(__name__)

def get_date_specific_tagline():
  today = datetime.datetime.now()
  if today.month == 3 and today.day == 14:
    return "Happy Pi Day!"
  elif today.month == 6 and today.day == 28:
    return "Happy Tau Day!"
  return None

@app.route('/api/tagline/')
def get_tagline():
  tag = get_date_specific_tagline()
  if tag != None:
    return tag
  taglines = [
    "An attempt at a blog by someone who thinks Haskell is cool.",
    "Contains 20% of your daily recommended dose of HTML.",
    "Powered by the cloud."
  ]
  ind = hash(request.args.get('page', '')) - hash('')
  return taglines[ind % len(taglines)]

@app.route('/.well-known/acme-challenge/<challenge>')
def letsencrypt_challenge(challenge):
  challenges = {'CLubHhYvkZj2ndjHNsETwDNvj6KriherBtAPhDNUTqw':
                "CLubHhYvkZj2ndjHNsETwDNvj6KriherBtAPhDNUTqw.RJszauNUxRavajsIJkOIl7hqRX-t5gk6J0vd7-RyIf8",
                '_C9gSbyYY37KIHciLfDdCoe6hd-nPd-8U9g_Z9yoThQ' :
                "_C9gSbyYY37KIHciLfDdCoe6hd-nPd-8U9g_Z9yoThQ.qmY1wTTHo_ar0hB2Nw-6lovfLHRSG0AQjy_5KR7piDI",
                'mxF4QaUO0x7krLUqqJaO2KmKRa_TZJ8cAPUdumaJNM8' :
                "mxF4QaUO0x7krLUqqJaO2KmKRa_TZJ8cAPUdumaJNM8.qmY1wTTHo_ar0hB2Nw-6lovfLHRSG0AQjy_5KR7piDI",
                'QX4_mvMA4yskTxWonFV53qSovItH_TJBqPhEQCGGhcs' :
                "QX4_mvMA4yskTxWonFV53qSovItH_TJBqPhEQCGGhcs.qmY1wTTHo_ar0hB2Nw-6lovfLHRSG0AQjy_5KR7piDI",
                '5B5DrY09IPZZP0MOknFsNXlW1Uqpmn_6FnhoVpoCKFw' :
                "5B5DrY09IPZZP0MOknFsNXlW1Uqpmn_6FnhoVpoCKFw.qmY1wTTHo_ar0hB2Nw-6lovfLHRSG0AQjy_5KR7piDI",
                '6tSRS4N9-8uC2lnh8MdmpbCtMVTteE22LtgTNaSVJmM' :
                "6tSRS4N9-8uC2lnh8MdmpbCtMVTteE22LtgTNaSVJmM.qmY1wTTHo_ar0hB2Nw-6lovfLHRSG0AQjy_5KR7piDI",
                'cQZJOUSdGqf1O2Md3wjP0VIp4qT3VFtgZqs2cbtGa_o' :
                "cQZJOUSdGqf1O2Md3wjP0VIp4qT3VFtgZqs2cbtGa_o.qmY1wTTHo_ar0hB2Nw-6lovfLHRSG0AQjy_5KR7piDI",
                'gqfq8DC9iaLftcGGyMr4k0xExSWMmZKs5Gyg3wPm0HA' :
                "gqfq8DC9iaLftcGGyMr4k0xExSWMmZKs5Gyg3wPm0HA.RJszauNUxRavajsIJkOIl7hqRX-t5gk6J0vd7-RyIf8"}
  return challenges[challenge]

@app.errorhandler(404)
def page_not_found(e):
  """Custom 404 error."""
  return render_template('404.html')

@app.errorhandler(500)
def application_error(e):
  """Custom 500 error."""
  return 'Sorry, unexpected error: {}'.format(e), 500

