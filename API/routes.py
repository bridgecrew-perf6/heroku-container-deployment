# -*- coding: utf-8 -*-
"""This module creates the routes for our API."""

import random

from flask import request

from API import app


@app.route('/api/v1', methods=['GET'])
@app.route('/', methods=['GET'])
def api_home() -> dict:
    """Handle get requests to /api/v1 route.

    Returns
    -------
    dict:
        A dictionary showing:
        {
            'data': 'Hello from shileds.io json endpoint'
        }
    """
    data = {
        'data': 'Hello from shileds.io json endpoint'
    }

    return data, 200
