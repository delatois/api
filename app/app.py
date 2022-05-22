# -*- coding: utf-8 -*-

from __future__ import absolute_import
import os

import falcon

from .assets import Assets
from .configuration import Configuration
from .pairs import Pairs
from .settings import LOGGER

app = falcon.App()
app.req_options.auto_parse_form_urlencoded = True
app.req_options.strip_url_path_trailing_slash = True
app.add_route('/assets', Assets())
app.add_route('/configuration', Configuration())
app.add_route('/pairs', Pairs())


if __name__ == '__main__':
    port = int(os.getenv('PORT') or 3000)
    LOGGER.info('Starting on port %s ...', port)

    import bjoern
    bjoern.run(app, '', port)