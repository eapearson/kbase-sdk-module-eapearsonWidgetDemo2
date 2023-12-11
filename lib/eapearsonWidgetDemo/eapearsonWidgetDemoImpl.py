# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
# BEGIN DS-SERVICE-WIDGET-IMPORT
# Injected by the Dynamic Service Widget Tool
#
from widget.handlers.assets import Assets
from widget.handlers.python_widget import PythonWidget
from widget.handlers.static_widget import StaticWidget
from widget.widget_handler import add_widget

#
# END DS-SERVICE-WIDGET-IMPORT
#END_HEADER


class eapearsonWidgetDemo:
    '''
    Module Name:
    eapearsonWidgetDemo

    Module Description:
    A KBase module: eapearsonWidgetDemo
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "git@github.com:eapearson/kbase-sdk-module-eapearsonWidgetDemo.git"
    GIT_COMMIT_HASH = "0a50e1e07b6a12a1d8fb68c317580f6f7de5cd0a"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        # BEGIN DS-SERVICE-WIDGET-ADD-WIDGETS
        # Injected by the Dynamic Service Widget Tool
        #
        module_name = __name__.split('.')[:1][0]

        add_widget('assets', Assets(
            service_module_name = module_name,  # TODO: maybe can just get this inside the class?
            name = 'Assets',  # Just for logging and feedback
            path = 'assets',  # path within the widgets directory, currently widget/widgets
            config = config  # widgets often need to access configuration
        ))
        
        add_widget('first', StaticWidget(
            service_module_name = module_name,  # TODO: maybe can just get this inside the class?
            name = 'First',  # Just for logging and feedback
            path = 'first',  # path within the widgets directory, currently widget/widgets
            config = config  # widgets often need to access configuration
        ))

        add_widget('media_viewer', StaticWidget(
            service_module_name = module_name,  # TODO: maybe can just get this inside the class?
            name = 'Media Viewer (Javascript version)',  # Just for logging and feedback
            path = 'media_viewer',  # path within the widgets directory, currently widget/widgets
            config = config  # widgets often need to access configuration
        ))

        add_widget('media_viewer_py', PythonWidget(
            service_module_name = module_name,  # TODO: maybe can just get this inside the class?
            name = 'Media Viewer (Python version)',  # Just for logging and feedback
            widget_module_name = 'media_viewer',  # path within the python widgets directory, currently widget/widgets
            config = config  # widgets often need to access configuration
        ))

        add_widget('devtool', PythonWidget(
            service_module_name = module_name,  # TODO: maybe can just get this inside the class?
            name = 'Development TOol',  # Just for logging and feedback
            widget_module_name = 'devtool',  # path within the python widgets directory, currently widget/widgets
            config = config  # widgets often need to access configuration
        ))

        add_widget('config', PythonWidget(
            service_module_name = module_name,  # TODO: maybe can just get this inside the class?
            name = 'Config Viewer',  # Just for logging and feedback
            widget_module_name = 'config',  # path within the python widgets directory, currently widget/widgets
            config = config  # widgets often need to access configuration
        ))

        add_widget('demos', PythonWidget(
            service_module_name = module_name,  # TODO: maybe can just get this inside the class?
            name = 'Demos',  # Just for logging and feedback
            widget_module_name = 'demos',  # path within the python widgets directory, currently widget/widgets
            config = config  # widgets often need to access configuration
        ))      
        #
        # END DS-SERVICE-WIDGET-ADD-WIDGETS
        #END_CONSTRUCTOR
        pass

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
        #END_STATUS
        return [returnVal]
