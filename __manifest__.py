{
    'name': 'EcoSphere: ESG Management Platform',
    'version': '1.0',
    'category': 'Operations',
    'summary': 'Manage Environmental, Social, and Governance performance',

    'description': """
        EcoSphere ESG Management Platform
        =================================
        A centralized application to track carbon emissions, promote employee participation 
        through gamification, and maintain governance compliance.
    """,

    'author': ' Kush Patel,Parva Mehta' ,

    'depends': [
        'base',
        'mail',
    ],

    'data': [
        # Security
        'security/ir.model.access.csv',

        # Initial Data
        'data/badge_data.xml',
        'data/reward_data.xml',

        # Views
        'views/menu.xml',
        'views/environmental_view.xml',
        'views/social_view.
        'views/governance_view.xml',
        'views/gamification_view.xml',
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}