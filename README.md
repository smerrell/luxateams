# Luxateams

A command line application that monitors your Teams status and sets your luxafor
flag to a corresponding color.

## Getting Started

- Register an Azure AD Application
  - go to portal.azure.com
  - Select Azure Active Directory
  - Select App Registrations
  - In App Registrations, select New registration
    - Pick a meaningful name
    - Select Accounts in any organization directory and personal Microsoft
      accounts
    - Select register application
  - create a config.json file using the config.example.json file
  - Fill in the application.id property using the Application (client) ID
  - Fill in the application.tenant property with your AAD tenant ID
  - Under Authentication, click Add a platform
  - Select Mobile and Desktop applications
  - Check the login.microsoftonline.com URL and add the URL
  - Check Allow public client flows
  - Under manifest set `allowPublicClient` to `true`
- Install dependencies using pipenv
- Run script
