# -*- coding: utf-8 -*-
"""This module executes or application."""

from API import app
import os


if __name__ == '__main__':
    port = os.getenv('PORT') or 5000
    app.run(host='0.0.0.0', port=port)
