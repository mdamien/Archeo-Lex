# -*- coding: utf-8 -*-
# 
# Archéo Lex – Pure Histoire de la Loi française
# – crée un dépôt Git des lois françaises écrites en syntaxe Markdown
# – ce module comprend diverses fonctions utilitaires
# 
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# the LICENSE file for more details.

# Imports
import os
import re
import subprocess
import datetime
import time
import shutil

MOIS = {
    'janvier': '01',
    'février': '02',
    'mars': '03',
    'avril': '04',
    'mai': '05',
    'juin': '06',
    'juillet': '07',
    'août': '08',
    'septembre': '09',
    'octobre': '10',
    'novembre': '11',
    'décembre': '12'
}


MOIS2 = ['', 'janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']


def normalisation_code(code):
    
    nom = ''
    repertoire = ''
    
    if code.startswith(('code', 'Code')):
        code = re.sub('\'', '’', code.lower())
        nom = re.sub('[-_]', ' ', code)
        nom = nom[0].upper() + nom[1:]
        repertoire = re.sub('[ _]', '-', code)
        nom = re.sub(' ', '_', re.sub('é', 'e', nom))
    else:
        nom = code.lower()
        repertoire = code.lower()
    
    return repertoire, nom


def normalise_date(texte):
    
    texte = texte.strip()
    if texte == '2999-01-01' or not texte:
        return None
    fm = re.match('(\d{4})-(\d{2})-(\d{2})', texte)
    if not fm:
        return None
    return datetime.date(int(fm.group(1)), int(fm.group(2)), int(fm.group(3)))


def normalise_datetime(texte):
    
    texte = texte.strip()
    fm = re.match('(\d{4})(\d{2})(\d{2})-(\d{2})(\d{2})(\d{2})', texte)
    if not fm:
        return None
    return datetime.datetime(int(fm.group(1)), int(fm.group(2)), int(fm.group(3)), int(fm.group(4)), int(fm.group(5)), int(fm.group(6)))


def comp_infini(x, y):
    
    dateinf = datetime.date(2999, 1, 1)

    if isinstance(x, str):
        x = datetime.date(*(time.strptime(x, '%Y-%m-%d')[0:3]))
    if isinstance(y, str):
        y = datetime.date(*(time.strptime(y, '%Y-%m-%d')[0:3]))
    if x == dateinf:
        x = None
    if y == dateinf:
        y = None

    if x == y:
        return 0;
    elif x == None:
        return 1
    elif y == None:
        return -1
    return -2 * int(x < y) + 1


def comp_infini_strict(x, y):
    
    dateinf = datetime.date(2999, 1, 1)

    if isinstance(x, str):
        x = datetime.date(*(time.strptime(x, '%Y-%m-%d')[0:3]))
    if isinstance(y, str):
        y = datetime.date(*(time.strptime(y, '%Y-%m-%d')[0:3]))
    if x == dateinf:
        x = None
    if y == dateinf:
        y = None

    if x == None and y == None:
        return False
    elif x == None:
        return False
    elif y == None:
        return True
    return x < y


def comp_infini_large(x, y):
    
    dateinf = datetime.date(2999, 1, 1)

    if isinstance(x, str):
        x = datetime.date(*(time.strptime(x, '%Y-%m-%d')[0:3]))
    if isinstance(y, str):
        y = datetime.date(*(time.strptime(y, '%Y-%m-%d')[0:3]))
    if x == dateinf:
        x = None
    if y == dateinf:
        y = None

    if x == y:
        return True
    elif x == None:
        return False
    elif y == None:
        return True
    return x < y


def min_date_infini( x, y ):

    if x == None:
        return y
    elif y == None:
        return x
    elif x < y:
        return x
    return y

# vim: set ts=4 sw=4 sts=4 et:
