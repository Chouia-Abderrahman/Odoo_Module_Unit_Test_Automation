{
    'name': '2FA by mail',
    'description': """
2FA by mail
===============
Two-Factor authentication by sending a code to the user email inbox
when the 2FA using an authenticator app is not configured.
To enforce users to use a two-factor authentication by default,
and encourage users to configure their 2FA using an authenticator app.
    """,
    'category': 'Extra Tools',
    'data': [
        'security/ir.model.access.csv',
    ],
    'license': 'LGPL-3',
}
