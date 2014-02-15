__author__ = 'mnowotka'

from chembl_beaker.beaker import app
from chembl_beaker.beaker.core_apps.descriptors.impl import _getNumAtoms, _getLogP, _getTPSA, _getMolWt, _getDescriptors
from bottle import request
import base64
import json

#-----------------------------------------------------------------------------------------------------------------------

@app.get('/getNumAtoms/<ctab>', name="getNumAtoms")
def getNumAtoms(ctab):
    """
Counts number of atoms of given compounds. CTAB is urlsafe_base64 encoded string containing single molfile or
concatenation of multiple molfiles.
    """

    data = base64.urlsafe_b64decode(ctab)
    return json.dumps(_getNumAtoms(data))

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/getNumAtoms', method=['OPTIONS', 'POST'], name="getNumAtoms")
def getNumAtoms():
    """
Counts number of atoms of given compounds. CTAB is either single molfile or SDF file.
    """

    data = request.body.getvalue()
    return json.dumps(_getNumAtoms(data))

#-----------------------------------------------------------------------------------------------------------------------

@app.get('/logP/<ctab>', name="logP")
def logP(ctab):
    """
Returns the logP value for a molecule. CTAB is urlsafe_base64 encoded string containing single molfile or
concatenation of multiple molfiles.
    """

    data = base64.urlsafe_b64decode(ctab)
    return json.dumps(_getLogP(data))

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/logP', method=['OPTIONS', 'POST'], name="logP")
def logP():
    """
Returns the logP value for a molecule. CTAB is either single molfile or SDF file.
    """

    data = request.body.getvalue()
    return json.dumps(_getLogP(data))

#-----------------------------------------------------------------------------------------------------------------------

@app.get('/tpsa/<ctab>', name="tpsa")
def tpsa(ctab):
    """
Returns the TPSA value for a molecule. CTAB is urlsafe_base64 encoded string containing single molfile or
concatenation of multiple molfiles.
    """

    data = base64.urlsafe_b64decode(ctab)
    return json.dumps(_getTPSA(data))

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/tpsa', method=['OPTIONS', 'POST'], name="tpsa")
def tpsa():
    """
Returns the TPSA value for a molecule. CTAB is either single molfile or SDF file.
    """

    data = request.body.getvalue()
    return json.dumps(_getTPSA(data))

#-----------------------------------------------------------------------------------------------------------------------

@app.get('/molWt/<ctab>', name="molWt")
def molWt(ctab):
    """
Returns molecular weight of a compound. CTAB is urlsafe_base64 encoded string containing single molfile or
concatenation of multiple molfiles.
    """

    data = base64.urlsafe_b64decode(ctab)
    return json.dumps(_getMolWt(data))
#-----------------------------------------------------------------------------------------------------------------------

@app.route('/molWt', method=['OPTIONS', 'POST'], name="molWt")
def molWt():
    """
Returns molecular weight of a compound. CTAB is either single molfile or SDF file.
    """

    data = request.body.getvalue()
    return json.dumps(_getMolWt(data))

#-----------------------------------------------------------------------------------------------------------------------

@app.get('/descriptors/<ctab>', name="descriptors")
def descriptors(ctab):
    """
Returns descriptors of a compound. CTAB is urlsafe_base64 encoded string containing single molfile or
concatenation of multiple molfiles.
    """

    data = base64.urlsafe_b64decode(ctab)
    return json.dumps(_getDescriptors(data))
#-----------------------------------------------------------------------------------------------------------------------

@app.route('/descriptors', method=['OPTIONS', 'POST'], name="descriptors")
def descriptors():
    """
Returns descriptors of a compound. CTAB is either single molfile or SDF file.
    """

    data = request.body.getvalue()
    return json.dumps(_getDescriptors(data, request.params))

#-----------------------------------------------------------------------------------------------------------------------