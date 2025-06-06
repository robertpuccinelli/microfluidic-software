"""
Purpose:

Create an application that listens for commands on a specified port. Commands are used to operate a microfluidic controller or provide status information.
"""

from flask import Flask
import logging
from plfluidics.server.controller import MicrofluidicController


logging.basicConfig(filename='purifier.log', filemode='a', format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%H:%M:%S')
log_format = '%(asctime)s - %(levelname)s - %(message)s [%(name)s]'

ctrl = MicrofluidicController()

app_server = Flask(__name__)
app_server.static_folder = ctrl.templatesDir()
app_server.template_folder = ctrl.templatesDir()

app_server.add_url_rule('/', view_func=ctrl.renderPage, methods=['GET'])

# CONFIG PAGE
app_server.add_url_rule('/configPreview', view_func=ctrl.configPreview, methods=['POST'])
app_server.add_url_rule('/configSave', view_func=ctrl.configSave, methods=['POST'])
app_server.add_url_rule('/configLoad', view_func=ctrl.configLoad, methods=['POST'])


# CONTROL PAGE
# Config
app_server.add_url_rule('/changeConfig', view_func=ctrl.configChange, methods=['POST'])
app_server.add_url_rule('/reloadConfig', view_func=ctrl.configReload, methods=['POST'])
# Script
app_server.add_url_rule('/loadScript', view_func=ctrl.scriptLoad, methods=['POST'])
app_server.add_url_rule('/saveScript', view_func=ctrl.scriptSave, methods=['POST'])
app_server.add_url_rule('/toggleScript', view_func=ctrl.scriptToggle, methods=['POST'])
app_server.add_url_rule('/skipScript', view_func=ctrl.scriptSkip, methods=['POST'])
app_server.add_url_rule('/stopScript', view_func=ctrl.scriptStop, methods=['POST'])
# Valves
app_server.add_url_rule('/toggleValve', view_func=ctrl.valveToggle, methods=['POST'])
app_server.add_url_rule('/closeValves', view_func=ctrl.valveCloseList, methods=['POST'])
app_server.add_url_rule('/openValves', view_func=ctrl.valveOpenList, methods=['POST'])


if __name__ == '__main__':
    app_server.run(host='0.0.0.0', port=5454, debug=False)