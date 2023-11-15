#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys, os

def logger(run_dir):
    logger = logging.getLogger(run_dir)

    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger