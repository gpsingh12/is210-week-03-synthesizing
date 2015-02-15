#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition
FLEMISH = inquisition.SPANISH
FLEMISH.index('Spanish')
FLEMISH = FLEMISH[:19] + 'Flemish' + FLEMISH[26:]
