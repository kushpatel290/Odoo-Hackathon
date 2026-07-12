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
    'author': 'PM',
    'depends': ['base', 'mail'], 
    'data': [
        'security/ir.model.access.csv', 
        'views/menu.xml',
        'views/environmental_view.xml',
        'views/governance_view.xml',
        'views/gamification_view.xml',
        'views/social_view.xml' 
       
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}