# -*- coding: utf-8 -*-
{
    'name': "zadatak5",

    'summary': """
        Na objekt zaposlenik dodati polje za upis djece. Moguće je unijeti više djece i za svako od njih upisati
ime i prezime te datum rođenja. Prikazati polje na form viewu, u tabu Private information, ispod
polja za broj djece (children). Prikazati polje samo ako je broj djece veći od 0""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/zadatak5.xml',

    ],
}