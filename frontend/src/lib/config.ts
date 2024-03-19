const config = {
    siteName: 'CrashDash',
    siteDescription: 'Educate yourself about traffic safety',
    nav: [
      {
        name: 'Home',
        path: '/'
      },
      {
        name: 'Dashboard',
        path: '/dashboard/'
      },
      {
        name: 'GitHub Repo',
        path: 'https://github.com/DHClimber/CIS4301'
      }
    ],
    queries: [
        'SELECT * from Crashes',
        'SELECT * from People'
    ]
  }
  
  export default config